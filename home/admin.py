from django.contrib import admin
from booking.models import Booking

# Register your models here.

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'pet',
        'service_type',
        'booking_date',
        'booking_time',
        'approved',
        'notes'
    )

    list_filter = ('booking_date',)