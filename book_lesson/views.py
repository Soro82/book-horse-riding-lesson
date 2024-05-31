from django.shortcuts import render, get_object_or_404
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
    booking = get_object_or_404(Booking)

    if request.method == "POST":
        booking_form = BookingForm()

    context = {'booking_form': booking_form}

    return render(request, 'make_booking.html', context)


def bookings(request):
    """
    View to display list of bookings.
    """
    bookings = Booking.objects.filter(user=request.user)
    context = {'bookings': bookings}

    return render(request, 'my_bookings.html', context)