from django.db import models

# Create your models here.
class Timeslot(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    discription = models.TextField()