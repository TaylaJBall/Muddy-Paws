from django.views.generic import CreateView, ListView, DetailView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Pet
from .forms import PetForm

# Create your views here.

class Dashboard(LoginRequiredMixin, ListView):
    """
    View all pets
    """

    template_name = "dashboard.html"
    model = Pet
    context_object_name = "dashboard"


class PetDetail(DetailView):
    """
    View a single pet
    """

    template_name = "dashboard/pet_detail.html"
    model = Pet
    context_object_name = "pet"


class AddPet(LoginRequiredMixin, CreateView):
    """
    Add pet view
    """

    template_name = "dashboard/add_pet.html"
    model = Pet
    form_class = PetForm
    success_url = "/dashboard/"
