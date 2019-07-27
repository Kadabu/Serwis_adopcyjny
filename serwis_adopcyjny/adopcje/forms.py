from django import forms
from django.contrib.auth.models import User
from .models import Dog, DogCategories, Message, AdoptionForm, REGION, CATEGORIES



class AddCategoriesForm(forms.ModelForm):
    class Meta:
        model = DogCategories
        exclude = ['dog']


class AddDogForm(forms.ModelForm):
    class Meta:
        model = Dog
        exclude = ['date_added', 'categories', 'user']


class AdoptDogForm(forms.ModelForm):
     class Meta:
         model = AdoptionForm
         exclude = ['dog']

class DeleteCategoriesForm(forms.ModelForm):
    class Meta:
        model = DogCategories
        exclude = ['dog']


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        exclude = ['dog', 'date_sent']


class SearchForm(forms.Form):
    category = forms.MultipleChoiceField(choices=CATEGORIES, widget=forms.CheckboxSelectMultiple)
    region = forms.MultipleChoiceField(choices=REGION, widget=forms.CheckboxSelectMultiple)


class SortForm(forms.Form):
    sort_by = forms.ChoiceField(choices=(
        (1, "Sortuj według daty dodania - od najnowszych"),
        (2, "Sortuj według daty dodania - od najstarszych"),
        (3, "Sortuj według wieku - rosnąco"),
        (4, "Sortuj według wieku - malejąco"),
        (5, "Sortuj według wagi - rosnąco"),
        (6, "Sortuj według wagi - malejąco"),
        (7, "Sortuj losowo")))


class LoginForm(forms.Form):
    username = forms.CharField(strip=True)
    password = forms.CharField(widget=forms.PasswordInput)


class AddUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "email")
    password_1 = forms.CharField(widget=forms.PasswordInput)
    password_2 = forms.CharField(widget=forms.PasswordInput)



