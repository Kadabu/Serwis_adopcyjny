from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re
from .models import *

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


class AddDogForm(forms.ModelForm):
    class Meta:
        model = Dog
        exclude = ['date_added', 'categories', 'picture_1''picture_2', 'picture_3', 'picture_4', 'picture_5', 'picture_6']

    picture_1 = forms.ImageField(required=False)
    picture_2 = forms.ImageField(required=False)
    picture_3 = forms.ImageField(required=False)
    picture_4 = forms.ImageField(required=False)
    picture_5 = forms.ImageField(required=False)
    picture_6 = forms.ImageField(required=False)


class AddCategoriesForm(forms.ModelForm):
    class Meta:
        model = DogCategories
        exclude = ['dog']

class DeleteCategoriesForm(forms.Form):
    class Meta:
        model = DogCategories
        exclude = ['dog']

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        exclude = ['dog', 'date_sent']

class AdoptDogForm(forms.Form):
    one = forms.ChoiceField(label="Czy pies, którego chcesz adoptować, to pies dla Ciebie i będzie mieszkał z Tobą?", choices=YES_NO)
    two = forms.ChoiceField(label="Czy wszyscy domownicy zgadzają się na psa?", choices=YES_NO)
    three = forms.ChoiceField(label="Gdzie mieszkasz?", choices=PLACE)
    four = forms.CharField(label="Kto jest właścicielem mieszkania lub domu, w którym mieszkasz?", max_length=64)
    five = forms.CharField(label="Jeżeli mieszkasz w bloku, to na którym piętrze i czy w budynku jest winda?", max_length=64, required=False)
    six = forms.ChoiceField(label="Jeżeli mieszkasz w domu, to czy dom jest ogrodzony?", choices=YES_NO, required=False)
    seven = forms.ChoiceField(label="Gdzie będzie przebywał pies podczas Twojej nieobecności?", choices=DOGS_PLACE)
    eight = forms.IntegerField(label="Ile godzin maksymalnie pies będzie zostawał sam?")
    nine = forms.IntegerField(label="Ile razy dziennie pies będzie wychodził na spacer?")
    ten = forms.CharField(label="Jak zamierzasz poradzić sobie w razie problemów behawioralnych (agresja, problemy z zostawaniem samemu - wycie, niszczenie)?", widget=forms.Textarea)
    eleven = forms.CharField(label="Czy w domu są dzieci, jeśli tak, to w jaki wieku?", max_length=128)
    twelve = forms.CharField(label="Czy w domu są zwierzęta, jeśli tak, to jakie?", max_length=128)
    thirteen = forms.CharField(label="Czy miałeś wcześniej psa i co się z nim stało?", widget=forms.Textarea)
    fourteen = forms.CharField(label="W jakiej miejscowości mieszkasz?", max_length=64)
    fifteen = forms.EmailField(label="Twój e-mail")   #walidacja    
    sixteen = forms.IntegerField(label="Twój telefon") #walidacja

