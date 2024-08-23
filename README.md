# Coding Test App

## Overview

The Coding Quiz App is a Django-based web application that allows users to participate in coding challenges while being recorded on camera. This app is designed to simulate a coding interview environment, helping users practice their coding skills under timed conditions.


## Structure

```

├── coding_app/
│   ├── requirements.txt
│   ├── db.sqlite3
│   ├── README.md
│   ├── .env
│   ├── manage.py
│   ├── coding_app/
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── app1/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── apps.py
│   │   ├── admin.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   │   ├── templates/
│   │   │   ├── registration/
│   │   │   │   └── login.html
│   │   │   ├── app1/
│   │   │   │   ├── interface.html
│   │   │   │   ├── base.html
│   │   │   │   └── results.html
│   │   ├── fixtures/
│   │   │   └── default_questions.json


## Features

- User authentication
- Camera integration for recording users during the quiz
- 10 coding questions presented one at a time
- Timed responses for each question
- Ability to save draft responses
- Final quiz submission
- Results page showing all responses

## Technologies Used

- Backend: Django
- Frontend: HTML, CSS, JavaScript
- Styling: Bootstrap
- Database: SQLite (default Django database)

## Prerequisites

- Python 3.8+
- pip
- Virtual environment (recommended)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/coding-quiz-app.git
   cd coding-quiz-app
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```
   python manage.py migrate
   ```

5. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

7. Access the application at `http://localhost:8000`

## Usage

1. Log in to the application
2. Start a new quiz session
3. Allow camera access when prompted
4. Answer each coding question within the time limit
5. Use the "Save Draft" button to save your progress
6. Move to the next question using the "Next Question" button
7. Submit your quiz when all questions are answered
8. View your results on the results page

## Admin Interface

Access the admin interface at `http://localhost:8000/admin/` to manage questions, user sessions, and responses.

## Customization

- To modify the number of questions or time limits, update the `Question` model and related views
- Customize the appearance by editing the Bootstrap classes in the HTML templates

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- Django framework
- Bootstrap for responsive design
- All contributors who participate in this project

## Support

If you encounter any problems or have any questions, please open an issue in the GitHub repository.
