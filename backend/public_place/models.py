from pyexpat import model
from django.db import models
from general_user.models import User, USER_STATUS_CHOICES


PLACE_STATUS_CHOICES = (
    ('W', 'White'),
    ('R', 'Red'),
)


class PublicPlace(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    name = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255, blank=True)
    region = models.PositiveSmallIntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class PlaceStatus(models.Model):
    place = models.ForeignKey(PublicPlace, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=PLACE_STATUS_CHOICES)
    date_created = models.DateTimeField(auto_now_add=True)


class MeetPlace(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    place = models.ForeignKey(
        PublicPlace, on_delete=models.SET_NULL, null=True)
    status_user = models.PositiveSmallIntegerField(choices=USER_STATUS_CHOICES)
    status_Place = models.PositiveSmallIntegerField(
        choices=PLACE_STATUS_CHOICES)
    date_created = models.DateTimeField(auto_now_add=True)