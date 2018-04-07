from django.db import models

class Kraj(models.Model):
	idKraj = models.AutoField(primary_key=True)
	nazwa = models.CharField(max_length=255)

class Adres_zamieszkania(models.Model):
	idAdresZamieszkania = models.AutoField(primary_key=True)
	ulica = models.CharField(max_length=255)
	numerBudynku = models.CharField(max_length=5)
	numerLokalu = models.CharField(max_length=5)
	kodPocztowy = models.CharField(max_length=6)
	miejscowosc = models.CharField(max_length=255)
	idKraj = models.ForeignKey(Kraj, on_delete=models.CASCADE)

class Osoba(models.Model):
	idOsoba = models.AutoField(primary_key=True)
	imie = models.CharField(max_length=60)
	nazwisko = models.CharField(max_length=60)
	pesel = models.CharField(max_length=11)
	idAdresZamieszkania = models.ForeignKey(Adres_zamieszkania, on_delete=models.CASCADE)

class Kryterium(models.Model):
	idKryterium = models.AutoField(primary_key=True)
	dlugoscGlosowania = models.IntegerField()
	iloscPoprartychKandydatow = models.IntegerField()

class Wybor(models.Model):
	idWybor = models.AutoField(primary_key=True)
	nazwa = models.CharField(max_length=255)
	dataRozpoczecia = models.DateTimeField('data rozpoczecia')
	dataZakonczenia = models.DateTimeField('data zakonczenia')
	opis = models.CharField(max_length=255)
	idKryterium = models.ForeignKey(Kryterium, on_delete=models.CASCADE)

class Kandydat(models.Model):
	idKandydat = models.AutoField(primary_key=True)
	idOsoba = models.ForeignKey(Osoba, on_delete=models.CASCADE)
	idWybor = models.ForeignKey(Wybor, on_delete=models.CASCADE)

class Uprawniony(models.Model):
	idUprawniony = models.AutoField(primary_key=True)
	idOsoba = models.ForeignKey(Osoba, on_delete=models.CASCADE)
	idWybor = models.ForeignKey(Wybor, on_delete=models.CASCADE)

class Oddany_glos(models.Model):
	idOddanyGlos = models.AutoField(primary_key=True)
	dataOddaniaGlosu = models.DateTimeField('data oddania glosu')
	idUprawniony = models.ForeignKey(Uprawniony, on_delete=models.CASCADE)
	idWybor = models.ForeignKey(Wybor, on_delete=models.CASCADE)
