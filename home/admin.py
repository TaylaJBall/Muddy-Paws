from django.contrib import admin
from booking.models import Booking

# Register your models here.

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'pet',
        'service_type',
        'slot',
        'slotapproved',
        'notes'
    )

    list_filter = ('slot', 'slotapproved')