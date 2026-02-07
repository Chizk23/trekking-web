# TrekViet - Nền tảng Cộng đồng Trekking Việt Nam

> Hệ thống web toàn diện kết nối cộng đồng leo núi và trekking tại Việt Nam, hỗ trợ quản lý cung đường, tổ chức chuyến đi nhóm và chia sẻ trải nghiệm.

<p align="center">
  <img src="LINK_ANH_BANNER_1" width="45%" />
  <img src="LINK_ANH_BANNER_2" width="45%" />
</p>

## Mục lục

1. [Giới thiệu](#giới-thiệu)
2. [Tính năng chính](#tính-năng-chính)
3. [Kiến trúc hệ thống](#kiến-trúc-hệ-thống)
4. [Công nghệ sử dụng](#công-nghệ-sử-dụng)
5. [Cài đặt và Triển khai](#cài-đặt-và-triển-khai)
6. [Hướng dẫn sử dụng](#hướng-dẫn-sử-dụng)
7. [Ảnh chụp màn hình](#ảnh-chụp-màn-hình)
8. [Cấu trúc dự án](#cấu-trúc-dự-án)

---

## Giới thiệu

**TrekViet** là giải pháp tích hợp giúp cộng đồng yêu thích trekking tại Việt Nam có thể khám phá cung đường, tổ chức chuyến đi nhóm và kết nối với những người có cùng đam mê.

**Thành phần cốt lõi:**
- **Quản lý Cung đường:** Cơ sở dữ liệu chi tiết về các cung đường trekking trên khắp Việt Nam với đánh giá, hình ảnh và thông tin GeoJSON.
- **Tổ chức Chuyến đi:** Công cụ tạo chuyến đi nhóm với lịch trình chi tiết, quản lý thành viên và chat nhóm real-time.
- **Cộng đồng:** Nền tảng chia sẻ trải nghiệm, bài viết và kết nối bạn đồng hành.
- **Gamification:** Hệ thống huy hiệu với 14 loại thành tích khuyến khích hoạt động.

### Video Demo
![Video Demo](LINK_VIDEO_DEMO)

---

## Tính năng chính

### Dành cho Người dùng (User)

| Tính năng | Mô tả |
|-----------|-------|
| Khám phá cung đường | Tìm kiếm, lọc theo tỉnh thành, độ khó, mùa đẹp nhất |
| Đánh giá & Review | Chấm điểm 1-5 sao, viết bình luận kèm hình ảnh |
| Đề xuất cung đường | Người dùng có thể đề xuất cung đường mới chờ duyệt |
| Tạo chuyến đi | Lập kế hoạch chi tiết, đặt số lượng, chi phí dự kiến |
| Tham gia chuyến đi | Gửi yêu cầu tham gia, chat nhóm với thành viên |
| Viết bài cộng đồng | Chia sẻ trải nghiệm, hình ảnh, video |
| Nhận huy hiệu | Tự động nhận thưởng khi đạt các mốc thành tích |

### Dành cho Quản trị viên (Admin)

| Tính năng | Mô tả |
|-----------|-------|
| Dashboard tổng quan | Thống kê số liệu hệ thống |
| Duyệt cung đường | Phê duyệt/từ chối cung đường do người dùng đề xuất |
| Duyệt chuyến đi | Kiểm tra và phê duyệt chuyến đi mới |
| Duyệt bài viết | Kiểm duyệt nội dung cộng đồng trước khi công khai |
| Xử lý báo cáo | Tiếp nhận và giải quyết report vi phạm |
| Quản lý người dùng | Phân quyền, khóa tài khoản |

### Đặc tả kỹ thuật Gamification

| Loại điều kiện | Ví dụ |
|----------------|-------|
| Số lượng hoạt động | Tham gia 5/10/20 chuyến đi |
| Đóng góp nội dung | Viết 10 bài viết, 50 bình luận |
| Thể lực | Tổng 100km quãng đường, 5000m độ cao leo |
| Khám phá | Đến 10 tỉnh thành khác nhau |
| Thử thách | Hoàn thành cung đường độ khó "Chuyên gia" |

---

## Kiến trúc hệ thống

Hệ thống được thiết kế theo mô hình MVC với Django Framework:

```mermaid
graph TB
    subgraph Client["Client (Browser)"]
        USER[Người dùng]
        ADMIN[Quản trị viên]
    end
    
    subgraph Server["Django Server"]
        VIEWS[Views/Controllers]
        MODELS[Models/ORM]
        TEMPLATES[Templates/Jinja2]
        STATIC[Static Files]
    end
    
    subgraph Database["Database"]
        MYSQL[(MySQL)]
    end
    
    subgraph Storage["Media Storage"]
        MEDIA[/Media Files/]
    end
    
    USER --> VIEWS
    ADMIN --> VIEWS
    VIEWS --> MODELS
    VIEWS --> TEMPLATES
    MODELS --> MYSQL
    TEMPLATES --> STATIC
    VIEWS --> MEDIA
```

### Quy trình tổ chức Chuyến đi

```mermaid
flowchart LR
    CREATE([Tạo chuyến đi]) -->|Chờ duyệt| ADMIN{Admin duyệt?}
    ADMIN --Từ chối--> REJECT[Bị từ chối]
    ADMIN --Duyệt--> OPEN[Đang tuyển]
    
    OPEN --> JOIN([Người dùng tham gia])
    JOIN -->|Chờ duyệt| HOST{Host duyệt?}
    HOST --Từ chối--> DENIED[Bị từ chối]
    HOST --Duyệt--> MEMBER[Thành viên]
    
    OPEN -->|Đủ người| FULL[Đã đủ người]
    OPEN -->|Đến ngày| ONGOING[Đang diễn ra]
    ONGOING -->|Kết thúc| DONE[Hoàn thành]
    
    style CREATE fill:#10b981,stroke:#333,stroke-width:2px
    style DONE fill:#3b82f6,stroke:#333,stroke-width:2px
    style REJECT fill:#ef4444,stroke:#333,stroke-width:2px
```
*Hình 1: Quy trình trạng thái chuyến đi.*

---

## Công nghệ sử dụng

### Backend

| Công nghệ | Phiên bản | Mục đích |
|-----------|-----------|----------|
| Python | 3.8+ | Ngôn ngữ lập trình |
| Django | 4.2.23 | Web Framework |
| MySQL | 5.7+ | Cơ sở dữ liệu |
| mysqlclient | 2.2.7 | MySQL Connector |
| Pillow | 11.3.0 | Xử lý hình ảnh |

### Frontend

| Công nghệ | Mục đích |
|-----------|----------|
| Bootstrap 5 | Framework CSS responsive |
| TinyMCE | Rich text editor |
| Font Awesome | Thư viện icon |
| Animate.css | Hiệu ứng animation |

---

## Cài đặt và Triển khai

### 1. Yêu cầu hệ thống

- **Server:** Python 3.8+, MySQL 5.7+
- **RAM:** 2GB trở lên
- **Disk:** 1GB cho source code, thêm dung lượng cho media

### 2. Cài đặt Server

```bash
# Clone source code
git clone <repo_url>
cd trekking_web

# Tạo môi trường ảo
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Cài đặt dependencies
pip install -r requirements.txt

# Tạo database MySQL
mysql -u root -p
CREATE DATABASE trekking_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

# Cấu hình settings.py (cập nhật thông tin database)

# Chạy migrations
python manage.py makemigrations
python manage.py migrate

# Tạo superuser
python manage.py createsuperuser

# Chạy server
python manage.py runserver
```

### 3. Truy cập

- **Trang chủ:** http://127.0.0.1:8000
- **Admin Dashboard:** http://127.0.0.1:8000/dashboard/

---

## Hướng dẫn sử dụng

### Đăng nhập
- **Quản trị viên:** Tài khoản superuser đã tạo
- **Người dùng:** Đăng ký tài khoản mới hoặc được Admin cấp

### Quy trình tạo Chuyến đi

```mermaid
sequenceDiagram
    autonumber
    actor U as Người tổ chức
    participant W as Web Dashboard
    participant A as Admin
    participant M as Thành viên

    Note over U, W: 1. Tạo chuyến đi
    U->>W: Chọn cung đường, nhập thông tin
    U->>W: Lập lịch trình chi tiết
    W-->>U: Chuyến đi chờ duyệt

    Note over A, W: 2. Admin duyệt
    A->>W: Xem và duyệt chuyến đi
    W-->>U: Thông báo được duyệt

    Note over M, W: 3. Tuyển thành viên
    M->>W: Gửi yêu cầu tham gia
    W-->>U: Thông báo có yêu cầu mới
    U->>W: Duyệt thành viên
    W-->>M: Thông báo được chấp nhận

    Note over U, M: 4. Chat nhóm
    U->>W: Nhắn tin trong nhóm
    W-->>M: Hiển thị tin nhắn
    M->>W: Phản hồi, gửi ảnh/video
```

---

## Ảnh chụp màn hình

### Trang chủ
![Trang chủ](LINK_ANH_TRANG_CHU)
*Hình 2: Giao diện trang chủ với hero section và các cung đường nổi bật.*

### Danh sách Cung đường
![Danh sách cung đường](LINK_ANH_DS_CUNG_DUONG)
*Hình 3: Trang khám phá cung đường với bộ lọc theo tỉnh thành, độ khó.*

### Chi tiết Cung đường
![Chi tiết cung đường](LINK_ANH_CT_CUNG_DUONG)
*Hình 4: Thông tin chi tiết cung đường với gallery ảnh và đánh giá.*

### Form tạo Cung đường
![Form tạo cung đường](LINK_ANH_FORM_TAO_CUNG_DUONG)
*Hình 5: Giao diện đề xuất cung đường mới.*

### Trip Hub
![Trip Hub](LINK_ANH_TRIP_HUB)
*Hình 6: Danh sách các chuyến đi đang tuyển thành viên.*

### Chi tiết Chuyến đi
![Chi tiết chuyến đi](LINK_ANH_CT_CHUYEN_DI)
*Hình 7: Thông tin chuyến đi với lịch trình và danh sách thành viên.*

### Form tạo Chuyến đi
![Form tạo chuyến đi](LINK_ANH_FORM_TAO_CHUYEN_DI)
*Hình 8: Giao diện tạo chuyến đi mới.*

### Lập lịch trình
![Lập lịch trình](LINK_ANH_LAP_LICH_TRINH)
*Hình 9: Giao diện lập kế hoạch lịch trình chi tiết theo ngày/giờ.*

### Chat nhóm
![Chat nhóm](LINK_ANH_CHAT_NHOM)
*Hình 10: Phòng chat nhóm của chuyến đi.*

### Góc Cộng đồng
![Cộng đồng](LINK_ANH_CONG_DONG)
*Hình 11: Danh sách bài viết cộng đồng.*

### Hồ sơ cá nhân
![Hồ sơ](LINK_ANH_HO_SO)
*Hình 12: Trang hồ sơ với thông tin và huy hiệu đã đạt.*

### Admin Dashboard
![Admin Dashboard](LINK_ANH_ADMIN_DASHBOARD)
*Hình 13: Dashboard tổng quan cho quản trị viên.*

### Duyệt nội dung
![Duyệt nội dung](LINK_ANH_DUYET_NOI_DUNG)
*Hình 14: Giao diện duyệt cung đường/chuyến đi/bài viết.*

---

## Cấu trúc dự án

```text
trekking_web/
├── accounts/                # Tài khoản & Hồ sơ người dùng
│   ├── models.py            # Model TaiKhoanHoSo
│   ├── views.py             # Đăng ký, đăng nhập, profile
│   └── templates/           # Giao diện accounts
│
├── treks/                   # Quản lý Cung đường
│   ├── models.py            # CungDuongTrek, DanhGia, Media
│   ├── views.py             # CRUD cung đường
│   └── templates/           # Giao diện cung đường
│
├── trips/                   # Tổ chức Chuyến đi
│   ├── models.py            # ChuyenDi, ThanhVien, TinNhan
│   ├── views.py             # Trip hub, chat, timeline
│   └── templates/           # Giao diện chuyến đi
│
├── community/               # Bài viết Cộng đồng
│   ├── models.py            # CongDongBaiViet, BinhLuan
│   ├── views.py             # CRUD bài viết
│   └── templates/           # Giao diện cộng đồng
│
├── gamification/            # Hệ thống Huy hiệu
│   ├── models.py            # GameHuyHieu, HuyHieuNguoiDung
│   └── services.py          # Logic kiểm tra & trao thưởng
│
├── articles/                # Bài viết Kiến thức
├── knowledge/               # Kiến thức Trekking
├── report_admin/            # Báo cáo Vi phạm
├── user_admin/              # Quản trị Người dùng
├── core/                    # Module dùng chung
│   └── models.py            # TinhThanh, DoKho, VatDung, The
│
├── templates/               # Base templates
│   ├── base.html            # Template người dùng
│   └── admin_base.html      # Template admin
│
├── static/                  # CSS, JS, Images
│   ├── css/
│   ├── js/
│   └── images/
│
├── media/                   # File upload
└── requirements.txt         # Dependencies
```

---

## Thông tin bổ sung

### Design System
Dự án sử dụng **TrekViet Design System** với màu chủ đạo **Emerald Green** (`#10b981`), tuân theo BEM methodology và responsive design với breakpoints 576px, 768px, 992px, 1200px.

### Bảo mật
> ⚠️ **Lưu ý:** File `settings.py` hiện tại chứa cấu hình development. Khi deploy production cần:
> - Tắt `DEBUG = False`
> - Dùng biến môi trường cho `SECRET_KEY`
> - Thêm domain vào `ALLOWED_HOSTS`

---

## Đóng góp

Dự án được phát triển cho mục đích học thuật. Mọi đóng góp từ cộng đồng đều được hoan nghênh.

---

## Nhóm phát triển

**Thành viên nhóm:**

| Thành viên | Module phụ trách |
|------------|------------------|
| **Developer 1** | Treks, Trips, User Admin |
| **Developer 2** | Community, Knowledge, Gamification, Articles, Reports |

---

**⭐ Nếu thấy dự án hữu ích, hãy cho chúng tôi một star!**
