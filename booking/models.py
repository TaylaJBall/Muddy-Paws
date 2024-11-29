from django.db import models
from django.contrib.auth.models import User
from .utils import ServiceType

# Create your models here.

class Booking(models.Model):
    """
    A model to create and delete bookings
    """
    user = models.ForeignKey(User, related_name='customer', on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, related_name='customer_pet', on_delete=models.CASCADE)
    service_type = models.IntegerField(choices=ServiceType.choices(), default=ServiceType.PAMPER_PACKAGE)
    booking_date = models.DateField()
    booking_time = models.TimeField()
    approved = models.BooleanField(default=False)
    notes = models.TextField(max_length=500)

    def __str__(self):
        return f"Booking for {self.user.pet} on {self.booking_date} at {self.booking_time}"
    
    class Meta:
        ordering = ['-booking_date', '-booking_time']