from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    image = models.URLField(null=True)
    hobbies = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username

