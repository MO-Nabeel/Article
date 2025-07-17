# Article Project

This is a Django-based web application for managing articles and user registration.

## Project Structure

- `article_project/` - Main Django project settings and configuration.
- `articles/` - Django app for article management (models, views, forms, etc.).
- `registration/` - Django app for user registration and authentication.
- `static/` - Static files (CSS, images).
- `templates/` - HTML templates for the project.
- `db.sqlite3` - SQLite database file (ignored by git).
- `manage.py` - Django management script.

## Setup Instructions

1. **Clone the repository:**
   ```sh
   git clone <repo-url>
   cd article_project
   ```
2. **Create a virtual environment and activate it:**
   ```sh
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # or
   source venv/bin/activate  # On macOS/Linux
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Apply migrations:**
   ```sh
   python manage.py migrate
   ```
5. **Run the development server:**
   ```sh
   python manage.py runserver
   ```
6. **Access the app:**
   Open your browser and go to `http://127.0.0.1:8000/`

## Features
- Article CRUD (Create, Read, Update, Delete)
- User registration and login
- Custom forms and templates
- Static file management

## Notes
- The `db.sqlite3` file and other sensitive files are excluded from version control via `.gitignore`.
- For production, configure environment variables and use a production-ready database.

---
