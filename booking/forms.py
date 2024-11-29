from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    """ Form to create a booking """
    class Meta:
        model = Booking
        fields = ['user', 'pet', 'service_type', 'booking_date', 'booking_time', 'approved, notes']

        widgets = {
            'notes': forms.Textarea(attrs={'rows': 5}),
            'user': forms.HiddenInput(),
            'booking_date': forms.HiddenInput(),
            'booking_time': forms.HiddenInput(),
        }

        labels = {
            'User': 'User',
            'pet': 'Pet Name',
            'service_type': 'Service Type',
            'booking_date': 'Booking Date',
            'booking_time': 'Booking Time',
            'approved': 'Approved?',
            'notes': 'Notes',


        }