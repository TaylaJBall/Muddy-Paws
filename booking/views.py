from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.core.management import call_command
from django.http import JsonResponse

from .models import Booking, Slot
from .forms import BookingForm

# Create your views here.

# Slot Views
@login_required
def populate_slots_view(request):
    try:
        call_command('populate_slots')
        return JsonResponse({'status': 'success', 'message': 'Slots populated successfully.'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})

def available_slots(request):
    return render(request, 'available_slots.html')

    # Submitting a booking form
    if request.method == 'POST':
        form = BookingForm(request.POST, available_slots=available_slots)
        if form.is_valid():
            form.save()
            # Mark the slot as booked
            slot = form.cleaned_data['slot']
            slot.is_available = False
            slot.save()
            return redirect('dashboard/')
    else:
        form = BookingForm(available_slots=available_slots)

    return render(request, 'available_slots.html', {'form': form, 'available_slots': available_slots})

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

    template_name = "bookings/bookings.html"
    model = Booking
    context_object_name = "booking"


class AddBooking(LoginRequiredMixin, CreateView):
    """
    Add booking view
    """

    template_name = "booking/add_booking.html"
    model = Booking
    form_class = BookingForm
    success_url = "/booking/"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
