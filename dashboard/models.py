from django.db import models
from django.contrib.auth.models import User

# Choice Fields
Gender = (
    ('male', 'Male'),
    ('female', 'Female')
)

# Create your models here.

class Pet(models.Model):
    """
    A model for creating a Pet profile
    """
    user = models.ForeignKey(User, related_name='pets', on_delete=models.CASCADE)
    pet = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    gender = models.CharField(max_length=50, choices=Gender, default='male')
    colour = models.CharField(max_length=50)
    age = models.IntegerField()
    allergies = models.BooleanField(default=False)
    vaccinated = models.BooleanField(default=False)
    microchipped = models.BooleanField(default=False)
    spayed_neutered = models.BooleanField(default=False)
    extra_info = models.TextField(max_length=300)