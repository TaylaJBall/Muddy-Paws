from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class Index(TemplateView):
    """
    Displays home page"
    """
    template_name = 'home/index.html'