from django.db import models

# Create your models here.
class menuItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.ImageField



class Reservation(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    guest_count = models.IntegerField
    reservationdate = models.DateField(auto_now=True)
    comment = models.CharField(max_length=1000)
