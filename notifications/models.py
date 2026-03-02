# notifications/models.py
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class ThongBao(models.Model):
    """Model lưu thông báo cho User & Admin"""

    class LoaiThongBao(models.TextChoices):
        # Trips
        TRIP_APPROVED = 'TRIP_APPROVED', _('Chuyến đi được duyệt')
        TRIP_REJECTED = 'TRIP_REJECTED', _('Chuyến đi bị từ chối')
        MEMBER_JOINED = 'MEMBER_JOINED', _('Có người xin vào chuyến đi')
        MEMBER_APPROVED = 'MEMBER_APPROVED', _('Được duyệt vào chuyến đi')
        MEMBER_REJECTED = 'MEMBER_REJECTED', _('Bị từ chối khỏi chuyến đi')
        # Treks
        TREK_APPROVED = 'TREK_APPROVED', _('Cung đường được duyệt')
        TREK_REJECTED = 'TREK_REJECTED', _('Cung đường bị từ chối')
        # Community
        POST_APPROVED = 'POST_APPROVED', _('Bài viết được duyệt')
        POST_REJECTED = 'POST_REJECTED', _('Bài viết bị từ chối')
        NEW_COMMENT = 'NEW_COMMENT', _('Bình luận mới')
        # Gamification
        BADGE_EARNED = 'BADGE_EARNED', _('Nhận huy hiệu mới')
        # System
        SYSTEM = 'SYSTEM', _('Thông báo hệ thống')

    nguoi_nhan = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='notifications',
        verbose_name=_('Người nhận')
    )
    loai = models.CharField(
        _('Loại'),
        max_length=20,
        choices=LoaiThongBao.choices,
        default=LoaiThongBao.SYSTEM
    )
    tieu_de = models.CharField(_('Tiêu đề'), max_length=200)
    noi_dung = models.TextField(_('Nội dung'), blank=True, default='')
    lien_ket = models.CharField(_('Liên kết'), max_length=500, blank=True, default='')
    da_doc = models.BooleanField(_('Đã đọc'), default=False)
    ngay_tao = models.DateTimeField(_('Ngày tạo'), auto_now_add=True)

    class Meta:
        ordering = ['-ngay_tao']
        verbose_name = _('Thông báo')
        verbose_name_plural = _('Thông báo')
        indexes = [
            models.Index(fields=['nguoi_nhan', '-ngay_tao']),
            models.Index(fields=['nguoi_nhan', 'da_doc']),
        ]

    def __str__(self):
        return f"[{self.loai}] {self.tieu_de} → {self.nguoi_nhan}"

    @property
    def icon(self):
        """Trả về icon FontAwesome tương ứng với loại thông báo"""
        icons = {
            'TRIP_APPROVED': 'fas fa-check-circle text-success',
            'TRIP_REJECTED': 'fas fa-times-circle text-danger',
            'MEMBER_JOINED': 'fas fa-user-plus text-primary',
            'MEMBER_APPROVED': 'fas fa-user-check text-success',
            'MEMBER_REJECTED': 'fas fa-user-times text-danger',
            'TREK_APPROVED': 'fas fa-mountain text-success',
            'TREK_REJECTED': 'fas fa-mountain text-danger',
            'POST_APPROVED': 'fas fa-newspaper text-success',
            'POST_REJECTED': 'fas fa-newspaper text-danger',
            'NEW_COMMENT': 'fas fa-comment text-info',
            'BADGE_EARNED': 'fas fa-award text-warning',
            'SYSTEM': 'fas fa-bell text-secondary',
        }
        return icons.get(self.loai, 'fas fa-bell')
