from django import forms
from datetime import date
from .models import Booking


class DateInput(forms.DateInput):
    """
    Allows the user to choose a date from a calender
    in the Booking Form.
    """
    input_type = "date"


class BookingForm(forms.ModelForm):
    """
    This class creates the form for making Bookings.
    """
    class Meta:
        model = Booking
        fields = ('lesson_date', 'lesson_time', 'location', 'experience')
        widgets = {"lesson_date": DateInput()}
        labels = {
            'lesson_date': 'Lesson Date',
            'lesson_time': 'Lesson Time'
        }
