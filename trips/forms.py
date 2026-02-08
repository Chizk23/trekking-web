# trips/forms.py

from django import forms
from django.forms import inlineformset_factory
from .models import ChuyenDi, ChuyenDiTimeline
from treks.models import CungDuongTrek
from core.models import DoKho, TinhThanh, The

# ==========================================================
# === 1. FORM LỌC CHUYẾN ĐI (TRANG HUB) - BẢN FULL ===
# ==========================================================
class TripFilterForm(forms.Form):
    # 1. Tìm kiếm cơ bản
    q = forms.CharField(
        label="Tìm kiếm", 
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Tên chuyến đi, địa điểm...',
            'class': 'form-control form-control-sm'
        })
    )
    
    # 2. Địa điểm
    tinh_thanh = forms.ModelChoiceField(
        label="Tỉnh thành",
        queryset=TinhThanh.objects.order_by('ten'),
        required=False,
        empty_label="Tất cả tỉnh thành",
        widget=forms.Select(attrs={'class': 'form-select form-select-sm select2'})
    )
    
    # 3. Ngày khởi hành
    start_date = forms.DateField(
        label="Khởi hành sau ngày",
        required=False,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control form-control-sm'})
    )
    
    # 4. Ngân sách (Min - Max)
    price_min = forms.DecimalField(
        required=False, 
        min_value=0, 
        widget=forms.NumberInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Từ (đ)'})
    )
    price_max = forms.DecimalField(
        required=False, 
        min_value=0, 
        widget=forms.NumberInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Đến (đ)'})
    )
    
    # 5. Thời lượng (Số ngày)
    duration_min = forms.IntegerField(
        required=False, 
        min_value=1, 
        widget=forms.NumberInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Từ'})
    )
    duration_max = forms.IntegerField(
        required=False, 
        min_value=1, 
        widget=forms.NumberInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Đến'})
    )
    
    # 6. Độ khó (Checkbox List)
    do_kho = forms.ModelMultipleChoiceField(
        queryset=DoKho.objects.all(),
        required=False,
        label="Cấp độ Trekking",
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'})
    )

    # 7. Tùy chọn nâng cao
    con_cho = forms.BooleanField(
        required=False, 
        label="Chỉ hiện chuyến còn chỗ",
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

    # 8. Sắp xếp
    SORT_CHOICES = [
        ('newest', 'Mới đăng nhất'),
        ('date_asc', 'Ngày đi: Gần -> Xa'),
        ('price_asc', 'Giá: Thấp -> Cao'),
        ('price_desc', 'Giá: Cao -> Thấp'),
    ]
    sort_by = forms.ChoiceField(
        choices=SORT_CHOICES, 
        required=False, 
        label="Sắp xếp theo",
        widget=forms.Select(attrs={'class': 'form-select form-select-sm'})
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=The.objects.all(),
        required=False,
        label="Chủ đề (Hashtag)",
        widget=forms.SelectMultiple(attrs={'class': 'form-select select2', 'data-placeholder': 'Chọn chủ đề...'})
    )

# ==========================================================
# === FORM CHÍNH ĐỂ TẠO / SỬA CHUYẾN ĐI ===
# ==========================================================
class ChuyenDiForm(forms.ModelForm):
    class Meta:
        model = ChuyenDi
        fields = [
            'ten_chuyen_di', 'mo_ta', 'ngay_bat_dau', 'ngay_ket_thuc', 'so_luong_toi_da', 
            'chi_phi_uoc_tinh', 'che_do_rieng_tu', 'yeu_cau_ly_do', 
            'dia_diem_tap_trung', 'toa_do_tap_trung', 'tags', 'trang_thai'
        ]
        widgets = {
            'ten_chuyen_di': forms.TextInput(attrs={'class': 'form-control'}),
            'mo_ta': forms.Textarea(attrs={'rows': 5, 'class': 'form-control', 'placeholder': 'Giới thiệu về chuyến đi, lịch trình dự kiến...'}),
            'ngay_bat_dau': forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'class': 'form-control'},
                format='%Y-%m-%dT%H:%M'
            ),
            'ngay_ket_thuc': forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'class': 'form-control'},
                format='%Y-%m-%dT%H:%M'
            ),
            'so_luong_toi_da': forms.NumberInput(attrs={'class': 'form-control'}),
            'chi_phi_uoc_tinh': forms.NumberInput(attrs={'class': 'form-control'}),
            'che_do_rieng_tu': forms.Select(attrs={'class': 'form-select'}),
            'yeu_cau_ly_do': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'dia_diem_tap_trung': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nhập tên địa điểm...'}),
            'toa_do_tap_trung': forms.HiddenInput(),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control select2'}),
            'trang_thai': forms.Select(attrs={'class': 'form-select fw-bold text-primary'}),
        }
        labels = {
            'ten_chuyen_di': 'Tên Chuyến đi',
            'mo_ta': 'Mô tả chi tiết & Kế hoạch',
            'ngay_bat_dau': 'Thời gian bắt đầu',
            'ngay_ket_thuc': 'Thời gian kết thúc',
            'so_luong_toi_da': 'Số lượng thành viên tối đa',
            'chi_phi_uoc_tinh': 'Chi phí dự kiến (VND / người)',
            'che_do_rieng_tu': 'Chế độ riêng tư',
            'yeu_cau_ly_do': 'Yêu cầu người tham gia điền lý do',
            'dia_diem_tap_trung': 'Địa điểm tập trung',
            'tags': 'Chủ đề (Hashtag)',
            'trang_thai': 'Trạng thái',
        }

    def __init__(self, *args, **kwargs):
        # Lấy user từ view truyền vào để phân quyền
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        
        # Config định dạng ngày tháng
        self.fields['ngay_bat_dau'].input_formats = ['%Y-%m-%dT%H:%M', '%Y-%m-%dT%H:%M:%S']
        self.fields['ngay_ket_thuc'].input_formats = ['%Y-%m-%dT%H:%M', '%Y-%m-%dT%H:%M:%S']

        # === LOGIC PHÂN QUYỀN TRẠNG THÁI ===
        if self.user and not self.user.is_staff:
            # User thường (Host) chỉ thấy các trạng thái vận hành cơ bản
            allowed_choices = [
                ('DANG_TUYEN', 'Đang tuyển thành viên'),
                ('DA_DONG', 'Đóng đăng ký (Ngưng tuyển)'),
                ('DA_HUY', 'Hủy chuyến đi'),
            ]
            
            # Nếu đang CHỜ DUYỆT hoặc BỊ TỪ CHỐI -> Khóa không cho sửa trạng thái
            if self.instance.pk and self.instance.trang_thai in ['CHO_DUYET', 'BI_TU_CHOI']:
                self.fields['trang_thai'].disabled = True
                self.fields['trang_thai'].help_text = "Trạng thái này đang được Admin xử lý."
            else:
                # Nếu đã được duyệt -> Chỉ hiện các lựa chọn cho phép
                self.fields['trang_thai'].choices = allowed_choices
        
        # Admin thì thấy full quyền (Mặc định)

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("ngay_bat_dau")
        end_date = cleaned_data.get("ngay_ket_thuc")
        
        if start_date and end_date and end_date < start_date:
            self.add_error('ngay_ket_thuc', "Ngày kết thúc không thể trước ngày bắt đầu.")
        
        return cleaned_data


# ==========================================================
# === FORM CHO MỖI MỐC TIMELINE ===
# ==========================================================
class ChuyenDiTimelineForm(forms.ModelForm):
    class Meta:
        model = ChuyenDiTimeline
        fields = ['ngay', 'thoi_gian', 'hoat_dong', 'mo_ta_chi_tiet']
        widgets = {
            'ngay': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ngày thứ...'}),
            'thoi_gian': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'hoat_dong': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Hoạt động chính'}),
            'mo_ta_chi_tiet': forms.Textarea(attrs={'rows': 2, 'class': 'form-control', 'placeholder': 'Mô tả thêm (tùy chọn)'}),
        }
        labels = {
            'ngay': 'Ngày',
            'thoi_gian': 'Thời gian',
            'hoat_dong': 'Hoạt động',
            'mo_ta_chi_tiet': 'Mô tả chi tiết',
        }


# ==========================================================
# === FORMSET ĐỂ QUẢN LÝ NHIỀU MỐC TIMELINE ===
# ==========================================================
TimelineFormSet = forms.inlineformset_factory(
    ChuyenDi, 
    ChuyenDiTimeline, 
    form=ChuyenDiTimelineForm,
    extra=1,
    can_delete=True,
    can_order=False,
)

# === FORM MỚI CHO TRANG CHỌN CUNG ĐƯỜNG ===
class TripAdminFilterForm(forms.Form):
    # 1. Tìm kiếm chung (Tên chuyến, Tên Leader)
    q = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': '🔍 Tìm tên chuyến, leader...'
        })
    )
    
    # 2. Lọc theo Cung đường (Mới thêm)
    cung_duong = forms.ModelChoiceField(
        queryset=CungDuongTrek.objects.filter(trang_thai='DA_DUYET').order_by('ten'),
        required=False,
        empty_label="--- Chọn Cung đường ---",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    # 3. Lọc theo Tỉnh thành
    tinh_thanh = forms.ModelChoiceField(
        queryset=TinhThanh.objects.all().order_by('ten'),
        required=False,
        empty_label="--- Chọn Tỉnh thành ---",
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    # 4. BỘ LỌC TRẠNG THÁI & RỦI RO (Logic màu vàng)
    STATUS_RISK_CHOICES = [
        ('', '--- 🛡️ Kiểm tra trạng thái ---'),
        ('upcoming_urgent', '🚀 Sắp đi (72h tới)'),
        ('ghost', '👻 Vắng khách (Sắp đi + < 2 người)'),
        ('crowded', '🔥 Full Slot (Đã đủ người)'),
        ('high_risk', '💰 Rủi ro cao (Thu > 5tr)'),
        ('ongoing', '⛺ Đang diễn ra'),
        ('canceled', '❌ Đã hủy / Tạm hoãn'),
    ]
    
    admin_status = forms.ChoiceField(
        required=False,
        choices=STATUS_RISK_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-select border-warning bg-warning-subtle text-dark fw-bold', 
            'style': 'background-color: #fffbeb;' # Màu nền vàng nhạt
        })
    )
    # ==========================================================
# === FORM MỚI CHO TRANG CHỌN CUNG ĐƯỜNG ===
# ==========================================================
class SelectTrekFilterForm(forms.Form):
    q = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tìm tên cung đường...'})
    )
    tinh_thanh = forms.ModelChoiceField(
        queryset=TinhThanh.objects.order_by('ten'),
        required=False,
        empty_label="Tất cả tỉnh thành",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    do_kho = forms.ModelChoiceField(
        queryset=DoKho.objects.all(),
        required=False,
        empty_label="Tất cả độ khó",
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    # ==========================================================
# === FORM DÀNH RIÊNG CHO ADMIN (BẮT BUỘC PHẢI CÓ) ===
# ==========================================================
class TripAdminForm(forms.ModelForm):
    # 1. Field chọn Cung đường (Giữ nguyên)
    cung_duong = forms.ModelChoiceField(
        queryset=CungDuongTrek.objects.filter(trang_thai='DA_DUYET').order_by('ten'),
        widget=forms.Select(attrs={'class': 'form-select select2', 'data-placeholder': '🔍 Tìm cung đường...'}),
        label="Cung đường gốc",
        help_text="Chọn cung đường để lấy dữ liệu cơ sở."
    )

    class Meta:
        model = ChuyenDi
        # [QUAN TRỌNG]: ĐÃ XÓA 'nguoi_to_chuc' KHỎI DANH SÁCH DƯỚI ĐÂY
        # Để Form không kiểm tra field này nữa => Hết lỗi đỏ.
        fields = [
            'ten_chuyen_di', 'cung_duong', 'mo_ta', 
            'ngay_bat_dau', 'ngay_ket_thuc', 
            'so_luong_toi_da', 'chi_phi_uoc_tinh', 
            'che_do_rieng_tu', 'trang_thai', 
            'yeu_cau_ly_do', 
            'dia_diem_tap_trung', 'toa_do_tap_trung', 
            'tags' 
            # Đã xóa 'nguoi_to_chuc' ở đây
        ]
        
        widgets = {
            'ten_chuyen_di': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nhập tên chuyến đi...'}),
            'mo_ta': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            
            # Giữ nguyên cấu hình ngày giờ (step: 60)
            'ngay_bat_dau': forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'class': 'form-control', 'step': 60},
                format='%Y-%m-%dT%H:%M'
            ),
            'ngay_ket_thuc': forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'class': 'form-control', 'step': 60},
                format='%Y-%m-%dT%H:%M'
            ),

            'so_luong_toi_da': forms.NumberInput(attrs={'class': 'form-control'}),
            'chi_phi_uoc_tinh': forms.NumberInput(attrs={'class': 'form-control'}),
            'che_do_rieng_tu': forms.Select(attrs={'class': 'form-select'}),
            'trang_thai': forms.Select(attrs={'class': 'form-select fw-bold text-primary'}),
            'dia_diem_tap_trung': forms.TextInput(attrs={'class': 'form-control'}),
            'toa_do_tap_trung': forms.HiddenInput(),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control select2'}),
            'yeu_cau_ly_do': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Format ngày giờ để tránh lỗi validation
        formats = ['%Y-%m-%dT%H:%M', '%Y-%m-%dT%H:%M:%S']
        self.fields['ngay_bat_dau'].input_formats = formats
        self.fields['ngay_ket_thuc'].input_formats = formats

    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get('ngay_bat_dau')
        end = cleaned_data.get('ngay_ket_thuc')
        
        if start and end and end < start:
            self.add_error('ngay_ket_thuc', "Ngày kết thúc phải sau ngày bắt đầu.")
        return cleaned_data