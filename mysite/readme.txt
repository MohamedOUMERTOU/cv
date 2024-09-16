/mysite/                  # Root directory of the project
    ├── mycv/             # Main application (your portfolio app)
    │   ├── migrations/   # Database migration files
    │   ├── templates/    # HTML templates folder
    │   │   └── mycv/     # Templates specific to the mycv app
    │   │       ├── base.html            # Base template for layout
    │   │       ├── index.html           # Homepage template
    │   │       ├── portfolio.html       # Portfolio page template
    │   │       ├── project_detail.html  # Individual project details
    │   │       └── contact.html         # Contact page template
    │   ├── static/       # Static files (CSS, JavaScript, images)
    │   │   ├── css/
    │   │   │   └── styles.css           # CSS file for styling
    │   │   ├── js/
    │   │   │   └── scripts.js           # JavaScript file
    │   │   └── images/                  # Image assets
    │   ├── admin.py       # Django admin configuration
    │   ├── apps.py        # App configuration
    │   ├── models.py      # Database models
    │   ├── forms.py       # Django forms for handling input
    │   ├── urls.py        # App-specific URL configuration
    │   ├── views.py       # Views for handling requests and responses
    │   └── tests.py       # Tests for the app
    ├── mysite/            # Main Django project folder
    │   ├── settings.py    # Main settings file
    │   ├── urls.py        # Project-wide URL configuration
    │   ├── wsgi.py        # WSGI configuration for deployment
    │   └── asgi.py        # ASGI configuration for asynchronous support
    ├── manage.py          # Django management script
    ├── db.sqlite3         # SQLite database (or link to your DB setup)
    └── requirements.txt   # Project dependencies


activate env python 
cv/scripts/activate