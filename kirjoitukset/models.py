from django.db import models
from django.urls import reverse


class Kirjoitus(models.Model):
    kirjoittaja = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    otsikko = models.CharField(max_length=100)
    teksti = models.TextField()

    def __str__(self):
        return self.otsikko

    def get_absolute_url(self):
        return reverse('koti')
