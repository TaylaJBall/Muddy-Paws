from django import forms
from .models import Booking, Slot
from dashboard.models import Pet


class SlotForm(forms.ModelForm):
    slot = forms.ModelChoiceField(queryset=Slot.objects.filter(is_available=True), required=True)

    class Meta:
        model = Slot
        fields = [
            'slot'
        ]

    def __init__(self, *args, **kwargs):
        available_slots = kwargs.pop('available_slots', None)
        super().__init__(*args, **kwargs)

        if available_slots:
            self.fields['slot'] = forms.ModelChoiceField(
                queryset=available_slots,
                required=True,
                empty_label="Select a slot"
            )


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
