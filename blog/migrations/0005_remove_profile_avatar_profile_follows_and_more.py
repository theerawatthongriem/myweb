# Generated by Django 4.2 on 2023-06-14 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_remove_profile_user_alter_profile_avatar"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="avatar",
        ),
        migrations.AddField(
            model_name="profile",
            name="follows",
            field=models.ManyToManyField(
                blank=True, related_name="followed_by", to="blog.profile"
            ),
        ),
        migrations.AddField(
            model_name="profile",
            name="profile_image",
            field=models.ImageField(blank=True, null=True, upload_to="media/"),
        ),
    ]
