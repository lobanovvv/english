from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<a href="frequencies_words">frequencies_words</a><br/><a href="words">words</a>')