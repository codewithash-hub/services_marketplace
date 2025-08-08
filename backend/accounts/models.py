from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(models.Model):
    class Gender(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', "Female"

    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    
    gender = models.CharField(
        max_length=2,
        choices=Gender,
        default=Gender.MALE
    )
    is_provider = models.BooleanField(default=False) # This is to determine if the user is a provider or a client
    phone_number = models.CharField(max_length=20, blank=True)
    town = models.CharField(max_length=255, blank=True)
    suburb = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.username
