# 🐍 Django Journey

Welcome to my **Django Journey**!  
This repository is both a learning log and a guide for anyone interested in learning Django — a high-level Python web framework that promotes rapid development and clean, pragmatic design.

---

## 📖 About

This repository is a personal learning path to mastering Django.  
Each commit represents something new I've learned — from project setup to building real apps.  
The goal is to make this a helpful and beginner-friendly space for others too!

---

## ⚙️ Setup Instructions (using `uv` + virtualenv)

```bash
# 1. Clone this repo
git clone https://github.com/prince-kumar-singh/django-journey.git
cd django-journey

# 2. Create a virtual environment (optional but recommended)
python -m venv .venv

# 3. Activate the virtual environment
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate

# 4. Install dependencies using uv (instead of pip)
uv pip install django

# 5. Run the Django development server
python manage.py runserver
```

---

### ✅ (April 5, 2025)
**Created Views for `home`, `about`, and `contact`**

In the `django-journey/Django/Django/views.py` file, I created three basic views that return plain text responses. These serve as the foundation for adding templates and routing later.

#### 📄 `Django/Django/views.py`
```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, world. You're at the home page.")

def about(request):
    return HttpResponse("Hello, world. You're at the about page.")

def contact(request):
    return HttpResponse("Hello, world. You're at the contact page.")
```

---

### 🔗 URL Configuration

The views are connected to URLs in the `Django/Django/urls.py` file. Currently, the project includes the default admin route. You can extend it to include the `home`, `about`, and `contact` views.

#### 📄 `Django/Django/urls.py`
```python
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
```


**Added Templates and Static Files**

1. Updated the `home` view to render an HTML template instead of returning plain text.
2. Added a static CSS file to style the `home` page.
3. Configured the `settings.py` file to include the `templates` and `static` directories.

#### 📄 `Django/Django/views.py`
```python
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # Render the home page using an HTML template
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse("Hello, world. You're at the about page.")

def contact(request):
    return HttpResponse("Hello, world. You're at the contact page.")
```

#### 📄 `Django/templates/website/index.html`
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Django</title>
    <link rel="stylesheet" href="{% static 'style.css' %}">
</head>
<body>
    <h1>Welcome to Django Journey</h1>
</body>
</html>
```

#### 📄 `Django/static/style.css`
```css
body {
    background-color: #08153d;
    color: #ffffff;
}

h1 {
    text-align: center;
    font-size: 2em;
}
```

#### 📄 `Django/Django/settings.py`
```python
# Added the templates directory
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],  # Added this line
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Added static files configuration
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```

---

### ✅ (April 6, 2025)
**Created a New App: `firstapp`**

1. Created a new app named `firstapp` using the following command:
   ```bash
   python manage.py startapp firstapp
   ```

2. Added a new view `all_firstapp` that renders an HTML template.
3. Configured the app's URLs and connected it to the main project.

#### 📄 `Django/firstapp/views.py`
```python
from django.shortcuts import render

def all_firstapp(request):
    return render(request, 'firstapp/all_firstapp.html', {})
```

#### 📄 `Django/firstapp/templates/firstapp/all_firstapp.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>All firstapp</title>
</head>
<body>
    <h1>All types of firstapp</h1>
</body>
</html>
```

#### 📄 `Django/firstapp/urls.py`
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_firstapp, name='all_firstapp'),
]
```

#### 📄 `Django/Django/urls.py`
```python
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('firstapp/', include('firstapp.urls')),
]
```

#### 📄 `Django/Django/settings.py`
```python
# Added the new app to INSTALLED_APPS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'firstapp',  # Added this line
]
```

---
**Enhanced `firstapp` with Template Inheritance**

1. Updated the `all_firstapp` view to use a base template (`layout.html`) for template inheritance.
2. Created a `layout.html` file to serve as the base template for all pages.

#### 📄 `Django/firstapp/templates/firstapp/all_firstapp.html`
```html
{% extends "layout.html" %}

{% block title %}
Firstapp Page
{% endblock %}
{% block content %}
    <h1>All firstapp</h1>
{% endblock %}
```

#### 📄 `Django/templates/layout.html`
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>
        {% block title %}
        Default Title
        {% endblock %}
    </title>
    <link rel="stylesheet" href="{% static 'style.css' %}">
</head>
<body>
    <nav>This is our Navbar</nav>
    {% block content %}{% endblock %}
</body>
</html>
```

---

### ✅ (April 9, 2025)
**Integrated Tailwind CSS with Django**

To integrate Tailwind CSS with Django, follow the official installation guide:  
[https://django-tailwind.readthedocs.io/en/latest/installation.html](https://django-tailwind.readthedocs.io/en/latest/installation.html)

#### 📄 Key Steps:
#### 📄 Key Steps: Tailwind CSS Setup in Django

- 📦 Install `django-tailwind`:
  ```bash
  python -m pip install django-tailwind
  ```

- 💻 (Optional) For live reload support:
  ```bash
  python -m pip install 'django-tailwind[reload]'
  ```

- 🧪 (Optional) Install latest dev version:
  ```bash
  python -m pip install git+https://github.com/timonweb/django-tailwind.git
  ```

---

- ⚙️ Add to `INSTALLED_APPS` in `settings.py`:
  ```python
  INSTALLED_APPS = [
    'tailwind',
  ]
  ```

- 🚀 Initialize Tailwind-compatible app:
  ```bash
  python manage.py tailwind init
  ```

- 🌀 (Optional) For Tailwind v3:
  ```bash
  python manage.py tailwind init --tailwind-version 3
  ```

- ➕ Add your new app (e.g., `theme`) to `INSTALLED_APPS`:
  ```python
  INSTALLED_APPS = [
    'tailwind',
    'theme',
  ]
  ```

- 🏷️ Register Tailwind app name in `settings.py`:
  ```python
  TAILWIND_APP_NAME = 'theme'
  ```

---

- 📁 Install Tailwind CSS dependencies:
  ```bash
  python manage.py tailwind install
  ```

- 🛑 (Optional) Skip package-lock:
  ```bash
  python manage.py tailwind install --no-package-lock
  ```

---

- 🧩 Add Tailwind to your `base.html`:
  ```html
  {% load static tailwind_tags %}
  <head>
    ...
    {% tailwind_css %}
    ...
  </head>
  ```

---

- 🔄 Add live reload support (Optional):

  - Add to `INSTALLED_APPS`:
    ```python
    INSTALLED_APPS = [
      'tailwind',
      'theme',
      'django_browser_reload',
    ]
    ```

  - Add middleware in `MIDDLEWARE`:
    ```python
    MIDDLEWARE = [
      ...,
      "django_browser_reload.middleware.BrowserReloadMiddleware",
    ]
    ```

  - Include reload URLs in `urls.py`:
    ```python
    from django.urls import include, path

    urlpatterns = [
      ...,
      path("__reload__/", include("django_browser_reload.urls")),
    ]
    ```

---

- 🚴‍♂️ Start Tailwind in development mode:
  ```bash
  python manage.py tailwind start
  ```

5. Run the Django development server in a separate terminal:
   ```bash
   python manage.py runserver
   ```

---

### 📄 key changes:

#### 📄 `Django/templates/layout.html`
```html
{% load static tailwind_tags %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>
        {% block title %}
        Default Title
        {% endblock %}
    </title>
    {% tailwind_css %}
</head>
<body>
    <nav class="bg-gray-800 text-white p-4">This is our Navbar</nav>
    <div class="container mx-auto mt-4">
        {% block content %}{% endblock %}
    </div>
</body>
</html>
```

#### 📄 `Django/templates/website/index.html`
```html
{% extends "layout.html" %}

{% block title %}
Home Page
{% endblock %}
{% block content %}
    <h1 class="text-3xl font-bold text-blue-600 bg-yellow-200 p-4 rounded-lg">Django | Home page</h1>
{% endblock %}
```

#### 📄 `Django/theme/static_src/src/styles.css`
```css
@import "tailwindcss";
```

#### 📄 `Django/Django/settings.py`
```python
# Added Tailwind CSS integration
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'firstapp',
    'tailwind',
    'theme',  # Added this line
]

TAILWIND_APP_NAME = 'theme'
```

---

**Set Up Django Admin**

To manage your project through the Django admin interface, follow these steps:

#### 📄 Required Terminal Commands:
1. Apply migrations to set up the database:
   ```bash
   python manage.py migrate
   ```

2. Create a superuser for the Django admin:
   ```bash
   python manage.py createsuperuser
   ```
   - You will be prompted to enter a username, email, and password for the superuser.

3. If you need to change the password of an existing user:
   ```bash
   python manage.py changepassword <username>
   ```

4. Start the development server to access the admin interface:
   ```bash
   python manage.py runserver
   ```

5. Visit the Django admin interface in your browser:
   ```
   http://127.0.0.1:8000/admin/
   ```

---

### 📄 Updated `urls.py` to Include Admin Interface

The Django admin interface is enabled by default. The following line in `urls.py` ensures that the admin interface is accessible:

#### 📄 `Django/Django/urls.py`
```python
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin interface
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('firstapp/', include('firstapp.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
]
```

---

### ✅ (April 10, 2025)
**Enhanced `firstapp` with Models, Admin, and Dynamic Views**

1. Created a model `firstappVarity` in the `firstapp` app to store app details.
2. Registered the model in the Django admin interface.
3. Added dynamic views to display all apps and individual app details.
4. Updated templates to display data dynamically.
5. Configured media files to handle image uploads.

---

#### 📄 Required Terminal Commands:
1. Apply migrations to create the database tables for the new model:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

2. Create a superuser for the Django admin interface:
   ```bash
   python manage.py createsuperuser
   ```

3. Start the development server:
   ```bash
   python manage.py runserver
   ```

---

### 📄 Key Changes:

#### 📄 `Django/firstapp/models.py`
```python
from django.db import models
from django.utils import timezone

class firstappVarity(models.Model):
    APP_CHOICE = [
        ('C', 'commercial'),
        ('P', 'personal'),
        ('E', 'enterprise'),
        ('B', 'business'),
        ('S', 'startup'),
        ('O', 'other'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=APP_CHOICE, default='C')
    description = models.TextField(default='')

    def __str__(self):
        return self.name
```

---

#### 📄 `Django/firstapp/admin.py`
```python
from django.contrib import admin
from .models import firstappVarity

# Register your models here.
admin.site.register(firstappVarity)
```

---

#### 📄 `Django/firstapp/views.py`
```python
from django.shortcuts import render, get_object_or_404
from .models import firstappVarity

def all_firstapp(request):
    apps = firstappVarity.objects.all()
    return render(request, 'firstapp/all_firstapp.html', {"apps": apps})

def app_detail(request, app_id):
    app = get_object_or_404(firstappVarity, pk=app_id)
    return render(request, 'firstapp/app_details.html', {"app": app})
```

---

#### 📄 `Django/firstapp/urls.py`
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_firstapp, name='all_firstapp'),
    path('<int:app_id>/', views.app_detail, name='app_details'),
]
```

---

#### 📄 `Django/firstapp/templates/firstapp/all_firstapp.html`
```html
{% extends "layout.html" %}

{% block title %}
Firstapp Page
{% endblock %}
{% block content %}
    <h1>All Firstapp</h1>

    <div class="grid grid-cols-3 gap-4">
        {% for app in apps %}
            <div class="bg-blue-800 p-5 rounded">
                <img class="rounded" src="{{ app.image.url }}" alt="{{ app.name }}">
                <h3 class="text-2xl font-bold">{{ app.name }}</h3>
                <a href="{% url 'app_details' app.id %}">
                    <button
                        class="inline-flex items-center w-full justify-center px-4 py-2 border border-transparent text-sm font-medium bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded transition duration-300 ease-in-out">
                        View Details
                    </button>
                </a>
            </div>
        {% endfor %}
    </div>
{% endblock %}
```

---

#### 📄 `Django/firstapp/templates/firstapp/app_details.html`
```html
{% extends "layout.html" %}

{% block title %}
App Detail Page
{% endblock %}
{% block content %}
    <h1>App Details</h1>
    <h3>{{ app.name }}</h3>
    <p>{{ app.description }}</p>
    <img src="{{ app.image.url }}" alt="{{ app.name }}">
{% endblock %}
```

---

#### 📄 `Django/Django/settings.py`
```python
# Added media files configuration
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

---

#### 📄 `Django/Django/urls.py`
```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('firstapp/', include('firstapp.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---


