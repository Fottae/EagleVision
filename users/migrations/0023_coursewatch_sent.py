# Generated by Django 4.2.7 on 2023-12-04 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0022_remove_course_offering_id_remove_course_sections"),
    ]

    operations = [
        migrations.AddField(
            model_name="coursewatch",
            name="sent",
            field=models.BooleanField(default=False),
        ),
    ]
