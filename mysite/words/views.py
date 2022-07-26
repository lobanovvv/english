import os.path

from django.http import HttpResponse
from django.template import loader


from .logics.audio import Audio
from .logics.column_choice import ColumnChoice
from mysite.settings import BASE_DIR


nationalities = None


def index(request):
    global nationalities

    if request.POST:
        nationalities.get_correct_answer()
        if request.POST.get('choice', '') == nationalities.correct_answer:
            nationalities.is_correct = 'CORRECT'
        else:
            nationalities.is_correct = 'WRONG'
        try:
            nationalities.extract_current_row()
        except ValueError:
            nationalities = ColumnChoice(base_column_name='country',
                                         answer_column_name='nationalities',
                                         filter={"oxford_chapter": "A2U1"})
        Audio.create_answer_sound(nationalities.correct_answer)
        Audio.play_audio(os.path.join(BASE_DIR, "static", "sounds", "answer_sound.mp3"))
    else:
        nationalities = ColumnChoice(base_column_name='country',
                                     answer_column_name='nationalities',
                                     filter={"oxford_chapter": "A2U1"})

    template = loader.get_template('words/index.html')
    context = {
        'country_info': nationalities.current_row,
        'answers': nationalities.get_shuffled_answers(),
        'countries_left': nationalities.get_number_of_remained_rows() + 1,
        'countries_count': nationalities.count_of_all_rows,
        'is_correct': nationalities.is_correct,
    }
    return HttpResponse(template.render(context, request))
