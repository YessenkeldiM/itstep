from django.db import models


class UserProfile(models.Model):
    cv = models.FileField(upload_to='profile_cv')
    photo = models.ImageField(upload_to='profile_photo')

# Create your models here.
