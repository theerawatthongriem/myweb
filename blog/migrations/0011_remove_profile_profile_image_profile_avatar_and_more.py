# Generated by Django 4.2 on 2023-06-17 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0010_alter_datapredict_student_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="profile_image",
        ),
        migrations.AddField(
            model_name="profile",
            name="avatar",
            field=models.ImageField(default=1, upload_to="media"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="profile",
            name="bio",
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
