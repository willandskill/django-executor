# Generated by Django 2.2.11 on 2020-05-21 05:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_executor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]