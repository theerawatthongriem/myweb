# Generated by Django 4.2 on 2023-07-05 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0018_branch"),
    ]

    operations = [
        migrations.AlterField(
            model_name="branch",
            name="branch_name",
            field=models.OneToOneField(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="blog.faculty",
            ),
            preserve_default=False,
        ),
    ]