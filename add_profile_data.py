import os
import django
from django.utils.text import slugify

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trekking_project.settings')
django.setup()

from django.contrib.auth.models import User
from core.models import VatDung, LoaiVatDung, The
from accounts.models import TaiKhoanThietBiCaNhan, TaiKhoanSoThichNguoiDung

def create_profile_data():
    print("--- Starting Profile Data Generation ---")
    
    # 1. Get User
    username = 'huyen_nguyen'
    try:
        user = User.objects.get(username=username)
        print(f"Found user: {user.username}")
    except User.DoesNotExist:
        print(f"User {username} not found! Creating...")
        user = User.objects.create_user(username=username, password='123')
        print(f"Created user: {user.username}")

    # 2. Add Interests (Tags)
    interests_list = ['Leo núi', 'Cắm trại', 'Chụp ảnh', 'Săn mây', 'Khám phá thiên nhiên', 'Bơi lội']
    print(f"Adding interests for {username}...")
    
    # Delete existing to avoid duplicates if re-run
    TaiKhoanSoThichNguoiDung.objects.filter(user=user).delete()
    
    for tag_name in interests_list:
        tag, created = The.objects.get_or_create(
            ten=tag_name, 
            defaults={'slug': slugify(tag_name)}
        )
        TaiKhoanSoThichNguoiDung.objects.create(user=user, the=tag)
        print(f"  - Added interest: {tag_name}")

    # 3. Add Equipment
    print(f"Adding equipment for {username}...")
    
    # Helper to get category
    def get_cat(name):
        cat, _ = LoaiVatDung.objects.get_or_create(ten=name)
        return cat

    cat_camping = get_cat('Dụng cụ cắm trại')
    cat_clothing = get_cat('Trang phục')
    cat_tech = get_cat('Thiết bị điện tử')

    # Equipment items to add
    equipment_data = [
        {'name': 'Lều 4 người Naturehike', 'cat': cat_camping, 'qty': 1, 'note': 'Màu xanh, chống nước tốt'},
        {'name': 'Túi ngủ đông', 'cat': cat_camping, 'qty': 2, 'note': 'Chịu nhiệt -5 độ'},
        {'name': 'Đèn pin đội đầu', 'cat': cat_tech, 'qty': 1, 'note': 'Siêu sáng'},
        {'name': 'Giày trekking chống thấm', 'cat': cat_clothing, 'qty': 1, 'note': 'Size 39'},
        {'name': 'Gậy leo núi', 'cat': cat_camping, 'qty': 2, 'note': 'Carbon siêu nhẹ'},
    ]

    # Delete existing equipment to avoid duplicates
    TaiKhoanThietBiCaNhan.objects.filter(user=user).delete()

    for item in equipment_data:
        vat_dung, created = VatDung.objects.get_or_create(
            ten=item['name'],
            defaults={'loai_vat_dung': item['cat']}
        )
        
        TaiKhoanThietBiCaNhan.objects.create(
            user=user,
            vat_dung=vat_dung,
            so_luong=item['qty'],
            ghi_chu=item['note']
        )
        print(f"  - Added equipment: {item['name']} (x{item['qty']})")

    print("--- Finished Profile Data Generation ---")

if __name__ == '__main__':
    create_profile_data()
