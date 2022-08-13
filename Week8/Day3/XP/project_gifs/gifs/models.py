from django.db import models
from django.urls import reverse

class Gif_model(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    uploader_name = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.title

def get_absolute_url(self):
    return reverse('show_gif', args = [self.id])




class Category_model(models.Model):
    name = models.CharField(max_length=100, unique=True)
    gifs = models.ManyToManyField(Gif_model, related_name='categories')

def __str__(self) :
    return self.name

def get_absolute_url(self):
    return reverse('show_category', args = [self.id])