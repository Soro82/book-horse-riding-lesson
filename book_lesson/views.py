from django.shortcuts import render
from django.views import generic
from django.contrib import messages
from .models import Booking
from .forms import BookingForm

# Create your views here.
class Home(generic.TemplateView):
    """
    View to dispaly the Homepage.
    """
    template_name = 'index.html'


def booking(request):
    """
    Displays the Booking Form.
    """
    booking_form = BookingForm()

    context = {'booking_form': booking_form}

    return render(request, 'booking.html', context)
