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
nationalities = None


def index(request):
    global nationalities

# TODO: Валится на случайном количестве ответов, нужно доделать счетчики всего и осталось ответов и
#           посмотреть что они покажут

    if request.POST:
        print('=============== POST WAY')
        if request.POST.get('choice', '') == nationalities.correct_answer:
            nationalities.is_correct = 'CORRECT'
        else:
            nationalities.is_correct = 'WRONG'
        nationalities.extract_current_row()
    else:
        print('=============== EMPTY WAY')
        is_correct = ''
        nationalities = ColumnChoice(base_column_name='country', 
                                            answer_column_name='nationalities',
                                            filter={"oxford_chapter":"A2U1"})
        answers = nationalities.get_shuffled_answers()

    # # ----------
    # if not countries_list:
    #     countries_list = list(Countries.objects.filter(oxford_chapter='A2U1'))
    # # ----------
    # answers_list = list(Countries.objects.values('nationalities'))

    # # COUNTER
    # # Countdown counter
    # # -----------
    # countries_left = len(countries_list)
    # # Count of countries in db
    # # -----------
    # countries_count = len(list(Countries.objects.filter(oxford_chapter='A2U1')))

    # # GET COUNTRY
    # # Get one country information and del it from list
    # # ---------
    # country_info = countries_list.pop(random.randrange(countries_left))
    # # Record country name to global variable for comparison later with customer answer
    # correct_answer = country_info.nationalities

    # # ANSWERS NATIONALITIES
    # # Add correct answer
    # answers.append(str(country_info.nationalities))
    # # Add random answers
    # # ------------
    # random_numbers = random.sample(range(countries_count), 3)
    # for num in random_numbers:
    #     answers.append(answers_list.pop(num)['nationalities'])
    # # Shuffle all answers
    # random.shuffle(answers)

    template = loader.get_template('words/index.html')
    context = {
        'country_info': nationalities.current_row,
        'answers': nationalities.get_shuffled_answers(),
        # 'countries_left': countries_left,
        # 'countries_count': countries_count,
        'is_correct': nationalities.is_correct,
    }
    return HttpResponse(template.render(context, request))
