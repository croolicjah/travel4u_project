from django.db import models

# Create your models here.
#
"""
    
      "id": 5702,
      "departure": {
        "code": "WMI",
        "airportName": "Modlin",
        "cityName": "Warszawa",
        "cityCode": "waw",
        "countryName": "Polska",
        "countryCode": "pl",
        "continentCode": "eu",
        "cityFrom": "z Warszawy",
        "cityNameFromForm": "z Warszawy"
      },
      "arrival": {
        "code": "CFU",
        "airportName": "Ioannis Kapodistrias",
        "cityName": "Korfu",
        "cityCode": "cfu",
        "countryName": "Grecja",
        "countryCode": "gr",
        "continentCode": "eu",
        "cityTo": "do Korfu",
        "cityNameToForm": "do Korfu"
      },
      "openJawDeparturePort": {
        "code": "",
        "airportName": null,
        "cityNameFromForm": ""
      },
      "openJawArrivalPort": {
        "code": "",
        "airportName": null,
        "cityNameToForm": ""
      },

"""


class Airport(models.Model):
    airport_name = models.CharField(max_length=55)
    airport_code = models.CharField(max_length=5)
    city_name = models.CharField(max_length=55)
    city_name_form = models.CharField(max_length=55)
    country_name = models.CharField(max_length=55)
    country_code =  models.CharField(max_length=10)
    country_name_form = models.CharField(max_length=55)

class Airline(models.Model):
    airline_name = models.CharField(max_length=70)
    airline_code = models.CharField(max_length=6)

class FlyTrip(models.Model):
    image_load = models.ImageField(upload_to='images/', null=True, blank=True)
    wide_photo_url = models.URLField(max_length=400)
    title = models.CharField(max_length=200, null=True, blank=True)

    departure_airport = models.ForeignKey(Airport, on_delete=models.SET_NULL)
    arrival_airport = models.ForeignKey(Airport, on_delete=models.SET_NULL)
    airline = models.ForeignKey(Airline, on_delete=models.SET_NULL)
    price_amount = models.DecimalField(max_digits=10, decimal_places=2)
    flightType = models.CharField(max_length=15)

    depart_on = models.DateField(null=True, blank=True)
    arrive_on = models.DateField(null=True, blank=True)
    likes = models.IntegerField()
    views = models.IntegerField()
    scoring = models.DecimalField(max_digits=5, decimal_places=2)

    offered_on = models.DateField(auto_now_add=True)
