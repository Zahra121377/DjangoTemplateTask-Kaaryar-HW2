# Generated by Django 4.2.7 on 2023-12-18 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("healthcare", "0004_doctor_image_filename"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="doctor",
            name="image_filename",
        ),
    ]
