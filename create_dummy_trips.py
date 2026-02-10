import os
import django
from datetime import timedelta
from django.utils import timezone
import random

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trekking_project.settings')
django.setup()

from django.contrib.auth.models import User
from django.utils.text import slugify
from treks.models import CungDuongTrek
from trips.models import ChuyenDi, ChuyenDiThanhVien, ChuyenDiTimeline
from core.models import The

def create_trips():
    print("--- Starting Trip Generation ---")

    # 1. Base Data
    users = {u.username: u for u in User.objects.all()}
    treks = {t.ten: t for t in CungDuongTrek.objects.all()}
    
    if not users or not treks:
        print("Error: Not enough users or treks found!")
        return

    # Helper to get user safely
    def get_user(username):
        return users.get(username) or User.objects.first()

    # Helper to get trek safely (fuzzy match or first)
    def get_trek(name_part):
        for name, trek in treks.items():
            if name_part in name:
                return trek
        return CungDuongTrek.objects.first()

    # 2. Define Trips
    trip_data_list = [
        {
            "name": "Leo Tả Liên Sơn - Mùa Rêu Cổ Tích",
            "trek_name": "Tả Liên Sơn",
            "host": "minh_tuan",
            "max": 12,
            "cost": 2500000,
            "start_days_offset": 5, # Starts in 5 days
            "duration": 2,
            "desc": "Chuyến đi khám phá khu rừng nguyên sinh đẹp nhất Tây Bắc với thảm thực vật phong phú và những cây cổ thụ phủ đầy rêu phong. Chúng ta sẽ cùng nhau săn mây trên đỉnh Tả Liên.",
            "members": [
                ("lan_anh", "THANH_VIEN", "DA_THAM_GIA"),
                ("quoc_bao", "THANH_VIEN", "DA_THAM_GIA"),
                ("thuy_tien", "THANH_VIEN", "DA_GUI_YEU_CAU"), # Pending
                ("duc_thang", "THANH_VIEN", "DA_GUI_YEU_CAU"), # Pending
            ],
            "tags": ["Rừng Nguyên Sinh", "Săn Mây", "Mùa Thu"],
             "schedule": [
                (1, "06:00", "Tập trung tại Mỹ Đình", "Di chuyển lên Sapa -> Tả Lèng."),
                (1, "12:00", "Ăn trưa tại Tả Lèng", "Chuẩn bị đồ đạc cá nhân."),
                (1, "13:30", "Bắt đầu leo", "Trekking qua rừng thảo quả, rừng trúc."),
                (1, "17:00", "Hạ trại ở lán nghỉ 2400m", "Nấu ăn tối, giao lưu văn nghệ."),
                (2, "04:30", "Dậy sớm, ăn sáng", "Trek lên đỉnh đón bình minh."),
                (2, "06:30", "Check-in đỉnh Tả Liên Sơn", "Chụp ảnh, ngắm biển mây."),
                (2, "08:00", "Xuống núi", "Về lại lán thu dọn đồ."),
                (2, "13:00", "Về đến bản Tả Lèng", "Ăn trưa, xe đón về Hà Nội."),
            ]
        },
        {
            "name": "Chinh Phục Fansipan - Cung Đường Trạm Tôn",
            "trek_name": "Fansipan",
            "host": "lan_anh",
            "max": 15,
            "cost": 3200000,
            "start_days_offset": 14,
            "duration": 2,
            "desc": "Hành trình chinh phục nóc nhà Đông Dương 3143m. Cung đường Trạm Tôn vừa sức, cảnh đẹp hùng vĩ.",
            "members": [
                ("chizk23", "THANH_VIEN", "DA_THAM_GIA"),
                ("huyen_nguyen", "THANH_VIEN", "DA_THAM_GIA"),
                ("quoc_bao", "THANH_VIEN", "DA_THAM_GIA"),
                ("thuy_tien", "THANH_VIEN", "DA_THAM_GIA"),
                ("duc_thang", "THANH_VIEN", "DA_THAM_GIA"),
                ("hoang_nam", "THANH_VIEN", "DA_THAM_GIA"),
                ("phuong_thao", "THANH_VIEN", "DA_THAM_GIA"),
                ("anh_khoa", "THANH_VIEN", "DA_GUI_YEU_CAU"),
            ],
            "tags": ["Leo Núi", "Thử Thách", "Sapa", "Top 1"],
            "schedule": [
                (1, "22:00", "Lên xe giường nằm", "Tại bến xe Mỹ Đình."),
                (2, "05:00", "Đến Sapa", "Vệ sinh cá nhân, ăn sáng."),
                (2, "08:00", "Có mặt tại Trạm Tôn", "Làm thủ tục với kiểm lâm."),
                (2, "12:00", "Nghỉ ăn trưa tại lán 2200m", "Đồ ăn nhẹ mang theo."),
                (2, "17:00", "Đến điểm nghỉ 2800m", "Hạ trại, ăn tối lẩu gà."),
                (3, "03:30", "Dậy sớm trekking lên đỉnh", "Đón bình minh trên đỉnh Fansipan."),
                (3, "06:00", "Chạm tay vào chóp inox", "Niềm tự hào chiến thắng bản thân."),
                (3, "08:00", "Quay về theo đường cũ", "Hoặc đi cáp treo (tự túc)."),
            ]
        }
    ]

    # 3. Process Loops
    for data in trip_data_list:
        trek = get_trek(data['trek_name'])
        host = get_user(data['host'])
        
        start_date = timezone.now() + timedelta(days=data['start_days_offset'])
        end_date = start_date + timedelta(days=data['duration'])
        
        # A. Create Trip
        print(f"Creating Trip: {data['name']} (Host: {host.username})")
        trip = ChuyenDi.objects.create(
            ten_chuyen_di=data['name'],
            cung_duong=trek,
            nguoi_to_chuc=host,
            ngay_bat_dau=start_date,
            ngay_ket_thuc=end_date,
            so_luong_toi_da=data['max'],
            trang_thai='DANG_TUYEN', # Open for joining
            che_do_rieng_tu='CONG_KHAI',
            chi_phi_uoc_tinh=data['cost'],
            dia_diem_tap_trung="Hà Nội",
            mo_ta=data['desc'],
            # Inherit basic info from trek if needed, but model handles some snapshots
            cd_ten=trek.ten,
            cd_mo_ta=trek.mo_ta[:200] if trek.mo_ta else "",
            cd_tinh_thanh_ten=trek.tinh_thanh.ten if trek.tinh_thanh else "",
            cd_do_kho_ten=trek.do_kho.ten if trek.do_kho else "",
            cd_do_dai_km=trek.do_dai_km,
        )

        # B. Add Host as LEADER
        ChuyenDiThanhVien.objects.create(
            chuyen_di=trip,
            user=host,
            vai_tro='TRUONG_DOAN',
            trang_thai_tham_gia='DA_THAM_GIA' # Host always joins
        )
        
        # C. Add Members
        for mem_username, role, status in data['members']:
            mem_user = get_user(mem_username)
            if mem_user and mem_user != host:
                ChuyenDiThanhVien.objects.create(
                    chuyen_di=trip,
                    user=mem_user,
                    vai_tro=role, # Mostly THANH_VIEN
                    trang_thai_tham_gia=status
                )
                print(f"  - Added {mem_username} ({status})")
        
        # D. Add Tags
        for tag_name in data['tags']:
            # Create tag if not exists
            slug = slugify(tag_name)
            tag_obj, created = The.objects.get_or_create(
                slug=slug, 
                defaults={'ten': tag_name}
            )
            trip.tags.add(tag_obj)
        print(f"  - Added {len(data['tags'])} tags.")

        # E. Add Timeline
        for day, time_str, activity, detail in data['schedule']:
             ChuyenDiTimeline.objects.create(
                chuyen_di=trip,
                ngay=day,
                thoi_gian=time_str, # String "HH:MM" works for TimeField in some DBs or needs parsing? 
                                    # Django TimeField usually takes string "HH:MM" or datetime.time object.
                                    # Let's try string first.
                hoat_dong=activity,
                mo_ta_chi_tiet=detail,
                thu_tu=day*10 # simple ordering
            )
        print(f"  - Added timeline.")

    print("--- Finished ---")

if __name__ == "__main__":
    create_trips()
