from django.db import models

# Create your models here.
class Trip(models.Model):
    price = models.DecimalField(decimal_places=2)