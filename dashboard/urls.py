from django.urls import path
from . import views
from .views import Dashboard, AddPet, PetDetail, DeletePet, EditPet

urlpatterns = [
    path("add_pet", AddPet.as_view(), name="add_pet"),
    path("", Dashboard.as_view(), name="dashboard"),
    path("<slug:pk>/", PetDetail.as_view(), name="pet_detail"),
    path("delete/<slug:pk>/", DeletePet.as_view(), name="delete_pet"),
    path("edit/<slug:pk>/", EditPet.as_view(), name="edit_pet"),
]
