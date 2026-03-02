# notifications/utils.py
from .models import ThongBao


def create_notification(nguoi_nhan, loai, tieu_de, noi_dung='', lien_ket=''):
    """
    Hàm tiện ích tạo thông báo. Gọi từ bất kỳ view nào.
    
    Ví dụ:
        create_notification(
            nguoi_nhan=user,
            loai='TRIP_APPROVED',
            tieu_de='Chuyến đi đã được duyệt',
            noi_dung='Chuyến đi "Fansipan" đã được Admin duyệt.',
            lien_ket='/chuyen-di/54/fansipan/'
        )
    """
    return ThongBao.objects.create(
        nguoi_nhan=nguoi_nhan,
        loai=loai,
        tieu_de=tieu_de,
        noi_dung=noi_dung,
        lien_ket=lien_ket
    )
