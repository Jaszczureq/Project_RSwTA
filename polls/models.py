from django.db import models
 
 
class Kraj(models.Model):
    #idKraj = models.AutoField(primary_key=True)
    nazwa = models.CharField(max_length=255)
    def __str__(self):
        return self.nazwa
    class Meta:
        verbose_name_plural = "Kraje"
 
 
class Adres_zamieszkania(models.Model):
    #idAdresZamieszkania = models.AutoField(primary_key=True)
    ulica = models.CharField(max_length=255)
    numerBudynku = models.CharField(max_length=5)
    numerLokalu = models.CharField(max_length=5, blank=True)
    kodPocztowy = models.CharField(max_length=6)
    miejscowosc = models.CharField(max_length=255)
    votes = models.IntegerField(default = 0)
    kraj = models.ForeignKey(Kraj, on_delete=models.CASCADE)
    def __str__(self):
        str_to_return = ""+self.ulica+' '+self.numerBudynku
        if self.numerLokalu:
            str_to_return += '/'+self.numerLokalu
        str_to_return +=' '+self.kodPocztowy+' '+self.miejscowosc
        return str_to_return
    class Meta:
        verbose_name_plural = "Adresy_zamieszkania"
 
 
class Osoba(models.Model):
    #idOsoba = models.AutoField(primary_key=True)
    imie = models.CharField(max_length=60)
    nazwisko = models.CharField(max_length=60)
    pesel = models.CharField(max_length=11)
    adresZamieszkania = models.ForeignKey(Adres_zamieszkania, on_delete=models.CASCADE)
    def __str__(self):
        return self.imie+' '+self.nazwisko+' '+self.pesel
    class Meta:
        verbose_name_plural = "Osoby"
 
 
class Kryterium(models.Model):
    #idKryterium = models.AutoField(primary_key=True)
    dlugoscGlosowania = models.IntegerField()
    iloscPoprartychKandydatow = models.IntegerField()
    def __str__(self):
        return "Kryterium: "+str(self.idKryterium)
    class Meta:
        verbose_name_plural = "Kryteria"
 
 
class Wybor(models.Model):
    #idWybor = models.AutoField(primary_key=True)
    nazwa = models.CharField(max_length=255)
    dataRozpoczecia = models.DateTimeField('data rozpoczecia')
    dataZakonczenia = models.DateTimeField('data zakonczenia')
    opis = models.CharField(max_length=255)
    kryterium = models.ForeignKey(Kryterium, on_delete=models.CASCADE)
    def __str__(self):
        return self.nazwa
    class Meta:
        verbose_name_plural = "Wybory"
 
 
class Kandydat(models.Model):
    #idKandydat = models.AutoField(primary_key=True)
    osoba = models.ForeignKey(Osoba, on_delete=models.CASCADE)
    wybor = models.ForeignKey(Wybor, on_delete=models.CASCADE)
    def __str__(self):
        return "Kandydat: "+str(self.idKandydat)
    class Meta:
        verbose_name_plural = "Kandydaci"
   
 
 
class Uprawniony(models.Model):
    #idUprawniony = models.AutoField(primary_key=True)
    osoba = models.ForeignKey(Osoba, on_delete=models.CASCADE)
    wybor = models.ForeignKey(Wybor, on_delete=models.CASCADE)
    def __str__(self):
        return "Uprawniony: "+str(self.idUprawniony)
    class Meta:
        verbose_name_plural = "Uprawnieni"
 
 
class Oddany_glos(models.Model):
    #idOddanyGlos = models.AutoField(primary_key=True)
    dataOddaniaGlosu = models.DateTimeField('data oddania glosu')
    uprawniony = models.ForeignKey(Uprawniony, on_delete=models.CASCADE)
    wybor = models.ForeignKey(Wybor, on_delete=models.CASCADE)
    def __str__(self):
        return "Oddany głos: "+str(self.idOddanyGlos)
    class Meta:
        verbose_name_plural = "Oddane_głosy"
		
