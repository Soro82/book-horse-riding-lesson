from django.shortcuts import render
from django.views import generic
from .models import Booking

# Create your views here.
class Home(generic.TemplateView):
    """
    View to dispaly the Homepage.
    """
    template_name = 'index.html'