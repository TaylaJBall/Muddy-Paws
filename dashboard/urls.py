from django.urls import path
from . import views
from dashboard.views import Dashboard, AddPet, PetDetail
from booking.views import AddBooking, Bookings, BookingDetail

urlpatterns = [
    path("dashboard", AddPet.as_view(), name="add_pet"),
    path("", Dashboard.as_view(), name="dashboard"),
    path("dashboard/pet_detail/<slug:pk>/", PetDetail.as_view(), name="pet_detail"),
]