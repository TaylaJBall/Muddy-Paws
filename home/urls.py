from . import views
from django.urls import path

urlpatterns = [
    path('', 
        views.Index.as_view(), name='home'),
    path('booking/', views.Booking.as_view(), name='booking')
]
