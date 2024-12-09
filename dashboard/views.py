from django.views.generic import CreateView, ListView, DetailView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Pet
from .forms import PetForm
from booking.models import Booking, Slot

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
        bookings = Booking.objects.filter(user=request.user)
        pets = Pet.objects.filter(user=request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pets'] = Pet.objects.filter(user=self.request.user)
        context['bookings'] = Booking.objects.filter(user=self.request.user)
        return context

        return render(request, "dashboard/dashboard.html", context)


class BookingDetail(DetailView):
    model = Booking
    template_name = "booking_detail.html"
    context_object_name = "booking"

    def get_object(self, queryset=None):
        booking = super().get_object(queryset)
        print(booking)
        return booking


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
        if request.method == 'POST':
            form = PetForm(request,POST, request.FILES)
            if form.is_valid():
                pet = form.save(commit=False)
                pet.user = request.user
                pet.save(Dashboard)
                return redirect('dashboard')
        
        else:
            form = PetForm()
        return render(request, 'dashboard/add_pet.html', {'form': form})

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddPet, self).form_valid(form)
