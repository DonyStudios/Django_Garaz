from django.db import models


class Motor(models.Model):
    znacka = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    valce = models.CharField(max_length=255)
    obsah = models.IntegerField()
    vykon = models.CharField(max_length=255)
    turbo = models.BooleanField(default=False)
    palivo = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.znacka} {self.model}"

class Brzdy(models.Model):
    znacka = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    efektivita = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.znacka} {self.model}"

class Pneu(models.Model):
    znacka = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    letni = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.znacka} {self.model}"

class Odpruzeni(models.Model):
    znacka = models.CharField(max_length=255)
    model = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.znacka} {self.model}"


class Vozidlo(models.Model):
    jmeno = models.CharField(max_length=80, verbose_name='Model vozidla', help_text='Zadejte model vozidla',
                             error_messages={'blank': 'Model vozidla musí být vyplněno'})
    vyrobce = models.CharField(max_length=50, verbose_name='vyrobce', help_text='Zadejte výrobce vozidla',
                               error_messages={'blank': 'Název výrobce musí být vyplněn'})
    typ_vozidla = models.CharField(max_length=50, verbose_name='typ', help_text='Auto,moto,kamion,traktor',
                               error_messages={'blank': 'Typ vozidla musí být vyplněn'})
    cena = models.IntegerField(help_text='v korunách')
    hmotnost = models.IntegerField(help_text='v kg')
    motorizace = models.ManyToManyField(Motor, verbose_name='Motorizace')
    brzdy = models.ManyToManyField(Brzdy, verbose_name='Brzdy')
    pneu = models.ManyToManyField(Pneu, verbose_name='Pneu')
    odpruzeni = models.ManyToManyField(Odpruzeni, verbose_name='Odpruzeni')

    class Meta:
      ordering = ["vyrobce"]
      verbose_name = "vozidlo"
      verbose_name_plural = "vozidlo"

    def __str__(self):
        return f"{self.vyrobce} {self.jmeno}"

class Ridic(models.Model):
      firstname = models.CharField(max_length=255)
      lastname = models.CharField(max_length=255)
      datum_narozeni = models.DateField()
      telefon = models.CharField(max_length=9)
      pojistovna = models.IntegerField()
      vozidlo = models.ManyToManyField(Vozidlo, verbose_name="vozidlo")

      def __str__(self):
        return f"{self.firstname} {self.lastname}"