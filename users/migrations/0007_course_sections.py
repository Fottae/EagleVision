# Generated by Django 4.2.6 on 2023-11-22 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0006_course_offering_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="sections",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
