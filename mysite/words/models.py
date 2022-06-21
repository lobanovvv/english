from django.db import models


class Countries(models.Model):
    country = models.CharField(max_length=100)
    nationalities = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    oxford_chapter = models.CharField(max_length=10)
