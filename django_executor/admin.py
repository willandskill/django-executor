from django.contrib import admin
from settings import CONFIG
from models import Log


class LogAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'app_name', 'command_name', 'started_at', 'ended_at',)


if not CONFIG['HIDE_FROM_DJANGO_ADMIN']:
    admin.site.register(Log, LogAdmin)