from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re
from .models import *



class AddCategoriesForm(forms.ModelForm):
    class Meta:
        model = DogCategories
        exclude = ['dog']


class AddDogForm(forms.ModelForm):
    class Meta:
        model = Dog
        exclude = ['date_added', 'categories']


class AdoptDogForm(forms.Form):
    dog_owner = forms.ChoiceField(label="Czy pies, którego chcesz adoptować, to pies dla Ciebie i będzie mieszkał z Tobą?",
                                  choices=YES_NO)
    family_agree = forms.ChoiceField(label="Czy wszyscy domownicy zgadzają się na psa?", choices=YES_NO)
    place_type = forms.ChoiceField(label="Gdzie mieszkasz?", choices=PLACE)
    house_owner = forms.CharField(label="Kto jest właścicielem mieszkania lub domu, w którym mieszkasz?", max_length=64)
    floor = forms.CharField(label="Jeżeli mieszkasz w bloku, to na którym piętrze i czy w budynku jest winda?",
                            max_length=64, required=False)
    fence = forms.ChoiceField(label="Jeżeli mieszkasz w domu, to czy dom jest ogrodzony?", choices=YES_NO, required=False)
    dogs_place = forms.ChoiceField(label="Gdzie będzie przebywał pies podczas Twojej nieobecności?", choices=DOGS_PLACE)
    time_alone = forms.IntegerField(label="Ile godzin maksymalnie pies będzie zostawał sam?")
    walks = forms.IntegerField(label="Ile razy dziennie pies będzie wychodził na spacer?")
    beh_problems = forms.CharField(label="Jak zamierzasz poradzić sobie w razie problemów behawioralnych "
                                  "(agresja, problemy z zostawaniem samemu - wycie, niszczenie)?", widget=forms.Textarea)
    children = forms.CharField(label="Czy w domu są dzieci, jeśli tak, to w jakim wieku?", max_length=128)
    pets_owned = forms.CharField(label="Czy w domu są zwierzęta, jeśli tak, to jakie?", max_length=128)
    prev_dogs = forms.CharField(label="Czy miałeś wcześniej psa i co się z nim stało?", widget=forms.Textarea)
    location = forms.CharField(label="W jakiej miejscowości mieszkasz?", max_length=64)
    e_mail = forms.EmailField(label="Twój e-mail")
    phone = forms.CharField(label="Twój telefon", max_length=64)


class DeleteCategoriesForm(forms.ModelForm):
    class Meta:
        model = DogCategories
        exclude = ['dog']


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        exclude = ['dog', 'date_sent']



class SearchForm(forms.ModelForm):
    class Meta:
        model = DogCategories
        exclude = ['dog']


class SortForm(forms.Form):
    sort_by = forms.ChoiceField(label="Sortuj według", choices=(
        (1, "daty dodania - od najnowszych"),
        (2, "daty dodania - od najstarszych"),
        (3, "wieku - rosnąco"),
        (4, "wieku - malejąco"),
        (5, "wagi - rosnąco"),
        (6, "wagi - malejąco"),
        (7, "losowo")))

