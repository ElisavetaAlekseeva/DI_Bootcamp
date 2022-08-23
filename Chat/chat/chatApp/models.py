from email.mime import image
from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='profile_images', default='blankprofilephoto.jpeg', null=True)
    hobbies = models.CharField(max_length=200, null=True)
    location = models.CharField(max_length=100, blank=True)
    friends = models.ManyToManyField('Friend', related_name='users_friends')

    def __str__(self) -> str:
        return self.name


class Friend(models.Model):
    profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.profile.name


class Chat(models.Model):
    body = models.TextField()
    sender = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='receiver')
    message_seen = models.BooleanField(default=False)

    def __str__(self) -> str:
            return self.body
