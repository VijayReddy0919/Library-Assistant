# Online Library Assistant

## Description
Online library Assistant built with Django. It provides a platform for managing books, users, and library operations efficiently.

## Features
- User authentication and authorization
- Admin panel for managing books, authors, and categories
- Student registration and book issuing
- Search functionality for books and registered users
- Dashboard for quick access to library operations

## Installation Instructions
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd olms
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up the database:
   - Update the database settings in `settings.py`.
   - Run migrations:
     ```bash
     python manage.py migrate
     ```

## Usage
1. Start the development server:
   ```bash
   python manage.py runserver
   ```
2. Access the application at `http://127.0.0.1:8000/`.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License.
