from django.contrib import admin
from .models import Booking


# Register your models here.
class BookingAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'service', 'booking_date', 'booking_time', 'approved']

    list_filter = ['booking_date', 'booking_time', 'approved']

admin.site.register(Booking, BookingAdmin)