from django.db import models


class CountryNationalitiesLanguage(models.Model):
    country = models.CharField(max_length=100)
    nationalities = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    oxford_exist = models.BooleanField(default=False)
