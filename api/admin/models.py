from django.db import models

# Create your models here.
class Event(models.Model):
    Event_id = models.CharField(max_length=15)
    Name=models.CharField(max_length=50)
    Image=models.ImageField()
    Location=models.CharField(max_length=15)
    Date=models.DateField()
    Time=models.TimeField()
    time_posted = models.DateTimeField(auto_now=True)
    Description=models.CharField(max_length=400)


    