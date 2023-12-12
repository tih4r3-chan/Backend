from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile(models.Model):
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=500)
    password = models.CharField(max_length=200)
    password_confirmation = models.CharField(max_length=200)

    def __str__(self):
        return self.username
