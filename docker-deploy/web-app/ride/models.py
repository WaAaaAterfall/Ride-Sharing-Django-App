from django.db import models

from django.contrib.auth.models import User 

from django.urls import reverse

# Create your models here.

class DriverVehicle(models.Model):
    driver = models.OneToOneField(User, on_delete=models.CASCADE)
    plate = models.CharField(default='000',max_length=50)
    capacity = models.IntegerField(default=4)
    vehicle_type = models.CharField(default='SEDAN',max_length=100)
    special_info = models.CharField(default='', max_length=200)

    def __str__(self):
        return f'{self.driver.username} Vehicle'

class RideOrder(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    destination = models.CharField(max_length=100)
    arrive_date = models.DateTimeField(help_text='Format: 2023-02-01 12:00')
    passenger_num = models.PositiveIntegerField(default=1)
    sharable = models.BooleanField()
    vehicle_type = models.CharField(default='None',max_length=100, blank=True)
    status = models.CharField(default='open', max_length=20)
    sharer = models.ManyToManyField(User, blank=True, related_name = 'sharer')
    driver = models.ForeignKey(DriverVehicle, blank=True, null=True, on_delete=models.CASCADE)
    special_request = models.CharField(max_length=400, default='', blank=True)

    def __str__ (self):
        return "{" + self.owner + self.addr + "}" 
