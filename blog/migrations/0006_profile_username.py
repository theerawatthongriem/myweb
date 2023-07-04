# Generated by Django 4.2 on 2023-06-15 02:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blog", "0005_remove_profile_avatar_profile_follows_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="username",
            field=models.OneToOneField(
                default=2,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
