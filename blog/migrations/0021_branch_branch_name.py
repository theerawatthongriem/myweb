# Generated by Django 4.2 on 2023-07-06 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0020_remove_branch_branch_name_remove_faculty_branch_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="branch",
            name="branch_name",
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]