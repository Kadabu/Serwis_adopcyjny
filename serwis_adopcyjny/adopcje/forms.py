from django import forms
from django.contrib.auth.models import User
from .models import AdoptionForm, Dog, Message, Picture, CATEGORIES, REGION, SEX



class AddDogForm(forms.ModelForm):
    class Meta:
        model = Dog
        exclude = ['date_added', 'user']


class AdoptDogForm(forms.ModelForm):
     class Meta:
         model = AdoptionForm
         exclude = ['dog']


class AddUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "email")
    password_1 = forms.CharField(widget=forms.PasswordInput)
    password_2 = forms.CharField(widget=forms.PasswordInput)


class LoginForm(forms.Form):
    username = forms.CharField(strip=True)
    password = forms.CharField(widget=forms.PasswordInput)


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        exclude = ['dog', 'date_sent']


class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        exclude = ['dog']


class SearchForm(forms.Form):
    sex = forms.MultipleChoiceField(choices=SEX, widget=forms.CheckboxSelectMultiple)
    region = forms.MultipleChoiceField(choices=REGION, widget=forms.CheckboxSelectMultiple)
    categories = forms.MultipleChoiceField(choices=CATEGORIES, widget=forms.CheckboxSelectMultiple)


class SortForm(forms.Form):
    sort_by = forms.ChoiceField(choices=(
        (1, "Sortuj według daty dodania - od najnowszych"),
        (2, "Sortuj według daty dodania - od najstarszych"),
        (3, "Sortuj według wieku - rosnąco"),
        (4, "Sortuj według wieku - malejąco"),
        (5, "Sortuj według wagi - rosnąco"),
        (6, "Sortuj według wagi - malejąco"),
        (7, "Sortuj losowo")))
