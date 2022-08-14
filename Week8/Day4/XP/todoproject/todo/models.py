from email.mime import image
from django.db import models
from django.urls import reverse
# Create your models here.

class Category_mod(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.URLField()

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('category', args=[self.id])



class ToDO_mod(models.Model):

    title = models.CharField(max_length=100)
    details = models.TextField()
    has_been_done = models.BooleanField(default=False)
    date_creation = models.DateField(auto_now_add=True)
    date_completion = models.DateField(null=True)
    deadline_date = models.DateField()
    category = models.ForeignKey(Category_mod, related_name='todos', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title