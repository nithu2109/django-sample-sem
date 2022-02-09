from django.db import models

# Create your models here.
class Calorie(models.Model):
    foodid = models.IntegerField()
    fooditem = models.CharField(max_length=50)
    calorie=models.IntegerField()
