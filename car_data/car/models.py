from django.db import models

# Create your models here.
class CarData(models.Model):
    temp = models.IntegerField()
    humidity = models.FloatField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    image_ip = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)

