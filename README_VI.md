# TrekViet - Nền tảng Cộng đồng Trekking Việt Nam

> Hệ thống web kết nối cộng đồng leo núi và trekking tại Việt Nam - khám phá cung đường, tổ chức chuyến đi nhóm và chia sẻ trải nghiệm.

<p align="center">
  <img src="docs/images/banner.png" width="100%" />
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


---

## Tính năng chính

### 🗺️ Quản lý Cung đường

| Tính năng | Mô tả |
|-----------|-------|
| Khám phá cung đường | Tìm kiếm và lọc theo tỉnh thành, độ khó, độ cao hoặc thời gian dự kiến |
| Xem chi tiết | Thông tin độ dài, độ cao, thời gian ước tính và danh sách vật dụng gợi ý |
| Đánh giá & Review | Người dùng chấm điểm 1-5 sao và viết nhận xét kèm hình ảnh |
| Gallery ảnh/video | Xem và quản lý hình ảnh, video của từng cung đường |
| **Đóng góp cung đường** | Người dùng gửi cung đường mới kèm ảnh/video, chờ Admin duyệt |
| **Quản lý đóng góp** | Xem danh sách cung đường đã gửi, theo dõi trạng thái (Chờ duyệt/Đã duyệt/Từ chối) |

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
| Upvote | Bình chọn bài viết hay và hữu ích |
| Bình luận | Tương tác với bài viết qua hệ thống bình luận phân cấp (trả lời bình luận) |
| Duyệt bài | Bài viết cần Admin duyệt trước khi hiển thị công khai |

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
| Dashboard | Xem thống kê tổng quan: số người dùng, chuyến đi, bài viết và biểu đồ phân tích |
| Duyệt cung đường | Xem xét cung đường người dùng đóng góp, phê duyệt hoặc từ chối kèm lý do |
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
| 1 | Danh sách Cung đường | ![DS Cung đường](docs/images/danhsachcungduong.png) | Bộ lọc chuyên sâu: Tỉnh thành, độ khó, độ dài (km), thời gian và đánh giá. Hỗ trợ tìm kiếm từ khóa. |
| 2 | Chi tiết Cung đường | <img src="docs/images/chitiecd1.png" width="100%"><br><img src="docs/images/chitietcd2.png" width="100%"><br><img src="docs/images/chitietcd3.png" width="100%"><br><img src="docs/images/chitietcd4.png" width="100%"> | Hiển thị thông tin địa hình, bản đồ tương tác (GeoJSON), galerry ảnh và hệ thống đánh giá/bình luận đa phương tiện. |
| 3 | Form tạo Cung đường | <img src="docs/images/taocd1.png" width="100%"><br><img src="docs/images/taocd2.png" width="100%"><br><img src="docs/images/taocd3.png" width="100%"> | Giao diện nhập liệu chi tiết với CKEditor/TinyMCE, tích hợp upload bản đồ GeoJSON và quản lý vật dụng gợi ý. |
| 4 | Trip Hub | ![Trip Hub](docs/images/triphub.png) | Tìm kiếm chuyến đi theo ngân sách, thời lượng, ngày khởi hành. Có bộ lọc "Chỉ hiện chuyến còn chỗ" và hiển thị trạng thái (Sắp đi, Đang tuyển). |
| 5 | Chi tiết Chuyến đi | <img src="docs/images/chitietchuyendi1.png" width="100%"><br><img src="docs/images/chitietchuyendi2.png" width="100%"><br><img src="docs/images/chitietchuyendi3.png" width="100%"> | Thông tin chi tiết lịch trình (Timeline), danh sách thành viên tham gia, và cơ chế tham gia (Công khai/Riêng tư với mã mời). |
| 6 | Form tạo Chuyến đi | <img src="docs/images/tạochuyendi1.png" width="100%"><br><img src="docs/images/taochuyendi2.png" width="100%"> | Quy trình thiết lập chuyến đi 2 bước tối ưu: Chọn cung đường mẫu -> Điền thông tin. Tích hợp công cụ **Lập lịch trình (Itinerary Builder)** cho phép kéo thả các mốc hoạt động theo ngày/giờ chi tiết. |
| 7 | Chat nhóm | ![Chat](docs/images/tinnhan.png) | Hệ thống chat realtime tích hợp trong chuyến đi: Gửi tin nhắn, chia sẻ file/ảnh, và danh sách thành viên online. |
| 8 | Góc Cộng đồng | <img src="docs/images/congdong.png" width="100%"> | Danh sách bài viết tin tức/chia sẻ với tính năng Upvote, bình luận và hiển thị thẻ tác giả (Avatar/Tên). |
| 9 | Kiến thức | <img src="docs/images/khokt.png" width="100%">| Thư viện bài viết hướng dẫn (Kỹ năng, Trang bị) được phân loại theo chuyên mục, hiển thị dạng thẻ Grid. |
| 10 | Hồ sơ cá nhân | ![Hồ sơ](docs/images/hosocanhan.png) | Trang tổng hợp: Lịch sử chuyến đi đã duyệt, Bộ sưu tập huy hiệu (Gamification), Quản lý tủ đồ cá nhân và Bài viết đã đăng. |

### Giao diện Quản trị

| STT | Màn hình | Ảnh | Mô tả |
|:---:|----------|-----|-------|
| 13 | Dashboard | ![Dashboard](docs/images/dashboard.png) | **Trung tâm Phân tích Dữ liệu**: Hiển thị các chỉ số KPI quan trọng (User, Trip, Doanh thu) và biểu đồ tăng trưởng thực tế. Hỗ trợ ra quyết định nhờ Ma trận BCG đánh giá chất lượng cung đường và Phễu chuyển đổi người dùng. |
| 14 | Duyệt Cung đường | ![Duyệt CD](docs/images/duyetcungduong.png) | **Quản lý & Kiểm duyệt**: Tích hợp Bộ lọc nhanh (Quick Filters) giúp phát hiện lỗi như thiếu ảnh, thiếu bản đồ hay rating thấp. Admin có thể duyệt nhanh hoặc yêu cầu chỉnh sửa dữ liệu GeoJSON trực tiếp. |
| 15 | Duyệt Chuyến đi | ![Duyệt Trip](docs/images/duyetchuyendi.png) | **Kiểm soát Rủi ro**: Hệ thống tự động ưu tiên các chuyến cần duyệt và cảnh báo rủi ro (Chuyến đi "Ma", Sắp khởi hành). Giúp Admin tập trung xử lý các trường hợp gấp hoặc vi phạm quy định an toàn. |
| 16 | Duyệt Bài viết | ![Duyệt Bài viết](docs/images/quanlybaiviet.png) | **Kiểm duyệt Cộng đồng**: Cho phép duyệt hoặc từ chối hàng loạt (Bulk Actions) bài viết với giao diện tối ưu. Tích hợp xem trước Media ngay trong danh sách giúp quy trình kiểm duyệt nhanh chóng hơn. |
| 17 | Thống kê và Báo cáo | ![Thống kê và Báo cáo](docs/images/thongkevabaocao.png) | **Giám sát & Xử lý**: Tổng hợp báo cáo vi phạm từ người dùng và thống kê xu hướng nội dung xấu. Quy trình xử lý khép kín (Cảnh báo/Xóa/Khóa) giúp duy trì môi trường cộng đồng lành mạnh. |
| 18 | Quản lý Người dùng | ![Quản lý User](docs/images/quanlyuser.png) | **Quản trị Tài khoản**: Thống kê người dùng (Mới/Active/Locked). Tích hợp bộ lọc theo Vai trò (Admin/Thành viên) và Trạng thái. Hỗ trợ xem chi tiết hồ sơ (Sở thích, Đồ dùng), lịch sử hoạt động và thực hiện Khóa/Mở khóa hoặc Xóa tài khoản. |
| 19 | Hệ thống Gamification | ![Gamification](docs/images/gamefication.png) | **Quản lý Vinh danh**: Thiết lập các tiêu chí đạt danh hiệu (Badges) và theo dõi tiến độ người dùng. Hệ thống tự động cấp phát huy hiệu dựa trên dữ liệu hoạt động thực tế (số chuyến đi, bài đóng góp). |

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
├── gamification/      # Huy hi\ệu và logic trao thưởng
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
