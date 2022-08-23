from django.contrib import admin
from .models import UserProfile, Friend, Chat
# Register your models here.

admin.site.register([UserProfile, Friend, Chat])