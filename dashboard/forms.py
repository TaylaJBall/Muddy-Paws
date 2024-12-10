from django import forms
from booking.models import Booking
from .models import Pet


class PetForm(forms.ModelForm):
    """Form to add a pet"""

    class Meta:
        model = Pet
        exclude = ["user"]
        fields = [
            "pet",
            "pet_image",
            "breed",
            "gender",
            "colour",
            "age",
            "allergies",
            "vaccinated",
            "microchipped",
            "spayed_neutered",
            "extra_info",
        ]

        widgets = {
            "extra_info": forms.Textarea(attrs={"rows": 5}),
        }

        labels = {
            "pet": "Pet Name",
            "pet_image": "Pet Image",
            "breed": "Breed of Dog",
            "gender": "Gender",
            "colour": "Colour",
            "age": "Age",
            "allergies": "Allergies",
            "vaccinated": "Vaccinated",
            "microchipped": "Microchipped",
            "spayed_neutered": "Spayed/Neutered",
            "extra_info": "Extra Information",
        }
