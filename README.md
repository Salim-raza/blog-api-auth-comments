# DRF Blog API

A Blog Backend API built with Django Rest Framework including authentication, posts, categories and comments.

---

## 🚀 Features

### 🔐 Authentication
- User registration
- User login
- Change password# DRF Blog API

A Blog Backend API built with Django Rest Framework including authentication, posts, comments and limited category creation.

---

## 🚀 Features

### 🔐 Authentication
- User registration
- User login
- Change password
- Reset password

### 📝 Posts
- Create post
- Read all posts
- Read single post
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
- Database: PostgreSQL / SQLite
- Authentication: JWT / Session Auth

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/drf-blog-api.git
cd drf-blog-api
python -m venv venv
source venv/bin/activate
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
