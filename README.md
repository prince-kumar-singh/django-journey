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

### 🛠️ Next Steps

1. **Extend Templates**: Add templates for the `about` and `contact` pages.
2. **Dynamic Content**: Pass dynamic data to templates using Django's context.
3. **Forms**: Implement forms for user input.
4. **Testing**: Write unit tests to ensure the application works as expected.
5. **Deployment**: Deploy the project to a hosting platform like Heroku or AWS.

Stay tuned for more updates as I continue my Django journey!


