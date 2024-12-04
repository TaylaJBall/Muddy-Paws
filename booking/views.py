from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.management import call_command
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.core.serializers import serialize

from .models import Booking, Slot
from .forms import BookingForm, SlotForm

# Create your views here.


# Slot Views
@login_required
def populate_slots_view(request):
    try:
        call_command('populate_slots')

        slots = Slot.objects.all()

        slots_data = serialize('json', slots)

        return JsonResponse({
            'status': 'success',
            'message': 'Slots populated successfully.',
            'slots': slots_data
            })
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})


def available_slots(request):
    available_slots = Slot.objects.filter(is_available=True)

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest' and request.method == "GET":

        slots_data = [
            {
                'booking_date': slot.booking_date,
                'booking_time': slot.booking_time,
                'id': slot.id,
            }
            for slot in available_slots
        ]
        return JsonResponse({
            'status': 'success',
            'message': 'Slots loaded successfully!',
            'slots': slots_data
        })

    # Submitting a booking form
    if request.method == 'POST':
        form = SlotForm(request.POST)
        if form.is_valid():
            # Mark the slot as booked
            slot = form.cleaned_data['slot']
            slot.is_available = False
            slot.save()
            return redirect('dashboard/')
    else:
        form = SlotForm(available_slots=available_slots)

    return render(request, 'booking/available_slots.html', {'form': form, 'available_slots': available_slots})

# Booking Views


class Bookings(ListView):
    """
    View all bookings
    """

    template_name = "booking/bookings.html"
    model = Booking
    context_object_name = "bookings"


class BookingDetail(DetailView):
    """
    View a single booking
    """

    template_name = "booking/bookings.html"
    model = Booking
    context_object_name = "booking"


class AddBooking(LoginRequiredMixin, CreateView):
    """
    Add booking view
    """

    template_name = "booking/add_booking.html"
    model = Booking
    form_class = BookingForm
    success_url = "/dashboard/"


class AvailableSlots(LoginRequiredMixin, CreateView):
    """
    Add booking view
    """

    template_name = "booking/available_slots.html"
    model = Booking
    success_url = "/dashboard/"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
