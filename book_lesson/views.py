from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Booking
from .forms import BookingForm

# Create your views here.
class Home(generic.TemplateView):
    """
    View to dispaly the Homepage.
    """
    template_name = 'index.html'


@login_required
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


@login_required
def edit_booking(request, booking_id):
    """
    View for the user to edit a booking.
    """
    booking = get_object_or_404(Booking, id=booking_id)

    form = BookingForm(instance=booking)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your update was successful.'
            )
            return redirect('bookings')

    context = {
        'form': form
        }

    return render(request, 'edit_booking.html', context)


@login_required
def delete_booking(request, booking_id):
    """
    View for the user to delete a booking.
    """
    booking = get_object_or_404(Booking, id=booking_id)

    booking.delete()
    messages.add_message(
        request, messages.SUCCESS,
        'Booking deleted successfully.'
        )
    return redirect('bookings')


def custom_handler404(request, exception):
    """
    Custom handler for 404 (Page Not Found) errors.
    """
    return render(request, '404.html', status=404)


def custom_handler500(request):
    """
    Custom handler for 500 (Internal Server Error) errors.
    """
    return render(request, '500.html', status=500)