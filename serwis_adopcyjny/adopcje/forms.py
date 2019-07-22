from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re
from .models import *



class AddDogForm(forms.ModelForm):
    class Meta:
        model = Dog
        exclude = ['date_added', 'categories', 'picture_2', 'picture_3', 'picture_4', 'picture_5', 'picture_6']
    picture_2 = forms.ImageField(required=False)
    picture_3 = forms.ImageField(required=False)
    picture_4 = forms.ImageField(required=False)
    picture_5 = forms.ImageField(required=False)
    picture_6 = forms.ImageField(required=False)


class AddCategoriesForm(forms.ModelForm):
    class Meta:
        model = DogCategories
        exclude = ['dog']


class DeleteCategoriesForm(forms.ModelForm):
    class Meta:
        model = DogCategories
        exclude = ['dog']


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        exclude = ['dog', 'date_sent']


class AdoptDogForm(forms.Form):
    field_1 = forms.ChoiceField(label="Czy pies, którego chcesz adoptować, to pies dla Ciebie i będzie mieszkał z Tobą?",
                                choices=YES_NO)
    field_2 = forms.ChoiceField(label="Czy wszyscy domownicy zgadzają się na psa?", choices=YES_NO)
    field_3 = forms.ChoiceField(label="Gdzie mieszkasz?", choices=PLACE)
    field_4 = forms.CharField(label="Kto jest właścicielem mieszkania lub domu, w którym mieszkasz?", max_length=64)
    field_5 = forms.CharField(label="Jeżeli mieszkasz w bloku, to na którym piętrze i czy w budynku jest winda?",
                              max_length=64, required=False)
    field_6 = forms.ChoiceField(label="Jeżeli mieszkasz w domu, to czy dom jest ogrodzony?", choices=YES_NO, required=False)
    field_7 = forms.ChoiceField(label="Gdzie będzie przebywał pies podczas Twojej nieobecności?", choices=DOGS_PLACE)
    field_8 = forms.IntegerField(label="Ile godzin maksymalnie pies będzie zostawał sam?")
    field_9 = forms.IntegerField(label="Ile razy dziennie pies będzie wychodził na spacer?")
    field_10 = forms.CharField(label="Jak zamierzasz poradzić sobie w razie problemów behawioralnych (agresja, problemy"
                                     " z zostawaniem samemu - wycie, niszczenie)?", widget=forms.Textarea)
    field_11 = forms.CharField(label="Czy w domu są dzieci, jeśli tak, to w jaki wieku?", max_length=128)
    field_12 = forms.CharField(label="Czy w domu są zwierzęta, jeśli tak, to jakie?", max_length=128)
    field_13 = forms.CharField(label="Czy miałeś wcześniej psa i co się z nim stało?", widget=forms.Textarea)
    field_14 = forms.CharField(label="W jakiej miejscowości mieszkasz?", max_length=64)
    field_15 = forms.EmailField(label="Twój e-mail")   #walidacja
    field_16 = forms.CharField(label="Twój telefon", max_length=64) #walidacja

