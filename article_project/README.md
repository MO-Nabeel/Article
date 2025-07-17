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

## Requirements

- Python 3.8+
- Django 4.x
- Other dependencies listed in `requirements.txt`

## Usage

- To add, update, or delete articles, use the navigation links in the app after logging in.
- User registration and login are available from the main page.
- Static files (CSS, images) are managed in the `static/` directory.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Create a new Pull Request

## License

This project is licensed under the MIT License.

## Acknowledgements

- [Django Documentation](https://docs.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)

---
