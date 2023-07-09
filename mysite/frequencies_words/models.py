from django.db import models


class FrequenciesWords(models.Model):

    name = models.CharField(max_length=100)
    percent = models.IntegerField()
    level = models.CharField(max_length=2)
    expression = models.BooleanField()

    def __str__(self):
        return self.name