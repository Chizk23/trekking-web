# treks/forms.py (PHIÊN BẢN TỐI GIẢN & CHUẨN XÁC)

from django import forms
from .models import CungDuongTrek, CungDuongDanhGia, CungDuongVatDungGoiY, TrangThaiDuyet
from core.models import TinhThanh, DoKho, VatDung
from tinymce.widgets import TinyMCE
from django import forms
from core.models import TinhThanh, DoKho

class CungDuongTrekAdminForm(forms.ModelForm):
    """
    Form dùng riêng cho trang Admin để tạo và cập nhật CungDuongTrek,
    bao gồm cả việc quản lý các Vật dụng gợi ý.
    """
    vat_dung_goi_y = forms.ModelMultipleChoiceField(
        # =======================================================
        # === ĐÂY LÀ DÒNG ĐÃ ĐƯỢC SỬA LỖI ======================
        # =======================================================
        queryset=VatDung.objects.all().order_by('loai_vat_dung__ten', 'ten'),
        
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Vat dụng gợi ý"
    )

    class Meta:
        model = CungDuongTrek
        # Liệt kê tất cả các trường sẽ hiển thị trên form.
        # 'trang_thai' được bỏ qua vì sẽ được xử lý tự động trong view.
        fields = [
            'ten', 'mo_ta', 'dia_diem_chi_tiet', 'tinh_thanh', 'do_dai_km', 
            'thoi_gian_uoc_tinh_gio', 'tong_do_cao_leo_m', 'do_kho', 
            'mua_dep_nhat', 'du_lieu_ban_do_geojson', 'vat_dung_goi_y', 'trang_thai'
        ]
        # Tùy chỉnh các widget để thêm class CSS và ID cho JavaScript.
        widgets = {
            'ten': forms.TextInput(attrs={'class': 'form-control'}),
            'mo_ta': TinyMCE(attrs={'cols': 80, 'rows': 20}),
            'dia_diem_chi_tiet': forms.TextInput(attrs={
                'class': 'form-control', 
                'id': 'id_dia_diem_chi_tiet', # ID cho ô nhập địa điểm
                'placeholder': 'VD: Vườn quốc gia Ba Vì, Hà Nội',
                'autocomplete': 'off' # Tắt tự động điền của trình duyệt
            }),
            
            'tinh_thanh': forms.Select(attrs={'class': 'form-control'}),
            'do_dai_km': forms.NumberInput(attrs={'class': 'form-control'}),
            'thoi_gian_uoc_tinh_gio': forms.NumberInput(attrs={'class': 'form-control'}),
            'tong_do_cao_leo_m': forms.NumberInput(attrs={'class': 'form-control'}),
            'do_kho': forms.Select(attrs={'class': 'form-control'}),
            'mua_dep_nhat': forms.TextInput(attrs={'class': 'form-control'}),
            'trang_thai': forms.Select(attrs={'class': 'form-select'}),
                       
            # DÒNG QUAN TRỌNG: Thêm ID cho trường ẩn này
            'du_lieu_ban_do_geojson': forms.Textarea(attrs={
                'style': 'display: none;', 
                'id': 'id_du_lieu_ban_do_geojson' 
            }),
        }

    def __init__(self, *args, **kwargs):
        """
        Ghi đè __init__ để gán giá trị ban đầu cho trường vật dụng khi chỉnh sửa.
        """
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['vat_dung_goi_y'].initial = self.instance.vat_dung_goi_y.all().values_list('vat_dung__pk', flat=True)

    def save(self, commit=True):
        """
        Ghi đè phương thức save để xử lý việc lưu quan hệ many-to-many 
        thông qua model trung gian CungDuongVatDungGoiY.
        """
        instance = super().save(commit=False)
        
        if commit:
            instance.save()
            instance.vat_dung_goi_y.all().delete()
            for vat_dung in self.cleaned_data['vat_dung_goi_y']:
                CungDuongVatDungGoiY.objects.create(cung_duong=instance, vat_dung=vat_dung)
        return instance


# ==============================================================================
# FORM USER: CHO NGƯỜI DÙNG ĐÓNG GÓP CUNG ĐƯỜNG
# ==============================================================================
class CungDuongUserContributionForm(forms.ModelForm):
    """
    Form cho người dùng đóng góp cung đường mới.
    Không có trường trạng thái (mặc định CHO_DUYET).
    """
    vat_dung_goi_y = forms.ModelMultipleChoiceField(
        queryset=VatDung.objects.all().order_by('loai_vat_dung__ten', 'ten'),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Vật dụng gợi ý"
    )

    class Meta:
        model = CungDuongTrek
        # KHÔNG có trường 'trang_thai' - mặc định sẽ là CHO_DUYET
        fields = [
            'ten', 'mo_ta', 'dia_diem_chi_tiet', 'tinh_thanh', 'do_dai_km', 
            'thoi_gian_uoc_tinh_gio', 'tong_do_cao_leo_m', 'do_kho', 
            'mua_dep_nhat', 'du_lieu_ban_do_geojson', 'vat_dung_goi_y'
        ]
        widgets = {
            'ten': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'VD: Tà Năng - Phan Dũng'}),
            'mo_ta': TinyMCE(attrs={'cols': 80, 'rows': 20}),
            'dia_diem_chi_tiet': forms.TextInput(attrs={
                'class': 'form-control', 
                'id': 'id_dia_diem_chi_tiet',
                'placeholder': 'VD: Vườn quốc gia Ba Vì, Hà Nội',
                'autocomplete': 'off'
            }),
            'tinh_thanh': forms.Select(attrs={'class': 'form-select'}),
            'do_dai_km': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'VD: 55'}),
            'thoi_gian_uoc_tinh_gio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'VD: 12'}),
            'tong_do_cao_leo_m': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'VD: 1500'}),
            'do_kho': forms.Select(attrs={'class': 'form-select'}),
            'mua_dep_nhat': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'VD: Tháng 11 - Tháng 4'}),
            'du_lieu_ban_do_geojson': forms.Textarea(attrs={
                'style': 'display: none;', 
                'id': 'id_du_lieu_ban_do_geojson' 
            }),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['vat_dung_goi_y'].initial = self.instance.vat_dung_goi_y.all().values_list('vat_dung__pk', flat=True)

    def save(self, commit=True):
        instance = super().save(commit=False)
        # Gán người tạo nếu là tạo mới
        if not instance.pk and self.user:
            instance.nguoi_tao = self.user
        # Mặc định trạng thái là CHỜ DUYỆT
        if not instance.pk:
            instance.trang_thai = TrangThaiDuyet.CHO_DUYET
        
        if commit:
            instance.save()
            # Xóa và tạo lại quan hệ vật dụng gợi ý
            instance.vat_dung_goi_y.all().delete()
            for vat_dung in self.cleaned_data.get('vat_dung_goi_y', []):
                CungDuongVatDungGoiY.objects.create(cung_duong=instance, vat_dung=vat_dung)
            
        return instance
# treks/forms.py

# ==============================================================================
# 2. FORM ADMIN: BỘ LỌC THÔNG MINH (ĐÃ SỬA LỖI THIẾU TRƯỜNG)
# ==============================================================================
class CungDuongTrekFilterForm(forms.Form):
    # --- ĐỊNH NGHĨA CÁC LỰA CHỌN ---
    CHOICES_TRANG_THAI = [('', '--- Tất cả trạng thái ---')] + TrangThaiDuyet.choices
    
    CHOICES_LOC_NHANH = [
        ('', '--- Lọc nhanh vấn đề ---'),
        ('missing_map', '⚠️ Thiếu bản đồ (GeoJSON)'),
        ('missing_image', '📷 Thiếu ảnh bìa/Media'),
        ('low_rating', '⭐ Đánh giá thấp (< 3 sao)'),
        ('no_reviews', '💬 Chưa có đánh giá'),
        ('outdated', '⏰ Cũ (Chưa cập nhật > 6 tháng)'),
    ]

    CHOICES_SORT = [
        ('newest', 'Mới nhất'),
        ('oldest', 'Cũ nhất'),
        ('rating_desc', 'Điểm đánh giá (Cao -> Thấp)'),
        ('rating_asc', 'Điểm đánh giá (Thấp -> Cao)'),
        ('review_desc', 'Nhiều đánh giá nhất'),
    ]

    CHOICES_AUTHOR = [
        ('', '--- Tất cả người đăng ---'),
        ('admin', '🛡️ Admin (Ban quản trị)'),
        ('user', '👤 User (Cộng đồng)'),
    ]
    # === THÊM NHÓM LỌC CHỈ SỐ (MỚI) ===
    # 1. Độ dài (km)
    min_len = forms.DecimalField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Km (Min)'}))
    max_len = forms.DecimalField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Km (Max)'}))

    # 2. Thời gian (giờ)
    min_time = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Giờ (Min)'}))
    max_time = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Giờ (Max)'}))

    # 3. Độ cao (m)
    min_high = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Mét (Min)'}))
    max_high = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Mét (Max)'}))
    # --- CÁC TRƯỜNG TÌM KIẾM ---
    q = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Tìm tên cung đường, địa điểm...'
        })
    )
    
    tinh_thanh = forms.ModelChoiceField(
        queryset=TinhThanh.objects.all().order_by('ten'),
        required=False,
        empty_label="--- Tất cả Tỉnh/Thành ---",
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    do_kho = forms.ModelChoiceField(
        queryset=DoKho.objects.all(),
        required=False,
        empty_label="--- Tất cả Độ khó ---",
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    trang_thai = forms.ChoiceField(
        required=False,
        choices=CHOICES_TRANG_THAI,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    # --- TRƯỜNG KIỂM SOÁT CHẤT LƯỢNG ---
    bo_loc_nhanh = forms.ChoiceField(
        required=False,
        choices=CHOICES_LOC_NHANH,
        widget=forms.Select(attrs={
            'class': 'form-select border-warning', 
            'style': 'background-color: #fff3cd;'
        })
    )

    # --- HAI TRƯỜNG QUAN TRỌNG VỪA THÊM (LÚC NÃY BẠN THIẾU) ---
    sort_by = forms.ChoiceField(
        required=False,
        choices=CHOICES_SORT,
        label="Sắp xếp",
        widget=forms.Select(attrs={'class': 'form-select fw-bold'})
    )

    author_type = forms.ChoiceField(
        required=False,
        choices=CHOICES_AUTHOR,
        label="Người đăng",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
# Form 2: Dùng cho người dùng lọc cung đường (KHÔNG THAY ĐỔI)
# treks/forms.py

class CungDuongFilterForm(forms.Form):
    q = forms.CharField(
        label='Tìm theo tên',
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'VD: Tà Năng - Phan Dũng...'})
    )
    tinh_thanh = forms.ModelChoiceField(
        label='Tỉnh/Thành phố',
        queryset=TinhThanh.objects.order_by('ten'),
        required=False,
        empty_label="Tất cả tỉnh thành"
    )
    do_kho = forms.ModelChoiceField(
        label='Độ khó',
        queryset=DoKho.objects.all(),
        required=False,
        empty_label="Tất cả độ khó"
    )
    
    min_do_dai = forms.DecimalField(
        label='Độ dài (km)',
        required=False,
        widget=forms.NumberInput(attrs={'placeholder': 'Từ', 'step': '0.1', 'min': '0'})
    )
    max_do_dai = forms.DecimalField(
        required=False,
        widget=forms.NumberInput(attrs={'placeholder': 'Đến', 'step': '0.1', 'min': '0'})
    )

    min_danh_gia = forms.DecimalField(
        label='Đánh giá tối thiểu',
        required=False,
        max_digits=2, decimal_places=1,
        widget=forms.NumberInput(attrs={'placeholder': 'Từ 1.0 đến 5.0', 'step': '0.1', 'min': '1', 'max': '5'})
    )
    min_do_cao = forms.IntegerField(
        label='Tổng độ cao leo (m)',
        required=False,
        widget=forms.NumberInput(attrs={'placeholder': 'Tối thiểu (m)', 'min': '0'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Gán class chung cho các widget để dễ style bằng CSS
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'trek-form-control'})

# Form 3: Dùng cho người dùng gửi đánh giá (CHỈ GIỮ LẠI CÁC TRƯỜNG CẦN VALIDATE)
class CungDuongDanhGiaForm(forms.ModelForm):
    # Sử dụng ChoiceField với widget RadioSelect để người dùng dễ chọn sao
    diem_danh_gia = forms.ChoiceField(
        label="Chấm điểm của bạn",
        choices=[(i, f"{i} sao") for i in range(5, 0, -1)],
        widget=forms.RadioSelect,
        required=True
    )
    
    binh_luan = forms.CharField(
        label="Bình luận của bạn",
        widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'Chia sẻ cảm nhận của bạn...'}),
        required=False
    )

    # --- ĐÃ XÓA TRƯỜNG `hinh_anh` KHỎI ĐÂY ---

    class Meta:
        model = CungDuongDanhGia
        fields = ['diem_danh_gia', 'binh_luan']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if not isinstance(self.fields[field].widget, forms.RadioSelect): 
                self.fields[field].widget.attrs.update({'class': 'form-control'})
class CungDuongMapForm(forms.ModelForm):
    """Một form siêu đơn giản chỉ để cập nhật dữ liệu bản đồ."""
    class Meta:
        model = CungDuongTrek
        fields = ['du_lieu_ban_do_geojson']
        widgets = {
            'du_lieu_ban_do_geojson': forms.Textarea(attrs={
                'id': 'id_du_lieu_ban_do_geojson', # ID quan trọng cho JS
                'style': 'display: none;'
            }),
        }
# XÓA BỎ CÁC FORM UPLOAD (MediaUploadForm, ReviewImageUploadForm)