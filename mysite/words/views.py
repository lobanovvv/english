from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Countries
import random

countries_list = []


def index(request):
    answers = []
    global countries_list

    if not countries_list:
        countries_list = list(Countries.objects.filter(oxford_chapter='A2U1'))
    answers_list = list(Countries.objects.values('nationalities'))

    # Countdown counter
    countries_left = len(countries_list)
    # Count of countries in db
    countries_count = len(list(Countries.objects.filter(oxford_chapter='A2U1')))
    # Get one country_info and del it from list
    country_info = countries_list.pop(random.randrange(countries_left))
    # Answers nationalities
    answers.append(str(country_info.nationalities))
    random_numbers = random.sample(range(countries_count), 3)
    for num in random_numbers:
        answers.append(answers_list.pop(num)['nationalities'])
    random.shuffle(answers)

    template = loader.get_template('words/index.html')
    context = {
        'country_info': country_info,
        'countries_left': countries_left,
        'countries_count': countries_count,
        'nationalities': answers,
    }
    return HttpResponse(template.render(context, request))
