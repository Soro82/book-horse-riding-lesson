from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


# Create your models here.
class Horse(models.Model):
    """
    Details of each horse available. Their image is
    stored using Cloudinary.
    """
    name = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    height = models.DecimalField(max_digits=4, decimal_places=2)
    image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.name


class Booking(models.Model):
    """
    Model to store all the information for each booking.
    The bookings are displayed in the admin panel with the
    username and lesson date of each booking and ordered by
    the lesson date.
    """
    EXPERIENCE_LEVEL = ((0, "Beginner"), (1, "Intermediate"), (2, "Advanced"))
    INDOOR_OUTDOOR = ((0, "Indoor"), (1, "Outdoor"))
    LESSON_TIMES = ((0, "10:00"), (1, "11:00"), (2, "12:00"), (3, "14:00"),
                    (4, "15:00"), (5, "16:00"), (6, "17:00"))
    AGE_RANGE = ((0, ""), (1, "Child"), (2, "Adult"))

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson_date = models.DateField()
    lesson_time = models.IntegerField(choices=LESSON_TIMES, default=0)
    location = models.IntegerField(choices=INDOOR_OUTDOOR, default=0)
    experience = models.IntegerField(choices=EXPERIENCE_LEVEL, default=0)
    horse = models.ForeignKey(Horse, on_delete=models.CASCADE)
    age = models.IntegerField(choices=AGE_RANGE, default=0, blank=True)
    user_height = models.DecimalField(max_digits=4, decimal_places=2,
                                      default=0.0, blank=True)

    class Meta:
        ordering = ["-lesson_date"]

    def __str__(self):
        return f"Booking for {self.user.username} on {self.lesson_date}"
