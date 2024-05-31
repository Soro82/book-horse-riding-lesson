from django.urls import path
from book_lesson.views import Home, booking, bookings

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('make_booking/', booking, name='booking'),
    path('my_bookings/', bookings, name='bookings'),
]