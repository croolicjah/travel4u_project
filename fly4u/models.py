from django.db import models

# Create your models here.
#

class FlyTrip(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200)

    # fares = [('faretype', )]
    # # price = models.DecimalField(decimal_places=2)
    # # timeframes
    # depart_on = models.DateField()
    # arrive_on = models.DateField()
    # # number of stops
    # stops = models.IntegerField()
    # # details
    # airline = models.CharField(max_length=50)
    # class_type = models.CharField(max_length=20)
    # base_fare = models.DecimalField(decimal_places=2)
    # tax_fees = models.DecimalField(decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
