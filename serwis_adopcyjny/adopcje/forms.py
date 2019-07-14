from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re
from .models import *



class AddDogForm(forms.ModelForm):
    class Meta:
        model = Dog
        exclude = ['dodany', 'kategorie']

#poprawić kategorie, tak, żeby były wielokrotnego wyboru
#czy zrobic to ręcznie: każda nowa kategoria dodaje się do Choices???