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
    friends = models.ManyToManyField('UserProfile', related_name='users_friends', default='')

    def __str__(self) -> str:
        return self.name


class Friend(models.Model):
    profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.profile.name

class FriendRequest(models.Model):
    sender = models.ForeignKey(UserProfile, related_name='sender', on_delete=models.CASCADE)
    receiver = models.ForeignKey(UserProfile, related_name='receiver', on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return "From {}, to {}".format(self.sender.username, self.receiver.username)


class Chat(models.Model):
    body = models.TextField()
    sender = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='chat_sender')
    receiver = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='chat_receiver')
    message_seen = models.BooleanField(default=False)

    def __str__(self) -> str:
            return self.body


