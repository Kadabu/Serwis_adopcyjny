from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User



SEX = (
    (1, "pies"),
    (2, "suczka"),
)

CATS = (
    (1, "tak"),
    (2, "nie"),
    (3, "do sprawdzenia"),
)

YES_NO = (
    (1, "tak"),
    (2, "nie"),
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

CATEGORIES = (
    (1, "wielkopsy"),
    (2, "maluchy"),
    (3, "czarnulki"),
    (4, "białaski"),
    (5, "rudzielce"),
    (6, "łaciate krówki"),
    (7, "kłapouszki"),
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

DOGS_PLACE = (
      (1, "w domu/mieszkaniu"),
      (2, "w domu/mieszkaniu w klatce kenelowej"),
      (3, "w ogrodzie"),
      (4, "w ogrodzie w kojcu"),
)


def validate_age(age):

    if age < 0 or age > 20:
        raise ValidationError("Podaj wiek w zakresie od 0 do 20 lat")


def validate_weight(weight):

    if weight < 0 or weight > 80:
        raise ValidationError("Podaj wagę w zakresie od 0 do 80 kg")


class Category(models.Model):
    name = models.CharField(max_length=64)
    def __str__(self):
        return self.name


class Dog(models.Model):

    name = models.CharField(max_length=64)
    sex = models.IntegerField(choices=SEX)
    age = models.IntegerField(default=0, validators=[validate_age])
    weight = models.IntegerField(default=0, validators=[validate_weight])
    picture_1 = models.ImageField(upload_to="documents/", default=None)
    picture_2 = models.ImageField(upload_to="documents/", default=None)
    picture_3 = models.ImageField(upload_to="documents/", default=None)
    picture_4 = models.ImageField(upload_to="documents/", default=None)
    picture_5 = models.ImageField(upload_to="documents/", default=None)
    picture_6 = models.ImageField(upload_to="documents/", null=True, blank=True)
    region = models.IntegerField(choices=REGION, default=1)
    town = models.CharField(max_length=64)
    accepts_cats = models.IntegerField(choices=CATS, default=1)
    house_with_male_dog = models.IntegerField(choices=YES_NO, default=1)
    house_with_female_dog = models.IntegerField(choices=YES_NO, default=1)
    transport = models.IntegerField(choices=YES_NO, default=1)
    adoption_abroad = models.IntegerField(choices=YES_NO, default=1)
    description = models.TextField()
    categories = models.ManyToManyField(Category, through="DogCategories")
    date_added = models.DateTimeField(auto_now_add=True)
    contact_data = models.CharField(max_length=64)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/radysiaki/"


class DogCategories(models.Model):
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)


class Message(models.Model):
    content = models.TextField()
    e_mail = models.CharField(max_length=64) #dodać walidację mejla
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    date_sent = models.DateField(auto_now_add=True)


class AdoptionForm(models.Model):
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE, null=True)
    field_1 = models.IntegerField(choices=YES_NO)
    field_2 = models.IntegerField(choices=YES_NO)
    field_3 = models.IntegerField(choices=PLACE)
    field_4 = models.CharField(max_length=64)
    field_5 = models.CharField(max_length=64,null=True, blank=True)
    field_6 = models.IntegerField(choices=YES_NO, null=True, blank=True)
    field_7 = models.IntegerField(choices=DOGS_PLACE)
    field_8 = models.IntegerField()
    field_9 = models.IntegerField()
    field_10 = models.TextField()
    field_11 = models.CharField(max_length=128)
    field_12 = models.CharField(max_length=128)
    field_13 = models.TextField()
    field_14 = models.CharField( max_length=64)
    field_15 = models.EmailField()  # walidacja
    field_16 = models.CharField(max_length=32)  # walidacja







