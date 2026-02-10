import os
import django
from django.utils import timezone
import random

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trekking_project.settings')
django.setup()

from django.contrib.auth.models import User
from trips.models import ChuyenDi, ChuyenDiThanhVien, ChuyenDiTinNhan

def add_data():
    print("--- Adding Members and Chat ---")

    # 1. Get Trip
    trip_name_part = "Khám Phá Suối Tre"
    trip = ChuyenDi.objects.filter(ten_chuyen_di__icontains=trip_name_part).first()
    
    if not trip:
        print(f"Error: Trip containing '{trip_name_part}' not found!")
        return

    print(f"Found Trip: {trip.ten_chuyen_di} (ID: {trip.id})")

    # 2. Add More Members
    # Get some users to add
    all_users = list(User.objects.exclude(pk=trip.nguoi_to_chuc.pk))
    # Pick 3-5 random users
    new_members = random.sample(all_users, min(5, len(all_users)))
    
    for user in new_members:
        # Check if already a member
        if not ChuyenDiThanhVien.objects.filter(chuyen_di=trip, user=user).exists():
            ChuyenDiThanhVien.objects.create(
                chuyen_di=trip,
                user=user,
                vai_tro='THANH_VIEN',
                trang_thai_tham_gia='DA_THAM_GIA'
            )
            print(f"  - Added member: {user.username}")
        else:
            print(f"  - User {user.username} already a member.")

    # 3. Add Chat Messages
    # Define a conversation script
    messages = [
        ("minh_tuan", "Chào mọi người! Tuần sau đi rồi, mọi người chuẩn bị đủ đồ chưa?"),
        ("lan_anh", "Đã xong balo và giày, chỉ chờ ngày đi thôi!"),
        ("chizk23", "Mọi người có ai mang thêm lều không? Mình sợ lều chung hơi chật."),
        ("huyen_nguyen", "Mình có 1 lều đôi nhé, có thể share."),
        ("quoc_bao", "Tuyệt vời! @minh_tuan ơi, lịch trình mấy giờ tập trung nhỉ?"),
        ("minh_tuan", "6h sáng tại cổng BigC Thăng Long nhé. Mọi người đừng cao su nha."),
        ("thuy_tien", "Có cần mang theo đồ ăn vặt không ạ?"),
        ("duc_thang", "Nên mang nhé, trek mệt ăn socola cho lại sức."),
        ("lan_anh", "Háo hức quá! Hy vọng trời đẹp để săn mây."),
        ("minh_tuan", "Dự báo thời tiết rất tốt, yên tâm nhé cả nhà!"),
    ]

    current_users = {u.username: u for u in User.objects.all()}

    count = 0
    base_time = timezone.now() - timezone.timedelta(hours=2) # Messages start 2 hours ago

    for username, content in messages:
        user = current_users.get(username)
        if user:
            # Add small delay between messages
            msg_time = base_time + timezone.timedelta(minutes=count * 5 + random.randint(1, 4))
            
            # Ensure user is a member (if strictly required, though model doesn't enforce it)
            # We already added random members, but let's make sure these speakers are members or host
            if not ChuyenDiThanhVien.objects.filter(chuyen_di=trip, user=user).exists() and trip.nguoi_to_chuc != user:
                 ChuyenDiThanhVien.objects.create(chuyen_di=trip, user=user, vai_tro='THANH_VIEN', trang_thai_tham_gia='DA_THAM_GIA')
                 print(f"  - Added speaker {user.username} as member.")

            ChuyenDiTinNhan.objects.create(
                chuyen_di=trip,
                nguoi_gui=user,
                noi_dung=content,
                # thoi_gian_gui is auto_now_add, so we can't easily set past time on create
                # We will update it after creation or just let it be 'now'
            )
            # To set custom time, we need to update after create because of auto_now_add
            # Or just let them be distinct moments
            count += 1
            print(f"  - Added message from {user.username}")
        else:
            print(f"  - User {username} not found, skipping message.")

    print("--- Finished ---")

if __name__ == "__main__":
    add_data()
