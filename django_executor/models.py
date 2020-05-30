from django.db import models
from django.conf import settings


class Log(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,
                             on_delete=models.SET_NULL)
    app_name = models.TextField(null=True)
    command_name = models.TextField(null=True)
    argv_raw = models.TextField(null=True)
    stdout = models.TextField(null=True)
    stderr = models.TextField(null=True)

    started_at = models.DateTimeField()
    ended_at = models.DateTimeField()

    def __unicode__(self):
        return u'{} {}'.format(self.app_name, self.command_name)
