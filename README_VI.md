# TrekViet - Nền tảng Cộng đồng Trekking Việt Nam

> Hệ thống web kết nối cộng đồng leo núi và trekking tại Việt Nam, hỗ trợ quản lý cung đường, tổ chức chuyến đi nhóm và chia sẻ trải nghiệm.

<p align="center">
  <img src="LINK_ANH_BANNER_1" width="45%" />
  <img src="LINK_ANH_BANNER_2" width="45%" />
</p>

## Mục lục

1. [Giới thiệu](#giới-thiệu)
2. [Tính năng chính](#tính-năng-chính)
3. [Công nghệ sử dụng](#công-nghệ-sử-dụng)
4. [Cài đặt](#cài-đặt)
5. [Ảnh chụp màn hình](#ảnh-chụp-màn-hình)
6. [Cấu trúc dự án](#cấu-trúc-dự-án)

---

## Giới thiệu

**TrekViet** là nền tảng web giúp cộng đồng yêu thích trekking tại Việt Nam khám phá cung đường, tổ chức chuyến đi nhóm và kết nối với những người có cùng đam mê.

**Thành phần chính:**
- **Quản lý Cung đường:** Thông tin chi tiết các cung đường với đánh giá, hình ảnh, bản đồ GeoJSON
- **Tổ chức Chuyến đi:** Tạo chuyến đi nhóm với lịch trình, quản lý thành viên, chat nhóm
- **Cộng đồng:** Chia sẻ trải nghiệm, bài viết, kết nối bạn đồng hành
- **Kiến thức:** Bài viết hướng dẫn theo chuyên mục
- **Gamification:** Hệ thống huy hiệu với 14 loại thành tích

### Video Demo
![Video Demo](LINK_VIDEO_DEMO)

---

## Tính năng chính

### 🗺️ Quản lý Cung đường

| Tính năng | Mô tả |
|-----------|-------|
| Danh sách cung đường | Lọc theo tỉnh thành, độ khó, mùa đẹp nhất |
| Chi tiết cung đường | Độ dài, độ cao leo, thời gian ước tính, gợi ý trang bị |
| Đánh giá & Review | Chấm điểm 1-5 sao, bình luận kèm hình ảnh |
| Gallery ảnh/video | Quản lý media cho từng cung đường |
| Đề xuất cung đường | Người dùng đề xuất, Admin duyệt trước khi công khai |

### 🎒 Tổ chức Chuyến đi

| Tính năng | Mô tả |
|-----------|-------|
| Tạo chuyến đi | Chọn cung đường, đặt số lượng, chi phí, điểm tập trung |
| Lập lịch trình | Kế hoạch chi tiết theo ngày và khung giờ |
| Chế độ riêng tư | Công khai hoặc mời bằng mã riêng |
| Quản lý thành viên | Duyệt yêu cầu, phân vai trò Trưởng đoàn/Thành viên |
| Chat nhóm | Nhắn tin, gửi ảnh/video, reply, like/dislike |
| Trạng thái động | Chờ duyệt → Đang tuyển → Đang diễn ra → Hoàn thành |

### 👥 Cộng đồng

| Tính năng | Mô tả |
|-----------|-------|
| Bài viết | Chia sẻ trải nghiệm kèm hình ảnh, video |
| Hashtag & Tag | Gắn chủ đề, liên kết chuyến đi |
| Tương tác | Upvote/Downvote, bình luận phân cấp |
| Kiểm duyệt | Admin duyệt trước khi công khai |

### 📚 Kiến thức & Hướng dẫn

| Tính năng | Mô tả |
|-----------|-------|
| Bài viết hướng dẫn | Theo chuyên mục: Kỹ thuật, Trang bị, An toàn... |
| Rich text editor | TinyMCE với nội dung phong phú |
| Quy trình duyệt | Admin kiểm duyệt trước khi đăng |

### 🏆 Gamification

| Loại điều kiện | Ví dụ |
|----------------|-------|
| Hoạt động | Tham gia 5/10/20 chuyến đi |
| Đóng góp | Viết 10 bài viết, 50 bình luận |
| Thể lực | Tổng 100km quãng đường, 5000m độ cao leo |
| Khám phá | Đến 10 tỉnh thành khác nhau |
| Thử thách | Hoàn thành cung đường độ khó "Chuyên gia" |

### 🔧 Quản trị Admin

| Tính năng | Mô tả |
|-----------|-------|
| Dashboard | Thống kê tổng quan hệ thống |
| Duyệt cung đường | Phê duyệt/từ chối cung đường mới |
| Duyệt chuyến đi | Kiểm tra và phê duyệt chuyến đi |
| Duyệt bài viết | Kiểm duyệt nội dung cộng đồng |
| Xử lý báo cáo | Tiếp nhận và giải quyết report vi phạm |
| Quản lý người dùng | Xem danh sách, khóa tài khoản |

---

## Công nghệ sử dụng

### Backend

| Công nghệ | Phiên bản |
|-----------|-----------|
| Python | 3.8+ |
| Django | 4.2.23 |
| MySQL | 5.7+ |
| Pillow | 11.3.0 |

### Frontend

| Công nghệ | Mô tả |
|-----------|-------|
| Bootstrap 5 | Framework CSS |
| TinyMCE | Rich text editor |
| Font Awesome | Icon library |

---

## Cài đặt

### Yêu cầu
- Python 3.8+
- MySQL 5.7+

### Các bước

```bash
# 1. Clone repository
git clone <repo_url>
cd trekking_web

# 2. Tạo virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# 3. Cài đặt dependencies
pip install -r requirements.txt

# 4. Tạo database
mysql -u root -p
CREATE DATABASE trekking_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

# 5. Cấu hình database trong settings.py

# 6. Chạy migrations
python manage.py makemigrations
python manage.py migrate

# 7. Tạo superuser
python manage.py createsuperuser

# 8. Chạy server
python manage.py runserver
```

**Truy cập:**
- Trang chủ: http://127.0.0.1:8000
- Admin: http://127.0.0.1:8000/dashboard/

---

## Ảnh chụp màn hình

### Giao diện Người dùng

| STT | Màn hình | Ảnh | Mô tả |
|:---:|----------|-----|-------|
| 1 | Trang chủ | ![Trang chủ](LINK_ANH_TRANG_CHU) | Hero section, cung đường nổi bật |
| 2 | Danh sách Cung đường | ![DS Cung đường](LINK_ANH_DS_CUNG_DUONG) | Lọc theo tỉnh thành, độ khó |
| 3 | Chi tiết Cung đường | ![CT Cung đường](LINK_ANH_CT_CUNG_DUONG) | Thông tin, gallery, đánh giá |
| 4 | Form tạo Cung đường | ![Form Cung đường](LINK_ANH_FORM_TAO_CUNG_DUONG) | Đề xuất cung đường mới |
| 5 | Trip Hub | ![Trip Hub](LINK_ANH_TRIP_HUB) | Danh sách chuyến đi |
| 6 | Chi tiết Chuyến đi | ![CT Chuyến đi](LINK_ANH_CT_CHUYEN_DI) | Lịch trình, thành viên |
| 7 | Form tạo Chuyến đi | ![Form Chuyến đi](LINK_ANH_FORM_TAO_CHUYEN_DI) | Tạo chuyến đi mới |
| 8 | Lập lịch trình | ![Lịch trình](LINK_ANH_LAP_LICH_TRINH) | Kế hoạch theo ngày/giờ |
| 9 | Chat nhóm | ![Chat](LINK_ANH_CHAT_NHOM) | Chat của chuyến đi |
| 10 | Góc Cộng đồng | ![Cộng đồng](LINK_ANH_CONG_DONG) | Bài viết cộng đồng |
| 11 | Kiến thức | ![Kiến thức](LINK_ANH_KIEN_THUC) | Bài viết hướng dẫn |
| 12 | Hồ sơ cá nhân | ![Hồ sơ](LINK_ANH_HO_SO) | Thông tin, huy hiệu |

### Giao diện Quản trị

| STT | Màn hình | Ảnh | Mô tả |
|:---:|----------|-----|-------|
| 13 | Dashboard | ![Dashboard](LINK_ANH_ADMIN_DASHBOARD) | Thống kê hệ thống |
| 14 | Duyệt Cung đường | ![Duyệt CD](LINK_ANH_DUYET_CUNG_DUONG) | Phê duyệt cung đường |
| 15 | Duyệt Chuyến đi | ![Duyệt Trip](LINK_ANH_DUYET_CHUYEN_DI) | Phê duyệt chuyến đi |
| 16 | Duyệt Bài viết | ![Duyệt Post](LINK_ANH_DUYET_BAI_VIET) | Kiểm duyệt bài viết |
| 17 | Quản lý Báo cáo | ![Báo cáo](LINK_ANH_QUAN_LY_BAO_CAO) | Xử lý report |

---

## Cấu trúc dự án

```
trekking_web/
├── accounts/          # Tài khoản & hồ sơ người dùng
├── treks/             # Quản lý cung đường
├── trips/             # Tổ chức chuyến đi & chat
├── community/         # Bài viết cộng đồng
├── articles/          # Bài viết kiến thức (admin)
├── knowledge/         # Kiến thức trekking
├── gamification/      # Hệ thống huy hiệu
├── report_admin/      # Báo cáo vi phạm
├── user_admin/        # Quản trị người dùng
├── core/              # Module dùng chung (TinhThanh, DoKho, VatDung)
├── templates/         # HTML templates
├── static/            # CSS, JS, images
├── media/             # File upload
└── requirements.txt
```

---

## Nhóm phát triển

| Thành viên | Module phụ trách |
|------------|------------------|
| Developer 1 | Treks, Trips, User Admin |
| Developer 2 | Community, Knowledge, Gamification, Articles, Reports |

---

**⭐ Nếu thấy dự án hữu ích, hãy cho chúng tôi một star!**
