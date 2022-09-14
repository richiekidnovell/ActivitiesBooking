
from django.db import models
class Action (models.Model):
    ActionId = models.AutoField(primary_key=True)
    ActionType = models.IntegerField()
    ActionDateDate = models.DateField()
    bookingComment = models.CharField(max_length=255)


class Bookings (models.Model):
    BookingId = models.AutoField(primary_key=True)
    UserId = models.IntegerField()
    BookingType = models.IntegerField()
    BookingDate = models.DateField()
    bookingComment = models.CharField(max_length=255)

class Cookings (models.Model):
    CookingId = models.AutoField(primary_key=True)
    UserId = models.IntegerField()
    BookingType = models.IntegerField()
    BookingDate = models.DateField()
    bookingComment = models.CharField(max_length=255)

class Lookings (models.Model):
    LookingId = models.AutoField(primary_key=True)
    UserId = models.IntegerField()
    BookingType = models.IntegerField()
    BookingDate = models.DateField()
    bookingComment = models.CharField(max_length=255)
# Create your models here.
