from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Countries


def index(request):
    countries = Countries.objects.all()
    country =
    template = loader.get_template('words/index.html')
    context = {
        'countries': countries,
    }
    return HttpResponse(template.render(context, request))
