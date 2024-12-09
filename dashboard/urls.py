from django.urls import path
from . import views
from .views import Dashboard, AddPet, PetDetail
from booking.views import AddBooking, Bookings, BookingDetail

urlpatterns = [
    path("", AddPet.as_view(), name="add_pet"),
    path("dashboard", Dashboard.as_view(), name="dashboard"),
    path("pet_detail/<int:pk>/", views.PetDetail.as_view(), name="pet_detail"),
    path('bookings', Bookings.as_view(), name='bookings'),
    path('booking/<int:pk>/', BookingDetail.as_view(), name='booking_detail'),
]