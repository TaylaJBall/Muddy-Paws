from django.urls import path, include
from booking.views import AddBooking, Bookings, BookingDetail
from dashboard.views import Dashboard
from . import views

app_name = 'booking'

urlpatterns = [
    # path('select-slot/', views.select_slot, name='select_slot'),
    path("add_booking/<int:slot_id>/", AddBooking.as_view(), name="add_booking"),
    path('populate-slots/', views.populate_slots_view, name='populate_slots'),
    path("available-slots/", views.available_slots, name='available_slots'),
    path("bookings/", Bookings.as_view(), name="bookings"),
    path("bookings/<slug:pk>/", BookingDetail.as_view(), name="booking_detail"),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
]
