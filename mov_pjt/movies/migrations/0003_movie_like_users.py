# Generated by Django 3.2.13 on 2022-10-12 07:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0002_auto_20221012_0246'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='like_users',
            field=models.ManyToManyField(related_name='likes_movies', to=settings.AUTH_USER_MODEL),
        ),
    ]
