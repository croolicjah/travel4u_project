from django.shortcuts import render
from django.views import View
from .models import FlyTrip
# Create your views here.


class HomeFly(View):
    def get(self, request):
        #  <view logic>
        flights = FlyTrip.objects
        return render(request, 'fly4u/home.html', {'flights': flights})