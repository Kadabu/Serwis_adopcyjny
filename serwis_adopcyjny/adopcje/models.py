from django.db import models


PŁEĆ = (
    (1, "samiec"),
    (2, "samica"),
)

KOTY = (
    (1, "tak"),
    (2, "nie"),
    (3, "do sprawdzenia"),
)

WOJEWÓDZTWO = (
    (1, "dolnośląskie"),
    (2, "kujawsko-pomorskie"),
    (3, "lubelskie"),
    (4, "lubuskie"),
    (5, "łódzkie"),
    (6, "małopolskie"),
    (7, "mazowieckie"),
    (8, "opolskie"),
    (9, "podkarpackie"),
    (10, "podlaskie"),
    (11, "pomorskie"),
    (12, "śląskie"),
    (13, "świętokrzyskie"),
    (14, "warmińsko-mazurskie"),
    (15, "wielkopolskie"),
    (16, "zachodniopomorskie"),
)

def validate_age(age):
    if age < 0 or age > 20:
        raise ValidationError("Podaj wiek w zakresie od 0 do 20 lat")

def validate_weight(age):
    if weight < 0 or weight > 80:
        raise ValidationError("Podaj wagę w zakresie od 0 do 80 kg")


class Category(models.Model):
    nazwa = models.CharField(max_length=64)

    def __str__(self):
        return self.nazwa


class Dog(models.Model):
    imię = models.CharField(max_length=64)
    płeć = models.IntegerField(choices=PŁEĆ)
    wiek = models.IntegerField(default=0, validators=[validate_age])
    waga = models.IntegerField(default=0, validators=[validate_weight])
    zdjęcie = models.ImageField(upload_to="documents/", default=None)
    województwo = models.IntegerField(choices=WOJEWÓDZTWO)
    miejscowość = models.CharField(max_length=64)
    akceptuje_koty = models.IntegerField(choices=KOTY)
    dom_bez_psów = models.BooleanField(default=False)
    dom_bez_suczek = models.BooleanField(default=False)
    możliwy_transport = models.BooleanField(default=False)
    adopcja_za_granicę = models.BooleanField(default=False)
    kategorie = models.ManyToManyField(Category)




