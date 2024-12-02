from django.views.generic import CreateView, ListView, DetailView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Booking
from .forms import BookingForm

# Create your views here.


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
