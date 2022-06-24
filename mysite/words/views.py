from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Countries
import random

countries_list = []


def index(request):
    global countries_list
    if not countries_list:
        countries_list = list(Countries.objects.filter(oxford_chapter='A2U1'))

    countries_left = len(countries_list)
    countries_count = len(list(Countries.objects.filter(oxford_chapter='A2U1')))
    country = countries_list.pop(random.randrange(countries_left))
    template = loader.get_template('words/index.html')
    context = {
        'country': country,
        'countries_left': countries_left,
        'countries_count': countries_count,
    }
    return HttpResponse(template.render(context, request))
