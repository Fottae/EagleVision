# Generated by Django 4.2.6 on 2023-12-01 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_remove_course_offering_id_remove_course_sections'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='credit_option',
            field=models.FloatField(default=0),
        ),
    ]