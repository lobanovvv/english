import random

from django.http import HttpResponse
from django.template import loader

from . models import FrequenciesWords as fw

def index(request):
    template = loader.get_template("frequencies_words/index.html")

    words = []
    for item in fw.objects.all():
        words.append(item.name)

    random.shuffle(words)

    context = {
        "words": words,
    }
    return HttpResponse(template.render(context, request))