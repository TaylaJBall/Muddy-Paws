from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django_resized import ResizedImageField
from django.conf import settings

# Choice Fields
Gender = (("male", "Male"), ("female", "Female"))

# Create your models here.


class Pet(models.Model):
    """
    A model for creating a Pet profile
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="pet_owner", on_delete=models.CASCADE
    )
    pet = models.CharField(max_length=50)
    pet_image = ResizedImageField(
        size=[400, None],
        quality=75,
        upload_to="pets/",
        force_format="WEBP",
        default="placeholder",
    )
    breed = models.CharField(max_length=50)
    gender = models.CharField(max_length=50, choices=Gender, default="male")
    colour = models.CharField(max_length=50)
    age = models.IntegerField()
    allergies = models.BooleanField(default=False)
    vaccinated = models.BooleanField(default=False)
    microchipped = models.BooleanField(default=False)
    spayed_neutered = models.BooleanField(default=False)
    extra_info = models.TextField(max_length=300)

    def __str__(self):
        return str(self.pet)
