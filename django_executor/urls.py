from django.conf.urls import url
from django import get_version
from distutils.version import StrictVersion

try:
    from django.conf.urls import patterns
except ImportError:
    patterns = None

from . import views


if StrictVersion(get_version()).version < (1, 9, 0):
    urlpatterns = patterns('',
    url(r'^django-executor/run-management-command/', views.RunManagementCommandView.as_view(), name='run-management-command'),
    url(r'^django-executor/', views.ManagementCommandListView.as_view(), name='index'),
)
else:
    urlpatterns = [
        url(r'^django-executor/run-management-command/', views.RunManagementCommandView.as_view(), name='run-management-command'),
        url(r'^django-executor/', views.ManagementCommandListView.as_view(), name='index'),
    ]