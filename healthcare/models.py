from django.db import models


# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=50)
    specialization = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to="doctor_profile_images/")
    facebook_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
