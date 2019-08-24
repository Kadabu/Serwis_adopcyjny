from django import forms
from django.contrib.auth.models import User
from .models import Picture, Category, Dog, DogCategories, Message, AdoptionForm, REGION


categories_list = []
for cat in Category.objects.all():
    cat_set = []
    cat_set.append(cat.id)
    cat_set.append(cat.name)
    cat_tup = tuple(cat_set)
    categories_list.append(cat_tup)

CATEGORIES = tuple(categories_list)


class AddCategoriesForm(forms.ModelForm):
    class Meta:
        model = DogCategories
        exclude = ['dog', 'category']
    categories = forms.MultipleChoiceField(choices=CATEGORIES, widget=forms.CheckboxSelectMultiple)


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class AddDogForm(forms.ModelForm):
    class Meta:
        model = Dog
        exclude = ['date_added', 'categories', 'user']
    categories = forms.MultipleChoiceField(choices=CATEGORIES, widget=forms.CheckboxSelectMultiple)


class AdoptDogForm(forms.ModelForm):
     class Meta:
         model = AdoptionForm
         exclude = ['dog']


class DeleteCategoriesForm(forms.ModelForm):
    class Meta:
        model = DogCategories
        exclude = ['dog']


class EditDogForm(forms.ModelForm):
    class Meta:
        model = Dog
        exclude = ['date_added', 'categories', 'user']


class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        exclude = ['dog']
        

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        exclude = ['dog', 'date_sent']


class SearchForm(forms.Form):
    region = forms.MultipleChoiceField(choices=REGION, widget=forms.CheckboxSelectMultiple)
    category = forms.MultipleChoiceField(choices=CATEGORIES, widget=forms.CheckboxSelectMultiple)


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
