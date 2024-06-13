from django.urls import path
from book_lesson.views import home, booking, horses, bookings, edit_booking, delete_booking

urlpatterns = [
    path('', home, name='home'),
    path('make_booking/', booking, name='booking'),
    path('my_bookings/', bookings, name='bookings'),
    path('horses/', horses, name='horses_page'),
    path('edit_booking/<int:booking_id>/', edit_booking, name='edit'),
    path('delete_booking/<int:booking_id>/', delete_booking, name='delete'),
]