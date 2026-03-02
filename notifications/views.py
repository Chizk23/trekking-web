# notifications/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator
import json

from .models import ThongBao


@login_required
def notification_list(request):
    """Trang danh sách thông báo đầy đủ"""
    qs = ThongBao.objects.filter(nguoi_nhan=request.user)
    paginator = Paginator(qs, 20)
    page = request.GET.get('page', 1)
    notifications = paginator.get_page(page)

    # Determine base template (admin vs user)
    is_admin_view = request.path.startswith('/dashboard/')
    base_template = 'admin_base.html' if is_admin_view else 'base.html'

    return render(request, 'notifications/notification_list.html', {
        'notifications': notifications,
        'page_title': 'Thông báo',
        'base_template': base_template,
    })


@login_required
@require_POST
def mark_as_read(request, pk):
    """API đánh dấu 1 thông báo đã đọc"""
    try:
        notif = ThongBao.objects.get(pk=pk, nguoi_nhan=request.user)
        notif.da_doc = True
        notif.save(update_fields=['da_doc'])
        return JsonResponse({'status': 'success'})
    except ThongBao.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Không tìm thấy.'}, status=404)


@login_required
@require_POST
def mark_all_read(request):
    """API đánh dấu tất cả đã đọc"""
    count = ThongBao.objects.filter(
        nguoi_nhan=request.user, da_doc=False
    ).update(da_doc=True)
    return JsonResponse({'status': 'success', 'count': count})


@login_required
@require_POST
def delete_notification(request, pk):
    """Xóa 1 thông báo"""
    try:
        notif = ThongBao.objects.get(pk=pk, nguoi_nhan=request.user)
        notif.delete()
        return JsonResponse({'status': 'success'})
    except ThongBao.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Không tìm thấy.'}, status=404)


@login_required
@require_POST
def delete_selected(request):
    """Xóa nhiều thông báo đã chọn (nhận danh sách IDs)"""
    try:
        data = json.loads(request.body)
        ids = data.get('ids', [])
    except (json.JSONDecodeError, AttributeError):
        ids = request.POST.getlist('ids')
    
    if not ids:
        return JsonResponse({'status': 'error', 'message': 'Chưa chọn thông báo nào.'}, status=400)
    
    count = ThongBao.objects.filter(
        pk__in=ids, nguoi_nhan=request.user
    ).delete()[0]
    return JsonResponse({'status': 'success', 'count': count})


@login_required
@require_POST
def delete_all(request):
    """Xóa tất cả thông báo"""
    count = ThongBao.objects.filter(nguoi_nhan=request.user).delete()[0]
    return JsonResponse({'status': 'success', 'count': count})


@login_required
def notification_count_api(request):
    """API trả về số thông báo chưa đọc (cho polling từ navbar)"""
    count = ThongBao.objects.filter(
        nguoi_nhan=request.user, da_doc=False
    ).count()
    return JsonResponse({'count': count})


@login_required
def notification_dropdown_api(request):
    """API trả về 5 thông báo gần nhất (cho dropdown navbar)"""
    notifs = ThongBao.objects.filter(
        nguoi_nhan=request.user
    )[:5]

    data = []
    for n in notifs:
        data.append({
            'id': n.id,
            'tieu_de': n.tieu_de,
            'noi_dung': n.noi_dung[:100],
            'lien_ket': n.lien_ket,
            'icon': n.icon,
            'da_doc': n.da_doc,
            'ngay_tao': n.ngay_tao.strftime('%d/%m %H:%M'),
        })

    return JsonResponse({'notifications': data})
