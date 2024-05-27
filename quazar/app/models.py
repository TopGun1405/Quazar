from django.db import models


# Create your models here.
class Weather(models.Model):
    location = models.CharField(max_length=100)
    date_time = models.DateTimeField()

    temperature = models.FloatField()
    humidity = models.FloatField()
    wind_speed = models.FloatField()
    wind_direction = models.CharField()
    precipitation = models.IntegerField()
    pressure = models.IntegerField()
    weather_condition = models.CharField()
