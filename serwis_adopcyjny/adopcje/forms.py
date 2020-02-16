from django import forms
from django.contrib.auth.models import User
from .models import Dog, Picture, CATEGORIES, REGION, SEX


class AcceptDogForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = ["accepted"]


class AddDogForm(forms.ModelForm):
    class Meta:
        model = Dog
        exclude = ['date_added', 'user', 'accepted']


class AddUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email"]
    password_1 = forms.CharField(widget=forms.PasswordInput)
    password_2 = forms.CharField(widget=forms.PasswordInput)
    consent = forms.BooleanField()
    terms_of_use = forms.BooleanField()


class EditUserForm(forms.Form):
    password_1 = forms.CharField(widget=forms.PasswordInput)
    password_2 = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()


class LoginForm(forms.Form):
    username = forms.CharField(strip=True)
    password = forms.CharField(widget=forms.PasswordInput)


class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        exclude = ['dog']


class SearchForm(forms.Form):
    sex = forms.MultipleChoiceField(choices=SEX, \
    widget=forms.CheckboxSelectMultiple)
    region = forms.MultipleChoiceField(choices=REGION, \
    widget=forms.CheckboxSelectMultiple)
    categories = forms.MultipleChoiceField(choices=CATEGORIES, \
    widget=forms.CheckboxSelectMultiple)


class SortForm(forms.Form):
    sort_by = forms.ChoiceField(choices=(
        (1, "Sortuj od najpóźniej dodanych"),
        (2, "Sortuj od najwcześniej dodanych"),
        (3, "Sortuj według wieku psa - rosnąco"),
        (4, "Sortuj według wieku psa - malejąco"),
        (5, "Sortuj losowo")))
