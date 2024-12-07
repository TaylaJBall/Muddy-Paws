from django.urls import path
from . import views
from dashboard.views import Dashboard, AddPet, PetDetail
from booking.views import AddBooking, Bookings, BookingDetail

urlpatterns = [
    path("add_pet.html", AddPet.as_view(), name="add_pet"),
    path("", Dashboard.as_view(), name="dashboard"),
    path("pet_detail/<slug:pk>/", PetDetail.as_view(), name="pet_detail"),
    path('bookings', Bookings.as_view(), name='bookings'),
    path('booking/<int:pk>/', BookingDetail.as_view(), name='booking_detail'),
]