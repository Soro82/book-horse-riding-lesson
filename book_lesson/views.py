from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
import datetime
from .models import Booking, Horse
from .forms import BookingForm


# Create your views here.
def home(request):
    """
    View to dispaly the Homepage.
    """
    top_horses = Horse.objects.all()[:3]
    context = {'top_horses': top_horses}

    return render(request, 'index.html', context)


@login_required
def booking(request, horse_id):
    """
    Displays the Booking Form.
    """
    horse = get_object_or_404(Horse, id=horse_id)

    if request.method == "POST":
        booking_form = BookingForm(request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.horse = horse
            booking_exists = Booking.objects.filter(
                lesson_date=booking.lesson_date,
                lesson_time=booking.lesson_time,
                horse=booking.horse
            )
            booking_time_exists = Booking.objects.filter(
                user=request.user,
                lesson_date=booking.lesson_date,
                lesson_time=booking.lesson_time
            )
            booking_full = Booking.objects.filter(
                lesson_date=booking.lesson_date,
                lesson_time=booking.lesson_time
            )
            today = datetime.date.today()

            if booking_exists:
                messages.warning(request, "This horse is already booked for this time.")
            elif booking_time_exists:
                messages.warning(request, "You already have a booking for this time.")
            elif booking_full.count() > 4:
                messages.warning(request, "This lesson is full. Please choose another time.")
            elif today > booking.lesson_date:
                messages.warning(request, "Please choose today's date or a future date.")
            else:
                booking.user = request.user
                booking.save()
                messages.add_message(
                    request, messages.SUCCESS,
                    'Your booking was successful'
                )

    booking_form = BookingForm()

    context = {'booking_form': booking_form, 'horse': horse}

    return render(request, 'make_booking.html', context)


def horses(request):
    """
    View to display all horses available on a seperate page.
    """
    horses = Horse.objects.all()
    paginator = Paginator(horses, 3)
    page_number = request.GET.get("page")
    horses = paginator.get_page(page_number)

    context = {'horses': horses}

    return render(request, 'horses.html', context)


def bookings(request):
    """
    View to display list of bookings.
    """
    bookings = Booking.objects.filter(user=request.user).order_by("lesson_date")
    paginator = Paginator(bookings, 3)
    page_number = request.GET.get("page")
    bookings = paginator.get_page(page_number)

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
            booking_exists = Booking.objects.filter(
                lesson_date=booking.lesson_date,
                lesson_time=booking.lesson_time,
                horse=booking.horse
            )
            booking_time_exists = Booking.objects.filter(
                lesson_date=booking.lesson_date,
                lesson_time=booking.lesson_time
            )
            booking_full = Booking.objects.filter(
                lesson_date=booking.lesson_date,
                lesson_time=booking.lesson_time
            )
            today = datetime.date.today()

            if booking_exists:
                messages.warning(request, "This horse is already booked for this time.")
            elif booking_time_exists:
                messages.warning(request, "You already have a booking for this time.")
            elif booking_full.count() > 4:
                messages.warning(request, "This lesson is full. Please choose another time.")
            elif today > booking.lesson_date:
                messages.warning(request, "Please choose today's date or a future date.")
            else:
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

    if request.method == 'POST':
        booking.delete()
        messages.add_message(
            request, messages.SUCCESS,
            'Booking deleted successfully.'
            )
        return redirect('bookings')

    return render(request, 'delete_booking.html', {'booking': booking})


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
