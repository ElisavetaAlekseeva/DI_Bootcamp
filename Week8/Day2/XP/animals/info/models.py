from django.db import models

# Create your models here.
class Family(models.Model):

    name = models.CharField(max_length=80)

    def __str__(self) -> str:
        return self.name

class Animal(models.Model):

    name = models.CharField(max_length=50,null=True)
    legs = models.IntegerField()
    weight = models.IntegerField()
    height = models.IntegerField()
    speed = models.IntegerField()
    family = models.ForeignKey(Family, on_delete = models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.name
