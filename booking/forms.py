from django import forms
from .models import Booking
from dashboard.models import Pet


class BookingForm(forms.ModelForm):
    """Form to create a booking"""

    class Meta:
        model = Booking
        fields = [
            "pet",
            "service_type",
            "booking_date",
            "booking_time",
            "approved",
            "notes",
        ]

        widgets = {
            "notes": forms.Textarea(attrs={"rows": 5}),
            "booking_date": forms.DateInput(attrs={"readonly": "readonly"}),
            "booking_time": forms.TimeInput(attrs={"readonly": "readonly"}),
        }

        labels = {
            "pet": "Pet Name",
            "service_type": "Service Type",
            "booking_date": "Booking Date",
            "booking_time": "Booking Time",
            "approved": "Approved?",
            "notes": "Notes",
        }

    # def __init__(self, *args, **kwargs):
    #     user = kwargs.pop("user", None)
    #     print('user in form: ', user)
    #     super(BookingForm, self).__init__(*args, **kwargs)
    #     self.fields["user"].required = False

    #     if user:
    #         self.fields["pet"].queryset = Booking.objects.filter(user=user)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        self.fields['pet'].queryset = Pet.objects.filter(user=user)
