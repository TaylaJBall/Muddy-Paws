from django import forms
from .models import Booking, Slot
from dashboard.models import Pet


class BookingForm(forms.ModelForm):
    """Form to create a booking"""

    class Meta:
        model = Booking
        fields = [
            "pet",
            "service_type",
            "slot"
            "approved",
            "notes",
        ]

        widgets = {
            "notes": forms.Textarea(attrs={"rows": 5}),
            "booking_date": forms.DateInput(attrs={"readonly": "readonly"}),
            "booking_time": forms.TimeInput(attrs={"readonly": "readonly"}),
            "slot": forms.DateTimeInput(attrs={"readonly": "readonly"}),
        }

        labels = {
            "pet": "Pet Name",
            "service_type": "Service Type",
            "slot": "Slot",
            "approved": "Approved?",
            "notes": "Notes",
        }

    def __init__(self, *args, **kwargs):
        available_slots = kwargs.pop('available_slots', [])
        super().__init__(*args, **kwargs)
        self.fields['slot'].queryset = available_slots

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        self.fields['pet'].queryset = Pet.objects.filter(user=user)
