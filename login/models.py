from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile2(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.username
