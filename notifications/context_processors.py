# notifications/context_processors.py
from .models import ThongBao


def notification_context(request):
    """Inject số thông báo chưa đọc vào mọi template (qua navbar)"""
    if request.user.is_authenticated:
        unread_count = ThongBao.objects.filter(
            nguoi_nhan=request.user, da_doc=False
        ).count()
        return {'unread_notification_count': unread_count}
    return {'unread_notification_count': 0}
