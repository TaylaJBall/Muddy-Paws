from django.db import models
from django.contrib.auth.models import User
from dashboard.models import Pet

# Choice Fields
ServiceType = (
    ("PAMPER_PACKAGE", "Pamper Package"),
    ("FULL_GROOM", "Full Groom"),
    ("HAND_STRIP", "Hand Strip"),
)

times = (
    ("10:00", "10:00"),
    ("12:00", "12:00"),
    ("14:00", "14:00"),
    ("16:00", "16:00"),
)

# Slots Model
class Slot(models.Model):
    booking_date = models.DateField()
    booking_time = models.CharField(choices = times)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Slot: {self.booking_date} at {self.booking_time}"

    @classmethod
    def select_slot(cls, slot_id):
        try:
            slot = cls.objects.get(id=slot_id, is_available=True)
            slot.is_available = False
            slot.save()
            return slot
        except cls.DoesNotExist:
            return None

# Booking Model


class Booking(models.Model):
    """
    A model to create and delete bookings
    """
    user = models.ForeignKey(User, related_name="bookings", on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, related_name="bookings", on_delete=models.CASCADE)
    service_type = models.CharField(
        max_length=50, choices=ServiceType, default="PAMPER_PACKAGE"
    )
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE, null=True, blank=True)
    slotapproved = models.BooleanField(default=False)
    notes = models.TextField(max_length=500)

    def __str__(self):
        return f"Booking for {self.pet} for a {self.service_type} on {self.slot}"

    class Meta:
        ordering = ["-slot"]
    @classmethod
    def create_booking_with_slot(cls, user, pet, service_type, slot_id, notes):
        selected_slot = Slot.select_slot(slot_id)
        if selected_slot:
            booking = cls.objects.create(
                user=user,
                pet=pet,
                service_type=service_type,
                slot=selected_slot,
                notes=notes
            )
            return booking
        return None
