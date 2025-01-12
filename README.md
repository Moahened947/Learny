# Learny - Online Learning Platform

Learny is a modern, feature-rich online learning platform built with Django. It provides an intuitive interface for both learners and instructors to manage and access educational content.

## Features

- **Organized Learning Paths**: Content is structured into sections, courses, and lessons for clear progression
- **Preview System**: Free preview lessons available for each course
- **Responsive Design**: Beautiful, mobile-friendly interface with dark mode support
- **Progress Tracking**: Track your learning progress across courses
- **Interactive UI**: Modern interface with smooth transitions and intuitive navigation
- **Flexible Pricing**: Multiple subscription tiers with monthly and annual billing options

## Tech Stack

- **Backend**: Django 5.0
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: SQLite
- **UI Framework**: Bootstrap 5
- **Icons**: Font Awesome
- **Media Handling**: Django File Storage

## Installation

### Option 1: Traditional Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Learny.git
cd Learny
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Apply migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

### Option 2: Docker Setup

1. Make sure you have Docker and Docker Compose installed on your system.

2. Clone the repository:
```bash
git clone https://github.com/yourusername/Learny.git
cd Learny
```

3. Build and run the containers:
```bash
docker-compose up --build
```

4. In a new terminal, create a superuser:
```bash
docker-compose exec web python manage.py createsuperuser
```

The application will be available at:
- Local: http://localhost:8000
- Network: http://YOUR_IP:8000

### Docker Commands

- Start the application:
```bash
docker-compose up
```

- Stop the application:
```bash
docker-compose down
```

- View logs:
```bash
docker-compose logs
```

- Run migrations:
```bash
docker-compose exec web python manage.py migrate
```

- Create superuser:
```bash
docker-compose exec web python manage.py createsuperuser
```

- Collect static files:
```bash
docker-compose exec web python manage.py collectstatic
```

## Project Structure

```
Learny/
├── tutorials/              # Main application
│   ├── migrations/        # Database migrations
│   ├── templates/        # HTML templates
│   ├── static/          # Static files (CSS, JS, images)
│   ├── models.py        # Database models
│   ├── views.py         # View logic
│   └── urls.py          # URL routing
├── manage.py            # Django management script
└── requirements.txt     # Project dependencies
```

## Usage

1. **Admin Interface**
   - Access the admin panel at `/admin`
   - Create sections, courses, and lessons
   - Manage user accounts and permissions

2. **Content Management**
   - Organize content into sections
   - Create courses within sections
   - Add lessons to courses
   - Mark lessons as preview-able

3. **User Features**
   - Browse available courses
   - Watch preview lessons
   - Track learning progress
   - Access premium content (with subscription)

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Mohaned M Tohami

## Support

For support, email mohanedtohami@gmail.com or open an issue in the repository.

---

Made with ❤️ by Mohaned M Tohami
