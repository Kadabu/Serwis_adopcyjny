from django.db import models
from django.core.exceptions import ValidationError



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
    picture = models.ImageField(upload_to="documents/", default=None)
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
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/pies/{}/".format(self.id)


class DogCategories(models.Model):
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)




