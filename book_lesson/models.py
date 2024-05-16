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

        
