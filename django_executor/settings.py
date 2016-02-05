from django.conf import settings
from importlib import import_module
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Default configuration
DEFAULT_CONFIG = {
    'HIDE_FROM_DJANGO_ADMIN': False,
    'HIDE_DJANGO_MANAGEMENT_COMMANDS': True,
    'EXCLUDED_APPS': []
}

# Update CONFIG with user added configuration
CONFIG = DEFAULT_CONFIG.copy()
if hasattr(settings, 'DJANGO_EXECUTOR_CONFIG'):
    for key, value in settings.DJANGO_EXECUTOR_CONFIG.iteritems():
        CONFIG[key] = value


# Patch app urls with root urlconf
def patch_root_urlconf():
    from django.core.urlresolvers import clear_url_caches, reverse, NoReverseMatch
    import urls

    try:
        reverse('django_executor:index')
    except NoReverseMatch:
        urlconf_module = import_module(settings.ROOT_URLCONF)
        urlconf_module.urlpatterns = urls.urlpatterns + urlconf_module.urlpatterns
        clear_url_caches()


def patch_staticfiles():
    settings.STATICFILES_DIRS += (
        os.path.join(BASE_DIR, 'django_executor', 'staticfiles'),
    )


# Add DJANGO_EXECUTOR_CONFIG to root settings
def patch_settings():
    setattr(settings, 'DJANGO_EXECUTOR_CONFIG', CONFIG)


def patch_all():
    patch_root_urlconf()
    patch_settings()
    patch_staticfiles()