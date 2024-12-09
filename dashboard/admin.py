from django.contrib import admin
from .models import Pet

# Register your models here.
@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'pet',
        'breed',
        'gender',
        'colour',
        'age',
        'allergies',
        'vaccinated',
        'microchipped',
        'spayed_neutered',
        'extra_info'
    ]
    list_filter = ('user',)