from operator import itemgetter

from django.http import HttpResponse
from django.views import View
from django.shortcuts import render

class Home(View):
    def get(self, request):
        #  <view logic>
        return render(request, 'index.html', {})

    # def post(self, request):
    #     # <other view logic>
    #     return render(request, 'result')


class Count(View):
    def get(self, request):
        #  <view logic>
        fulltext = request.GET['wordscounter']
        words_list = fulltext.split()
        print(words_list)
        words_dictionary = {}

        for word in words_list:
            print(word)
            if word in words_dictionary:
                words_dictionary[word] += 1
            else:
                words_dictionary[word] = 1
        sorted_dict = sorted(words_dictionary.items(), key=itemgetter(1), reverse=True)
        return render(request, 'count.html', {'wordscounter':fulltext, 'count': len(words_list), 'wordsdictionary': sorted_dict})

class About(View):
    def get(self, request):
        #  <view logic>

        return render(request, 'about.html')
