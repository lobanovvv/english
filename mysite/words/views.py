from secrets import choice
from warnings import filters
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .logics.column_choice import ColumnChoice

from .models import Countries
import random

countries_list = []
correct_answer = ''


def index(request):
    global countries_list
    global correct_answer
    global is_correct
    answers = []

    if request.POST:
        if request.POST.get('choice', '') == correct_answer:
            is_correct = 'CORRECT'
        else:
            is_correct = 'WRONG'
    else:
        print('Enter into empty way')
        is_correct = ''
        nationalities_choice = ColumnChoice(base_column_name='country', 
                                            answer_column_name='nationalities',
                                            filter={"oxford_chapter":"A2U1"})

    # ----
    if not countries_list:
        countries_list = list(Countries.objects.filter(oxford_chapter='A2U1'))
    
    answers_list = list(Countries.objects.values('nationalities'))

    # COUNTER
    # Countdown counter
    # -----------
    countries_left = len(countries_list)
    # Count of countries in db
    # -----------
    countries_count = len(list(Countries.objects.filter(oxford_chapter='A2U1')))

    # GET COUNTRY
    # Get one country information and del it from list
    # ---------
    country_info = countries_list.pop(random.randrange(countries_left))
    # Record country name to global variable for comparison later with customer answer
    correct_answer = country_info.nationalities

    # ANSWERS NATIONALITIES
    # Add correct answer
    answers.append(str(country_info.nationalities))
    # Add random answers
    random_numbers = random.sample(range(countries_count), 3)
    for num in random_numbers:
        answers.append(answers_list.pop(num)['nationalities'])
    # Shuffle all answers
    random.shuffle(answers)

    template = loader.get_template('words/index.html')
    context = {
        'country_info': country_info,
        'countries_left': countries_left,
        'countries_count': countries_count,
        'nationalities': answers,
        'is_correct': is_correct,
    }
    return HttpResponse(template.render(context, request))
