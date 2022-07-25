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

    
    template = loader.get_template('words/index.html')
    context = {
        'country_info': nationalities.current_row,
        'answers': nationalities.get_shuffled_answers(),
        'countries_left': nationalities.get_number_of_remained_rows(),
        'countries_count': nationalities.count_of_all_rows,
        'is_correct': nationalities.is_correct,
    }
    return HttpResponse(template.render(context, request))
