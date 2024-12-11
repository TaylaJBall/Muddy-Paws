from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
)

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render

from .models import Pet
from .forms import PetForm

# Create your views here.


class Dashboard(LoginRequiredMixin, ListView):
    """
    View all pets
    """

    template_name = "dashboard/dashboard.html"
    model = Pet
    context_object_name = "pets"

    @login_required
    def dashboard(request):
        pets = Pet.objects.filter(user=request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pets"] = Pet.objects.filter(user=self.request.user)
        return context

        return render(request, "dashboard/dashboard.html", context)


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

    @login_required
    def add_pet(request):
        if request.method == "POST":
            form = PetForm(request, POST, request.FILES)
            if form.is_valid():
                pet = form.save(commit=False)
                pet.user = request.user
                pet.save(Dashboard)
                return redirect("dashboard")

        else:
            form = PetForm()
        return render(request, "dashboard/add_pet.html", {"form": form})

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success
        (self.request, f"Your pet has been added successfully!")
        return super(AddPet, self).form_valid(form)


class EditPet(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Edit a Pet
    """

    template_name = "dashboard/edit_pet.html"
    model = Pet
    form_class = PetForm
    success_url = "/dashboard/"

    def test_func(self):
        return self.request.user == self.get_object().user

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success
        (self.request, f"Your pet has been edited successfully!")
        return super().form_valid(form)


class DeletePet(
    LoginRequiredMixin,
    UserPassesTestMixin,
    DeleteView,
):
    """
    Delete a Pet
    """

    model = Pet
    success_url = "/dashboard/"

    def test_func(self):
        return self.request.user == self.get_object().user

    def form_valid(self, form):
        messages.success
        (self.request, f"Your pet has been deleted successfully!")
        return super().form_valid(form)
