from django import forms
from .models import Booking, Slot
from dashboard.models import Pet
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


class SlotForm(forms.ModelForm):
    slot = forms.ModelChoiceField(queryset=Slot.objects.filter(is_available=True), required=True, empty_label="Select a slot")

    class Meta:
        model = Slot
        fields = [
            'slot'
        ]

    def __init__(self, *args, **kwargs):
        available_slots = kwargs.pop('available_slots', None)
        super().__init__(*args, **kwargs)

        if available_slots:
            self.fields['slot'].queryset = available_slots


class BookingForm(forms.ModelForm):
    """Form to create a booking"""

    class Meta:
        model = Booking
        fields = [
            "user",
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
            "user": "User",
            "pet": "Pet Name",
            "service_type": "Service Type",
            "slot": "Slot",
            "approved": "Approved?",
            "notes": "Notes",
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        available_slots = kwargs.pop('available_slots', [])
        selected_slot = kwargs.pop("selected_slot", None)
        
        super().__init__(*args, **kwargs)

    

        if user:
            self.fields['pet'].queryset = Pet.objects.filter(user=user)

        if selected_slot:
            self.selected_slot = select_slot
        
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('pet', css_class='form-group col-md-6 mb-0'),
                Column('service_type', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'notes',
            Submit('submit', 'Book Now', css_class='btn btn-primary')
        )
