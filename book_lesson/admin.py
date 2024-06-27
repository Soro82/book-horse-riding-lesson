from django.contrib import admin
from .models import Horse, Booking

admin.site.register(Horse)


@admin.register(Booking)
class Bookings(admin.ModelAdmin):
    """
    Arranges how the Bookings are displayed for the admin user.
    Allows the admin user to filter the list of bookings.
    """
    list_display = ('user', 'horse', 'lesson_date', 'lesson_time')
    list_filter = ('user', 'horse')
