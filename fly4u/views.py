from django.contrib.admin.utils import flatten
from django.shortcuts import render
from django.views import View
from .models import FlyTrip
import requests
from operator import itemgetter
from  fly4u.ulc.pdf_to_python import most_trafficed_cities
from fly4u.deals_scoring_tools import most_viewed_destinations
# Create your views here.


class HomeFly(View):
    def get(self, request):
        #  <view logic>
        deals = self.select_cheapest_deals(self.get_esky_deals())

        return render(request, 'fly4u/home.html', {'deals': deals})

    # grab deals from eSky API
    def get_esky_deals(self):
        # eSky response has lists deals and simpleDealsData. Collecting set from deals list

        deals = requests.get('https://www2.esky.pl/api/v1.0/deals.json').json()['deals']

        return self.sort_deals(deals)

    def sort_deals(self, deals):
        list_2_digits, list_3_digits, list_4_digits = [], [], []

        # cut list of deals
        for deal in deals:
            if len(deal['priceAmount']) < 3:
                list_2_digits.append(deal)
            elif len(deal['priceAmount']) < 4:
                list_3_digits.append(deal)
            elif len(deal['priceAmount']) < 5:
                list_4_digits.append(deal)

        new_deals = sorted(list_2_digits, key=itemgetter('priceAmount')) + sorted(list_3_digits, key=itemgetter('priceAmount')) + sorted(list_4_digits, key=itemgetter('priceAmount'))

        return new_deals

    def select_cheapest_deals(self, deals):
        repeaters = []
        cheap_deals = []
        destination_deals = []
        selected_deals = most_viewed_destinations + flatten(most_trafficed_cities)
        # select deals by key: not double destination, sort by price
        for deal in deals:
            if deal['arrival']['continentCode'] == "eu" and deal['arrival']['code'] in selected_deals:

                deal_price = int(deal['priceAmount'])
                deal_destination = deal['arrival']['cityTo']

                # create list for showing on site. no double destinations. only europe flights
                if deal_destination not in repeaters:
                    repeaters.append(deal_destination)
                    cheap_deals.append(deal)
                else:
                    for i in range(len(cheap_deals)):
                        if (deal_price < int(cheap_deals[i]['priceAmount'])):
                            cheap_deals[i] = deal
                        elif (deal_price == int(cheap_deals[i]['priceAmount'])):
                            destination_deals.append(deal)

        return cheap_deals

    def select_long_deals(self, deals):

        repeaters = []
        cheap_deals = []
        destination_deals = []

        # select deals by key: not double destination, sort by price
        for deal in deals:
            if deal['arrival']['codeContinent'] in longs:
                deal_price = int(deal['priceAmount'])
                deal_destination = deal['arrival']['code']

                # create list for showing on site. no double destinations. only the cheapest flight on
                if deal_destination not in repeaters:
                    repeaters.append(deal_destination)
                    cheap_deals.append(deal)
                else:
                    for i in range(len(cheap_deals)):
                        if deal_price < int(cheap_deals[i]['priceAmount']):
                            cheap_deals[i] = deal
                        elif deal_price == int(cheap_deals[i]['priceAmount']):
                            destination_deals.append(deal)

        return cheap_deals

    def score_deal(self):
        self.score = 1
        return self.score

    def set_deals_que(self, deals):
        self.deals = deals
        return self.deals