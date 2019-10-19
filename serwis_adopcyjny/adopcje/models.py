from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField


CATEGORIES = (
    (1, "mikropsy"),
    (2, "wielkopsy"),
    (3, "przegubowce"),
    (4, "czarnulki"),
    (5, "białaski"),
    (6, "rudzielce"),
    (7, "buraski"),
    (8, "łaciate krówki"),
    (9, "włochacze"),
    (10, "młodzież"),
    (11, "starszaki"),
)

CATS = (
    (1, "tak"),
    (2, "do sprawdzenia"),
    (3, "eksterminator kotów"),
)

DOGS_PLACE = (
      (1, "w domu/mieszkaniu"),
      (2, "w domu/mieszkaniu w klatce kenelowej"),
      (3, "w ogrodzie"),
      (4, "w ogrodzie w kojcu"),
)

OWNER = (
    (1, "dla mnie"),
    (2, "dla kogoś innego"),
)

PLACE = (
    (1, "w domu z ogrodem"),
    (2, "w bloku/kamienicy"),
    (2, "w innym miejscu"),
)

REGION = (
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

SEX = (
    (1, "pies"),
    (2, "suczka"),
)

YES_NO = (
    (1, "tak"),
    (2, "nie"),
)


def validate_age(age):

    if age < 0 or age > 20:
        raise ValidationError("Podaj wiek w zakresie od 0 do 20 lat")


def validate_weight(weight):

    if weight < 0 or weight > 80:
        raise ValidationError("Podaj wagę w zakresie od 0 do 80 kg")


class Dog(models.Model):

    name = models.CharField(max_length=64)
    sex = models.IntegerField(choices=SEX, default=1)
    age = models.IntegerField(default=0, validators=[validate_age])
    weight = models.IntegerField(default=0, validators=[validate_weight])
    region = models.IntegerField(choices=REGION, default=1)
    town = models.CharField(max_length=64)
    accepts_cats = models.IntegerField(choices=CATS, default=1)
    house_with_male_dog = models.IntegerField(choices=YES_NO, default=1)
    house_with_female_dog = models.IntegerField(choices=YES_NO, default=1)
    transport = models.IntegerField(choices=YES_NO, default=1)
    adoption_abroad = models.IntegerField(choices=YES_NO, default=1)
    description = models.TextField()
    categories = MultiSelectField(choices=CATEGORIES, default=1)
    date_added = models.DateTimeField(auto_now_add=True)
    contact_data = models.CharField(max_length=64)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Picture(models.Model):
    picture = models.ImageField(upload_to="documents/", null=True, blank=True)
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    profile = models.BooleanField(default=False)


class Message(models.Model):
    content = models.TextField()
    e_mail = models.EmailField()
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    date_sent = models.DateField(auto_now_add=True)


class AdoptionForm(models.Model):
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE, default=1)
    dog_owner = models.IntegerField(choices=YES_NO)
    family_agree = models.IntegerField(choices=YES_NO)
    place_type = models.IntegerField(choices=PLACE)
    house_owner = models.CharField(max_length=64)
    floor = models.CharField(max_length=64, null=True, blank=True)
    fence = models.CharField(max_length=32, null=True, blank=True)
    dogs_place = models.IntegerField(choices=DOGS_PLACE)
    time_alone = models.IntegerField()
    walks = models.IntegerField()
    beh_problems = models.TextField()
    children = models.CharField(max_length=128)
    pets_owned = models.CharField(max_length=128)
    prev_dogs = models.TextField()
    location = models.CharField(max_length=64)
    e_mail = models.EmailField()
    phone = models.CharField(max_length=32, null=True, blank=True)
