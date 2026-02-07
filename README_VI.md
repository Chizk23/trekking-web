# TrekViet - Nền tảng Cộng đồng Trekking Việt Nam

> Hệ thống web kết nối cộng đồng leo núi và trekking tại Việt Nam - khám phá cung đường, tổ chức chuyến đi nhóm và chia sẻ trải nghiệm.

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

**TrekViet** là nền tảng web dành cho cộng đồng yêu thích trekking tại Việt Nam. Người dùng có thể tìm kiếm cung đường phù hợp, tổ chức hoặc tham gia chuyến đi nhóm, và chia sẻ trải nghiệm với cộng đồng.

**Các module chính:**
- **Cung đường:** Quản lý thông tin các tuyến trekking trên khắp Việt Nam
- **Chuyến đi:** Tổ chức trip nhóm với lịch trình và chat real-time
- **Cộng đồng:** Chia sẻ bài viết, hình ảnh và tương tác với thành viên khác
- **Kiến thức:** Bài viết hướng dẫn về kỹ năng, trang bị và an toàn
- **Gamification:** Hệ thống huy hiệu tự động trao thưởng khi đạt thành tích

### Video Demo
![Video Demo](LINK_VIDEO_DEMO)

---

## Tính năng chính

### 🗺️ Quản lý Cung đường

| Tính năng | Mô tả |
|-----------|-------|
| Khám phá cung đường | Tìm kiếm và lọc theo tỉnh thành, độ khó hoặc mùa đẹp nhất |
| Xem chi tiết | Thông tin độ dài, độ cao, thời gian ước tính và danh sách vật dụng gợi ý |
| Đánh giá & Review | Người dùng chấm điểm 1-5 sao và viết nhận xét kèm hình ảnh |
| Gallery ảnh/video | Xem và quản lý hình ảnh, video của từng cung đường |
| Đề xuất cung đường | Người dùng có thể gửi cung đường mới chờ Admin phê duyệt |

### 🎒 Tổ chức Chuyến đi

| Tính năng | Mô tả |
|-----------|-------|
| Tạo chuyến đi | Chọn cung đường, nhập số lượng thành viên, chi phí và điểm tập trung |
| Lập lịch trình | Xây dựng kế hoạch chi tiết theo từng ngày và khung giờ cụ thể |
| Chế độ công khai/riêng tư | Chuyến đi riêng tư yêu cầu mã mời để tham gia |
| Quản lý thành viên | Người tổ chức duyệt yêu cầu và phân vai trò Trưởng đoàn/Thành viên |
| Chat nhóm | Trao đổi thông tin, gửi ảnh/video, trả lời tin nhắn và react emoji |
| Trạng thái tự động | Hệ thống cập nhật: Chờ duyệt → Đang tuyển → Đang diễn ra → Hoàn thành |

### 👥 Cộng đồng

| Tính năng | Mô tả |
|-----------|-------|
| Viết bài | Chia sẻ trải nghiệm trekking kèm hình ảnh và video |
| Gắn tag | Liên kết bài viết với chuyến đi hoặc chủ đề cụ thể |
| Upvote/Downvote | Bình chọn bài viết hay và hữu ích |
| Bình luận | Tương tác với bài viết qua hệ thống bình luận phân cấp |

### 📚 Kiến thức

| Tính năng | Mô tả |
|-----------|-------|
| Bài viết hướng dẫn | Chia sẻ kiến thức theo chuyên mục: Kỹ thuật, Trang bị, An toàn... |
| Trình soạn thảo | Viết nội dung phong phú với TinyMCE editor |
| Phân loại | Quản lý bài viết theo danh mục dễ tìm kiếm |

### 🏆 Gamification

| Loại huy hiệu | Điều kiện ví dụ |
|---------------|-----------------|
| Hoạt động | Tham gia hoặc tổ chức 5/10/20 chuyến đi |
| Đóng góp | Đăng 10 bài viết hoặc 50 bình luận trên cộng đồng |
| Thể lực | Tích lũy 100km quãng đường hoặc 5000m độ cao |
| Khám phá | Đặt chân đến 10 tỉnh thành khác nhau |
| Thử thách | Hoàn thành cung đường có độ khó "Chuyên gia" |

> Hệ thống tự động kiểm tra và trao huy hiệu khi người dùng đạt điều kiện.

### 🔧 Trang Quản trị

| Tính năng | Mô tả |
|-----------|-------|
| Dashboard | Xem thống kê tổng quan: số người dùng, chuyến đi, bài viết... |
| Duyệt cung đường | Xem xét và phê duyệt/từ chối cung đường do người dùng đề xuất |
| Duyệt chuyến đi | Kiểm tra nội dung trước khi cho phép công khai tuyển thành viên |
| Duyệt bài viết | Kiểm duyệt nội dung cộng đồng trước khi hiển thị |
| Xử lý báo cáo | Tiếp nhận và giải quyết các report vi phạm từ người dùng |

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
| Bootstrap 5 | Xây dựng giao diện responsive |
| TinyMCE | Trình soạn thảo văn bản cho bài viết |
| Font Awesome | Icon cho các thành phần UI |

---

## Cài đặt

### Yêu cầu
- Python 3.8 trở lên
- MySQL 5.7 trở lên

### Các bước

```bash
# 1. Clone repository
git clone <repo_url>
cd trekking_web

# 2. Tạo môi trường ảo
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# 3. Cài đặt thư viện
pip install -r requirements.txt

# 4. Tạo database
mysql -u root -p
CREATE DATABASE trekking_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

# 5. Cấu hình database trong settings.py

# 6. Chạy migrations
python manage.py makemigrations
python manage.py migrate

# 7. Tạo tài khoản admin
python manage.py createsuperuser

# 8. Khởi động server
python manage.py runserver
```

**Truy cập:**
- Trang chủ: http://127.0.0.1:8000
- Trang quản trị: http://127.0.0.1:8000/dashboard/

---

## Ảnh chụp màn hình

### Giao diện Người dùng

| STT | Màn hình | Ảnh | Mô tả |
|:---:|----------|-----|-------|
| 1 | Trang chủ | ![Trang chủ](LINK_ANH_TRANG_CHU) | Giao diện chính hiển thị các cung đường nổi bật, sự kiện trekking sắp diễn ra và lối tắt đến các tính năng quan trọng. |
| 2 | Danh sách Cung đường | ![DS Cung đường](LINK_ANH_DS_CUNG_DUONG) | Thư viện cung đường với bộ lọc đa dạng theo tỉnh thành, độ khó và mùa trekking lý tưởng. |
| 3 | Chi tiết Cung đường | ![CT Cung đường](LINK_ANH_CT_CUNG_DUONG) | Thông tin đầy đủ về địa hình, độ cao, bản đồ GeoJSON, cùng đánh giá thực tế và hình ảnh từ cộng đồng. |
| 4 | Form tạo Cung đường | ![Form Cung đường](LINK_ANH_FORM_TAO_CUNG_DUONG) | Công cụ cho phép người dùng đóng góp cung đường mới với đầy đủ thông tin chi tiết và media. |
| 5 | Trip Hub | ![Trip Hub](LINK_ANH_TRIP_HUB) | Trung tâm tìm kiếm bạn đồng hành, hiển thị các chuyến đi đang mở đơn với trạng thái tuyển thành viên rõ ràng. |
| 6 | Chi tiết Chuyến đi | ![CT Chuyến đi](LINK_ANH_CT_CHUYEN_DI) | Thông tin chuyến đi bao gồm lịch trình, danh sách thành viên hiện tại và nút gửi yêu cầu tham gia. |
| 7 | Form tạo Chuyến đi | ![Form Chuyến đi](LINK_ANH_FORM_TAO_CHUYEN_DI) | Giao diện tạo trip mới cho phép thiết lập số lượng thành viên, chi phí dự kiến và chế độ riêng tư (mã mời). |
| 8 | Lập lịch trình | ![Lịch trình](LINK_ANH_LAP_LICH_TRINH) | Công cụ lập kế hoạch hành trình chi tiết theo từng ngày và khung giờ cụ thể cho chuyến đi. |
| 9 | Chat nhóm | ![Chat](LINK_ANH_CHAT_NHOM) | Không gian thảo luận riêng tư của từng chuyến đi, hỗ trợ gửi tin nhắn, hình ảnh và video real-time. |
| 10 | Góc Cộng đồng | ![Cộng đồng](LINK_ANH_CONG_DONG) | Nơi chia sẻ bài viết, trải nghiệm trekking, tương tác qua bình luận và hệ thống upvote/downvote. |
| 11 | Kiến thức | ![Kiến thức](LINK_ANH_KIEN_THUC) | Kho tàng bài viết hướng dẫn kỹ năng, trang bị và an toàn được phân loại theo chuyên mục rõ ràng. |
| 12 | Hồ sơ cá nhân | ![Hồ sơ](LINK_ANH_HO_SO) | Trang quản lý thông tin tài khoản, tủ đồ trekking cá nhân và trưng bày bộ sưu tập huy hiệu thành tích. |

### Giao diện Quản trị

| STT | Màn hình | Ảnh | Mô tả |
|:---:|----------|-----|-------|
| 13 | Dashboard | ![Dashboard](LINK_ANH_ADMIN_DASHBOARD) | Bảng điều khiển trung tâm thống kê tổng quan về người dùng, bài viết và hoạt động hệ thống. |
| 14 | Duyệt Cung đường | ![Duyệt CD](LINK_ANH_DUYET_CUNG_DUONG) | Giao diện kiểm duyệt nội dung cung đường do người dùng đóng góp trước khi công khai. |
| 15 | Duyệt Chuyến đi | ![Duyệt Trip](LINK_ANH_DUYET_CHUYEN_DI) | Công cụ xem xét và phê duyệt các chuyến đi mới được tạo trên hệ thống. |
| 16 | Duyệt Bài viết | ![Duyệt Post](LINK_ANH_DUYET_BAI_VIET) | Hệ thống kiểm duyệt bài viết cộng đồng đảm bảo nội dung phù hợp và chất lượng. |
| 17 | Quản lý Báo cáo | ![Báo cáo](LINK_ANH_QUAN_LY_BAO_CAO) | Danh sách và công cụ xử lý các báo cáo vi phạm từ người dùng gửi về. |

---

## Cấu trúc dự án

```
trekking_web/
├── accounts/          # Đăng ký, đăng nhập và hồ sơ người dùng
├── treks/             # CRUD cung đường, đánh giá, media
├── trips/             # Tạo chuyến đi, quản lý thành viên, chat
├── community/         # Bài viết cộng đồng, bình luận, upvote
├── articles/          # Bài viết kiến thức (quản lý bởi admin)
├── knowledge/         # Hiển thị kiến thức cho người dùng
├── gamification/      # Huy hiệu và logic trao thưởng
├── report_admin/      # Xử lý báo cáo vi phạm
├── user_admin/        # Quản lý danh sách người dùng
├── core/              # Model dùng chung: TinhThanh, DoKho, VatDung, The
├── templates/         # Giao diện HTML
├── static/            # CSS, JavaScript, hình ảnh
├── media/             # File upload từ người dùng
└── requirements.txt   # Danh sách thư viện Python
```

---

## Nhóm phát triển

| Thành viên | Module phụ trách |
|------------|------------------|
| Developer 1 | Treks, Trips, User Admin |
| Developer 2 | Community, Knowledge, Gamification, Articles, Reports |

---

**⭐ Nếu thấy dự án hữu ích, hãy cho chúng tôi một star!**
