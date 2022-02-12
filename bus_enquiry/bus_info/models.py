from django.db import models

# Create your models here.
class Bus(models.Model):
    busid=models.IntegerField()
    bustype=models.CharField(max_length=30)
    source=models.CharField(max_length=50)
    destination=models.CharField(max_length=50)
    startingat=models.TimeField()
    willreachat=models.TimeField()
    stops=models.CharField(max_length=30)
    drivername=models.CharField(max_length=30)
    conductorname=models.CharField(max_length=30)
