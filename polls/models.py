# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone


class Kraj(models.Model):
    nazwa = models.CharField(max_length=255)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name_plural = "Kraje"


class Adres_zamieszkania(models.Model):
    ulica = models.CharField(max_length=255)
    numerBudynku = models.CharField(max_length=5)
    numerLokalu = models.CharField(max_length=5, blank=True)
    kodPocztowy = models.CharField(max_length=6)
    miejscowosc = models.CharField(max_length=255)
    kraj = models.ForeignKey(Kraj, on_delete=models.CASCADE)

    def __str__(self):
        str_to_return = str(self.id) + ' ' + self.ulica + ' ' + self.numerBudynku
        if self.numerLokalu:
            str_to_return += '/' + self.numerLokalu
        str_to_return += ' ' + self.kodPocztowy + ' ' + self.miejscowosc
        return str_to_return

    class Meta:
        verbose_name_plural = "Adresy_zamieszkania"


class Osoba(models.Model):
    imie = models.CharField(max_length=60)
    nazwisko = models.CharField(max_length=60)
    pesel = models.CharField(max_length=11)
    adresZamieszkania = models.OneToOneField(Adres_zamieszkania, on_delete=models.CASCADE)

    def __str__(self):
        return self.imie + ' ' + self.nazwisko + ' ' + self.pesel

    class Meta:
        verbose_name_plural = "Osoby"


class Kryterium(models.Model):
    dlugoscGlosowania = models.IntegerField()
    iloscPoprartychKandydatow = models.IntegerField()
    votes = models.IntegerField(default=-1)

    def __str__(self):
        return "Kryterium: " + str(self.id)

    class Meta:
        verbose_name_plural = "Kryteria"


class Wybor(models.Model):
    nazwa = models.CharField(default='', max_length=255)
    dataRozpoczecia = models.DateTimeField(default=timezone.now)
    dataZakonczenia = models.DateTimeField(default=timezone.now)
    opis = models.CharField(max_length=255, default='')
    kryterium = models.ManyToManyField(Kryterium)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.nazwa + ", ID: " + str(self.id)

    class Meta:
        verbose_name_plural = "Wybory"


class Kandydat(models.Model):
    osoba = models.OneToOneField(Osoba, on_delete=models.CASCADE)
    wybor = models.ForeignKey(Wybor, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return "Kandydat: " + str(self.id)

    class Meta:
        ordering = ['-votes']
        verbose_name_plural = "Kandydaci"
        ordering = ['-votes']


class Uprawniony(models.Model):
    osoba = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    wybor = models.ForeignKey(Wybor, on_delete=models.CASCADE, unique=False)

    def __str__(self):
        return "Uprawniony: " + str(self.id)

    class Meta:
        verbose_name_plural = "Uprawnieni"


class Oddany_glos(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    dataOddaniaGlosu = models.DateTimeField('data oddania glosu')
    wybor = models.ForeignKey(Wybor, on_delete=models.CASCADE)

    def get_username(self):
        return self.user.objects.first().username

    def __str__(self):
        return "Oddany głos: " + str(self.id)

    class Meta:
        verbose_name_plural = "Oddane_głosy"
