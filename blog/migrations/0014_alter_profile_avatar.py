# Generated by Django 4.2 on 2023-07-04 08:22

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0013_alter_profile_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="avatar",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="media",
                verbose_name=django.contrib.auth.models.User,
            ),
        ),
    ]
