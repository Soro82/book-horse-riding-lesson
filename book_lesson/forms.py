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
        fields = ('lesson_date', 'lesson_time', 'location', 'experience', 'horse')
        widgets = {"lesson_date": DateInput()}