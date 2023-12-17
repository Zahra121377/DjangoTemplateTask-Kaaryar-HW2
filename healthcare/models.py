from django.db import models


# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=50)
    specialization = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to="images/doctor_profile_images/", blank=True, null=True)
    facebook_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name
