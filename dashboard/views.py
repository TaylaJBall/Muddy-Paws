from django.shortcuts import render

# Create your views here.
class DashboardView(TemplateView):
    template_name = 'dashboard.html'