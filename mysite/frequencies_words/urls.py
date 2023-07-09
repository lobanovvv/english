from django.urls import path

from . import views

app_name = "frequencies_words"

urlpatterns = [
    path('', views.index, name='index'),
]