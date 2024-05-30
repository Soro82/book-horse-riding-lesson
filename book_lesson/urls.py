from django.urls import path
from book_lesson.views import Home, booking

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('booking/', booking, name='booking'),
]