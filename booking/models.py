from django.db import models
from django.contrib.auth.models import User
from dashboard.models import Pet

# Choice Fields
ServiceType = (
    ('PAMPER_PACKAGE', 'Pamper Package'),
    ('FULL_GROOM', 'Full Groom'),
    ('HAND_STRIP', 'Hand Strip'),

)

# Booking Model

class Booking(models.Model):
    """
    A model to create and delete bookings
    """
    user = models.ForeignKey(User, related_name='bookings', on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, related_name='bookings', on_delete=models.CASCADE)
    service_type = models.CharField(max_length=50, choices=ServiceType, default='PAMPER_PACKAGE')
    booking_date = models.DateField()
    booking_time = models.TimeField()
    approved = models.BooleanField(default=False)
    notes = models.TextField(max_length=500)

    def __str__(self):
        return f"Booking for {self.user.pet} for a {self.service_type} on {self.booking_date} at {self.booking_time}"
    
    class Meta:
        ordering = ['-booking_date', '-booking_time']