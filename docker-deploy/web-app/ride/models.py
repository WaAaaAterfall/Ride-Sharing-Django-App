from django.db import models

from django.contrib.auth.models import User 

from django.urls import reverse

# Create your models here.

class RideOrder(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    addr = models.CharField(max_length=100)
    arrive_date = models.DateTimeField(help_text='Format: 2020-01-01 12:00')
    passenger_num = models.PositiveIntegerField(default=1)
    remaining_passenger_num = models.IntegerField(default=0)
    sharable = models.BooleanField()
    max_share_num = models.PositiveIntegerField(help_text='If you do not want to share please choose 0', default=0)
    #required_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='--')
    required_special = models.CharField(max_length=400, blank=True)
    status = models.CharField(default='open', max_length=20)
    share_name = models.CharField(default='', max_length=50, blank=True)
    share_num = models.PositiveIntegerField(default=0)
    driver_name = models.CharField(default='', max_length=50, blank=True)
    driver_license = models.CharField(default='', max_length=50, blank=True)

    def __str__ (self):
        return "{" + self.owner + self.addr + "}"

    # def get_absolute_url(self):
    #     return reverse('rideinfo')

class Driver(models.Model):
    driver = models.OneToOneField(User, on_delete=models.CASCADE)
    plate = models.CharField(default='000',max_length=50)
    capacity = models.IntegerField(default=4)
    Vtype = models.CharField(default='SEDAN',max_length=100)
    brand = models.CharField(default='', max_length=100)
    special_info = models.CharField(default='', max_length=200)

    def __str__(self):
        return f'{self.driver.username} Vehicle'
