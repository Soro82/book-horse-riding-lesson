from django import forms
from datetime import date
from .models import Booking


class DateInput(forms.DateInput):
    input_type = "date"


class BookingForm(forms.ModelForm):
    """
    This class creates the form for making Bookings.
    """
    class Meta:
        model = Booking
        fields = ('horse', 'lesson_date', 'lesson_time', 'location', 'experience')
        widgets = {"lesson_date": DateInput()}