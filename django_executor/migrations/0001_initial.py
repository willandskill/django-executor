# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('app_name', models.TextField(null=True)),
                ('command_name', models.TextField(null=True)),
                ('argv_raw', models.TextField(null=True)),
                ('stdout', models.TextField(null=True)),
                ('stderr', models.TextField(null=True)),
                ('started_at', models.DateTimeField()),
                ('ended_at', models.DateTimeField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]
