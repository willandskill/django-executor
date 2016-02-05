# django-executor
Manage your django management commands easily within your browser

## Installation
* ```pip install django-executor```
* Add "django_executor" to INSTALLED_APPS
* ```./manage.py migrate django_executor```

## Manage management commands
* Open /django-executor/ in browser

## Configuration
Add the default DJANGO_EXECUTOR_CONFIG and modify the following attributes:

```
DJANGO_EXECUTOR_CONFIG = {
    'HIDE_FROM_DJANGO_ADMIN': False,  # Hides Log model from django admin
    'HIDE_DJANGO_MANAGEMENT_COMMANDS': True,  # Hides all django.* related management commands
    'EXCLUDED_APPS': []  # Add apps your want to exclude
}
```

### Tested on Django 1.8.6 > 1.9.1