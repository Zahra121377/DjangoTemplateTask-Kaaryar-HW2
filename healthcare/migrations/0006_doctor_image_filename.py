# Generated by Django 4.2.7 on 2023-12-18 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("healthcare", "0005_remove_doctor_image_filename"),
    ]

    operations = [
        migrations.AddField(
            model_name="doctor",
            name="image_filename",
            field=models.CharField(default="d2.png", max_length=255),
        ),
    ]