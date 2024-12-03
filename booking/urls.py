from django.urls import path
from booking.views import AddBooking, Bookings, BookingDetail
from . import views

urlpatterns = [
    path("", AddBooking.as_view(), name="add_booking"),
    path('populate-slots/', views.populate_slots_view, name='populate_slots'),
    path("available-slots/", views.available_slots, name='available_slots'),
    path("bookings/", Bookings.as_view(), name="bookings"),
    path("bookings/<slug:pk>/", BookingDetail.as_view(), name="booking_detail"),
]
