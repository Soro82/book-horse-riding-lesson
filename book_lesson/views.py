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
    if request.method == "POST":
        booking_form = BookingForm(request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your booking was successful'
            )

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


def edit_booking(request, booking_id):
    """
    View for the user to edit a booking.
    """
    booking = get_object_or_404(Booking, id=booking_id)

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your update was successful.'
            )

    context = {
        'form': form
        }

    return render(request, 'edit_booking.html', context)
