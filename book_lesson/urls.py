from django.urls import path
from book_lesson.views import Home

urlpatterns = [
    path('', Home.as_view(), name='home'),
]