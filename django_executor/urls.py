from django.conf.urls import patterns, url
from django import get_version
import views


if get_version() < 1.9:
    urlpatterns = patterns('',
    url(r'^django-executor/run-management-command/', views.RunManagementCommandView.as_view(), name='run-management-command'),
    url(r'^django-executor/', views.ManagementCommandListView.as_view(), name='index'),
)
else:
    urlpatterns = [
        url(r'^django-executor/run-management-command/', views.RunManagementCommandView.as_view(), name='run-management-command'),
        url(r'^django-executor/', views.ManagementCommandListView.as_view(), name='index'),
    ]