from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    """
    This class creates the form for making Bookings.
    """
    class Meta:
        model = Booking
        fields = ('lesson_date', 'lesson_time', 'location', 'experience_level', 'horse')
