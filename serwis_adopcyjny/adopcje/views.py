from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, CreateView, DeleteView, FormView, UpdateView
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render


class MainView(View):

    def get(self, request):
        return render(request, "base.html")

class DogView(View):

    def get(self, request, id):
        dog = get_object_or_404(Dog, pk=id)
        ctx = {"dog": dog}
        return render(request, "dog.html", ctx)

class AddDog(View):

    def get(self, request):
        form = AddDogForm(request.GET)
        return render(request, "add_dog.html", {"form": form})

    def post(self, request):
        form = AddDogForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('/radysiaki/')
        else:
            form = AddDogForm(request.GET)
            return render(request, "add_dog.html", {"form": form})

class EditDog(UpdateView):

        model = Dog
        fields = ('name', 'sex', 'weight', 'age', 'picture', 'region', 'town', 'accepts_cats', 'house_with_male_dog',
                  'house_with_female_dog', 'transport', 'adoption_abroad', 'description')
        template_name = 'dog_update_form.html'
        success_url = reverse_lazy("main-page")



