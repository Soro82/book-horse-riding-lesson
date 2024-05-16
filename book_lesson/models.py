from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Horse(models.Model):
    """
    Details of each horse available.
    """
    name = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    height = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.name


class Booking(models.Model):
    """
    Book a horse riding lesson.
    """
    EXPERIENCE_LEVEL = ((0, "Beginner"), (1, "Intermediate"), (2, "Advanced"))
    INDOOR_OUTDOOR = ((0, "Indoor"), (1, "Outdoor"))

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson_date = models.DateField()
    lesson_time = models.TimeField()
    location = models.IntegerField(choices=INDOOR_OUTDOOR, default=0)
    experience = models.IntegerField(choices=EXPERIENCE_LEVEL, default=0)
    horse = models.ForeignKey(Horse, on_delete=models.CASCADE)

    def __str__(self):
        return f"Booking {self.id} for {self.user.username} on {self.lesson_date}"


        
