from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re
from .models import *



class AddDogForm(forms.ModelForm):
    class Meta:
        model = Dog
        exclude = ['date_added', 'categories']

class AddCategoriesForm(forms.ModelForm):
    class Meta:
        model = DogCategories
        fields = '__all__'



