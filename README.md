# TrekViet - Vietnam Trekking Community Platform

> A web platform connecting the trekking and mountaineering community in Vietnam - discovering trails, organizing group trips, and sharing experiences.

<p align="center">
  <img src="docs/images/banner.png" width="100%" />
</p>

## Table of Contents

1. [Introduction](#introduction)
2. [Key Features](#key-features)
3. [Technologies](#technologies)
4. [Installation](#installation)
5. [Screenshots](#screenshots)
6. [Project Structure](#project-structure)

---

## Introduction

**TrekViet** is a web platform dedicated to the trekking community in Vietnam. Users can search for suitable trails, organize or join group trips, and share their experiences with the community.

**Main Modules:**
- **Treks:** Manage information about trekking routes across Vietnam.
- **Trips:** Organize group trips with schedules and real-time chat.
- **Community:** Share posts, photos, and interact with other members.
- **Knowledge:** Guides on skills, equipment, and safety.
- **Gamification:** Automated badge system rewarding user achievements.


---

## Key Features

### 🗺️ Trek Management

| Feature | Description |
|---------|-------------|
| Discover Treks | Search and filter by province, difficulty, altitude, or estimated duration. |
| View Details | Information on length, altitude, estimated time, and suggested equipment list. |
| Ratings & Reviews | Users rate 1-5 stars and write reviews with images. |
| Gallery | View and manage images/videos for each trek. |
| **Contribute Trek** | Users submit new trail data with media, pending Admin approval. |
| **Contribution Mgmt** | View submitted trails and track status (Pending/Approved/Rejected). |

### 🎒 Trip Organization

| Feature | Description |
|---------|-------------|
| Create Trip | Select a trek, input member limit, cost, and meeting point. |
| Itinerary Builder | Build a detailed plan by day and specific time slots. |
| Public/Private Mode | Private trips require an invitation code to join. |
| Member Management | Organizer approves requests and assigns roles (Leader/Member). |
| Group Chat | Exchange info, send media, reply to messages, and react with emojis. |
| Auto Status | System updates: Pending → Recruiting → Ongoing → Completed. |

### 👥 Community

| Feature | Description |
|---------|-------------|
| Write Posts | Share trekking experiences with images and videos. |
| Tagging | Link posts to specific trips or topics. |
| Upvote | Vote for helpful and interesting posts. |
| Comments | Interact via a threaded comment system (nested replies). |
| Post Approval | Posts require Admin approval before being publicly displayed. |

### 📚 Knowledge

| Feature | Description |
|---------|-------------|
| Guide Articles | Share knowledge by category: Techniques, Gear, Safety... |
| Rich Editor | Write rich content using TinyMCE editor. |
| Categorization | Manage articles by categories for easy searching. |

### 🏆 Gamification

| Badge Type | Example Condition |
|------------|-------------------|
| Activity | Join or organize 5/10/20 trips. |
| Contribution | Post 10 articles or 50 comments in the community. |
| Fitness | Accumulate 100km distance or 5000m altitude. |
| Exploration | Visit 10 different provinces. |
| Challenge | Complete a "Expert" difficulty trek. |

> The system automatically checks and awards badges when users meet the conditions.

### 🔧 Administration

| Feature | Description |
|---------|-------------|
| Dashboard | View overview stats: users, trips, posts, and analytical charts. |
| Trek Approval | Review user-contributed trails, approve or reject with reasons. |
| Trip Approval | Check content before allowing public member recruitment. |
| Post Approval | Moderate community content before display. |
| Report Handling | Receive and resolve violation reports from users. |

---

## Technologies

### Backend

| Technology | Version |
|------------|---------|
| Python | 3.8+ |
| Django | 4.2.23 |
| MySQL | 5.7+ |
| Pillow | 11.3.0 |

### Frontend

| Technology | Description |
|------------|-------------|
| Bootstrap 5 | Build responsive interfaces. |
| TinyMCE | Rich text editor for posts. |
| Font Awesome | Icons for UI components. |

---

## Installation

### Requirements
- Python 3.8 or higher
- MySQL 5.7 or higher

### Steps

```bash
# 1. Clone repository
git clone <repo_url>
cd trekking_web

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create database
mysql -u root -p
CREATE DATABASE trekking_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

# 5. Configure database in settings.py

# 6. Run migrations
python manage.py makemigrations
python manage.py migrate

# 7. Create admin account
python manage.py createsuperuser

# 8. Start server
python manage.py runserver
```

**Access:**
- Homepage: http://127.0.0.1:8000
- Admin Dashboard: http://127.0.0.1:8000/dashboard/

---

## Screenshots

### User Interface

| No. | Screen | Image | Description |
|:---:|--------|-------|-------------|
| 1 | Trek List | ![Trek List](docs/images/danhsachcungduong.png) | Advanced filters: Province, difficulty, length (km), time, and rating. Supports keyword search. |
| 2 | Trek Details | <img src="docs/images/chitiecd1.png" width="100%"><br><img src="docs/images/chitietcd2.png" width="100%"><br><img src="docs/images/chitietcd3.png" width="100%"><br><img src="docs/images/chitietcd4.png" width="100%"> | Displays terrain info, interactive map (GeoJSON), gallery, and multimedia review/rating system. |
| 3 | Trek Creation Form | <img src="docs/images/taocd1.png" width="100%"><br><img src="docs/images/taocd2.png" width="100%"><br><img src="docs/images/taocd3.png" width="100%"> | Detailed input interface with CKEditor/TinyMCE, integrated GeoJSON map upload, and suggested gear management. |
| 4 | Trip Hub | ![Trip Hub](docs/images/triphub.png) | Search trips by budget, duration, departure date. Filters for "Available spots only" and status (Upcoming, Recruiting). |
| 5 | Trip Details | <img src="docs/images/chitietchuyendi1.png" width="100%"><br><img src="docs/images/chitietchuyendi2.png" width="100%"><br><img src="docs/images/chitietchuyendi3.png" width="100%"> | Detailed itinerary (Timeline), member list, and join mechanism (Public/Private with invite code). |
| 6 | Trip Creation Form | <img src="docs/images/tạochuyendi1.png" width="100%"><br><img src="docs/images/taochuyendi2.png" width="100%"> | Optimal 2-step trip setup: Select template trek -> Fill info. Integrated **Itinerary Builder** tool allows dragging and dropping activities by day/hour. |
| 7 | Group Chat | ![Chat](docs/images/tinnhan.png) | Real-time chat system integrated within trips: messaging, file/photo sharing, and online member list. |
| 8 | Community Corner | <img src="docs/images/congdong.png" width="100%"> | List of news/sharing posts with Upvote, commenting, and author card (Avatar/Name) features. |
| 9 | Knowledge | <img src="docs/images/khokt.png" width="100%">| Library of guide articles (Skills, Gear) categorized by topic, displayed as Grid cards. |
| 10 | Personal Profile | ![Profile](docs/images/hosocanhan.png) | Overview page: History of trips, Badge collection (Gamification), Gear locker management, and Posted articles. |

### Admin Interface

| No. | Screen | Image | Description |
|:---:|--------|-------|-------------|
| 13 | Dashboard | ![Dashboard](docs/images/dashboard.png) | **Data Analytics Hub**: Displays key KPIs (User, Trip, Revenue) and actual growth charts. Supports decision making via BCG Matrix for trek quality and User Conversion Funnel. |
| 14 | Trek Approval | ![Approve Trek](docs/images/duyetcungduong.png) | **Management & Moderation**: Integrated Quick Filters help detect errors like missing photos, maps, or low ratings. Admins can quick-approve or request GeoJSON data edits directly. |
| 15 | Trip Approval | ![Approve Trip](docs/images/duyetchuyendi.png) | **Risk Control**: System automatically prioritizes trips needing approval and warns of risks (Ghost Trips, Departing Soon). Helps Admins focus on urgent cases or safety violations. |
| 16 | Post Approval | ![Approve Post](docs/images/quanlybaiviet.png) | **Community Moderation**: Allows Bulk Actions (Approve/Reject) for posts with an optimized interface. Integrated Media preview within the list speeds up moderation. |
| 17 | Multi-dimensional Analysis | ![Analytics](docs/images/thongkevabaocao.png) | **Detailed Analytics**: Detailed reporting system for each module: Users, Trips, Treks, and Content. Helps Admins grasp trends and operational efficiency of the entire platform. |
| 18 | User Management | ![User Mgmt](docs/images/quanlyuser.png) | **Account Administration**: User statistics (New/Active/Locked). Integrated filters by Role (Admin/Member) and Status. Supports viewing profile details (Interests, Gear), activity history, and performing Lock/Unlock or Delete actions. |
| 19 | Gamification System | ![Gamification](docs/images/gamefication.png) | **Badge Management**: Configure badge criteria and track user progress. System automatically awards badges based on real activity data (trips joined, posts contributed). |

---

## Project Structure

```
trekking_web/
├── accounts/          # Registration, login, and user profiles
├── treks/             # CRUD treks, ratings, media
├── trips/             # Create trips, manage members, chat
├── community/         # Community posts, comments, upvotes
├── articles/          # Knowledge articles (managed by admin)
├── knowledge/         # Knowledge display for users
├── gamification/      # Badges and reward logic
├── report_admin/      # Violation report handling
├── user_admin/        # User list management
├── core/              # Shared models: Province, Difficulty, Gear, Tags
├── templates/         # HTML templates
├── static/            # CSS, JavaScript, images
├── media/             # User uploaded files
└── requirements.txt   # Python dependencies list
```

---

## Development Team

- **Nguyen Thanh Huyen** - GitHub: [@Chizk23](https://github.com/Chizk23)
- **Tran Thi Phuong** - GitHub: [@PhuongTran2212](https://github.com/PhuongTran2212)

---

**⭐ If you find this project useful, give us a star!**
