# DRF Blog API

A Blog Backend API built with Django Rest Framework including authentication, posts, comments and limited category creation.

---

## 🚀 Features

### 🔐 Authentication
- User registration
- User login
- Send OTP
- Change password
- Reset password

### 📝 Posts
- Create post
- Read all posts (paginated)
- Read single user posts
- Update post
- Delete post
- Search posts

### 🗂 Categories
- Create category only

### 💬 Comments
- Add comment on post
- Update comment
- Delete comment
- Get comments by post

---

## 🛠 Tech Stack

- Backend: Django
- API: Django Rest Framework (DRF)
- Database: SQLite
- Authentication: JWT / Session Auth

---

## 📌 API Endpoints

### 🔐 Authentication

| Method | Endpoint | Description | Auth |
|--------|----------|-------------|-------|
| POST | /api/v1/account/signup/ | Register new user | ❌ |
| POST | /api/v1/account/signin/ | Login user | ❌ |
| POST | /api/v1/account/send_otp/ | Send OTP | ❌ |
| POST | /api/v1/account/change_password/ | Change password | ✅ |
| POST | /api/v1/account/reset_password/ | Reset password | ❌ |

---

### 📝 Posts

| Method | Endpoint | Description | Auth |
|--------|----------|-------------|-------|
| GET | /api/v1/blogpost/read_post/?page=1 | Get all posts | ❌ |
| GET | /api/v1/blogpost/user_post/ | Get logged-in user posts | ✅ |
| GET | /api/v1/blogpost/search/?q=python | Search posts | ❌ |
| POST | /api/v1/blogpost/create_post/ | Create post | ✅ |
| PATCH | /api/v1/blogpost/update_post/{post_id}/ | Update post | ✅ |
| DELETE | /api/v1/blogpost/delete_post/{post_id}/ | Delete post | ✅ |

---

### 🗂 Categories

| Method | Endpoint | Description | Auth |
|--------|----------|-------------|-------|
| POST | /api/v1/blogpost/create_category/ | Create category | ✅ |

---

### 💬 Comments

| Method | Endpoint | Description | Auth |
|--------|----------|-------------|-------|
| GET | /api/v1/blogpost/comment_read/{post_id}/ | Get comments by post | ❌ |
| POST | /api/v1/blogpost/comment/{post_id}/ | Add comment | ✅ |
| PUT | /api/v1/blogpost/comment_edit/{comment_id}/ | Update comment | ✅ |
| DELETE | /api/v1/blogpost/comment_delete/{comment_id}/ | Delete comment | ✅ |

---

## ⚙️ Installation (Windows)

```bash
git clone https://github.com/Salim-raza/blog-api-auth-comments.git
cd drf-blog-api
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
