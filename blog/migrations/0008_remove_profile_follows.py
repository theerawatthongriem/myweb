# Generated by Django 4.2 on 2023-06-15 02:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0007_rename_username_profile_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="follows",
        ),
    ]
