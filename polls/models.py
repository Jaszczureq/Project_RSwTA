from django.db import models

class Adres_zamieszkania(models.Model):
	idAdresZamieszkania = models.IntegerField();
	ulica = models.CharField(max_length=255)
	numerBudynku = models.CharField(max_length=5)
	numerLokalu = models.CharField(max_length=5)
	kodPocztowy = models.CharField(max_length=6)
	miejscowosc = models.CharField(max_length=255)
	idKraj = models.IntegerField();
