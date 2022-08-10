from django.db import models
from django.contrib.auth.models import AbstractUser
from config.settings import GENERAL_USER, BUSINESS_USER, ADMIN_USER


USER_STATUS_CHOICES = (
    (1, 'Healthy'),
    (2, 'Doubtful'),
    (3, 'Perilous'),
    (4, 'Patient'),
    (5, 'Dead')
)


class User(AbstractUser):
    national_code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=11, blank=True)

    @property
    def type(self):
        if hasattr(self, 'generaluser'):
            return GENERAL_USER
        if hasattr(self, 'publicplace'):
            return BUSINESS_USER
        if hasattr(self, 'administrator'):
            return ADMIN_USER


class GeneralUser(models.Model):
    BLOOD_TYPE_CHOICES = (
        ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'),
        ('O+', 'O+'), ('O-', 'O-'),
        ('AB+', 'AB+'), ('AB-', 'AB-')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True)
    blood_type = models.CharField(
        max_length=3, choices=BLOOD_TYPE_CHOICES, null=True)
    height = models.PositiveSmallIntegerField(null=True)
    weight = models.PositiveSmallIntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class UserStatus(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.PositiveSmallIntegerField(choices=USER_STATUS_CHOICES)
    date_created = models.DateTimeField(auto_now_add=True)


class MeetPeople(models.Model):
    user1 = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name='meet_people1', null=True)
    user2 = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name='meet_people2', null=True)
    status_user1 = models.PositiveSmallIntegerField(
        choices=USER_STATUS_CHOICES)
    status_user2 = models.PositiveSmallIntegerField(
        choices=USER_STATUS_CHOICES)
    date_created = models.DateTimeField(auto_now_add=True)