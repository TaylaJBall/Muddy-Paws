from django.views.generic import CreateView
from .models import Booking

# Create your views here.

class AddBooking(CreateView):
    """
    Add booking view
    """
    template_name = 'booking/add_booking.html'
    model = Booking
    success_url = '/booking/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddBooking, self).form_valid(form)