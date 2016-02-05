from __future__ import absolute_import, unicode_literals
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _
from django_executor import settings as de_settings


class ExecutorConfig(AppConfig):
    name = 'django_executor'
    verbose_name = _("Django Executor")

    def ready(self):
        de_settings.patch_all()