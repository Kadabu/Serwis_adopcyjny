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
            return HttpResponseRedirect('/lista/')
        else:
            form = AddDogForm(request.GET)
            return render(request, "add_dog.html", {"form": form})

class EditDog(UpdateView):

        model = Dog
        fields = ('name', 'sex', 'weight', 'age', 'picture', 'region', 'town', 'accepts_cats', 'house_with_male_dog',
                  'house_with_female_dog', 'transport', 'adoption_abroad', 'description')
        template_name = 'dog_update_form.html'


class AddCategory(View):

    def get(self, request, id):
        form = AddCategoriesForm()
        dog = get_object_or_404(Dog, pk=id)
        return render(request, "categories_form.html", {"form": form})

    def post(self, request, id):
        dog = Dog.objects.get(pk=id)
        category = Category.objects.get(id=request.POST.get('category'))
        DogCategories.objects.create(dog=dog, category=category)

        return HttpResponseRedirect('/edytuj/{}'.format(id))

class Categories(View):

    def get(self, request, id):
        dog = get_object_or_404(Dog, pk=id)
        return render(request, "remove_categories_form.html", {"dog": dog})


class RemoveCategory(View):
    def get(self, request, d_id, c_id):
        dog = get_object_or_404(Dog, pk=d_id)
        category = get_object_or_404(Category, pk=c_id)
        cat_set = DogCategories.objects.filter(dog=dog, category=category)
        for cat in cat_set:
            cat.delete()

        return HttpResponseRedirect('/edytuj/{}'.format(d_id))

class MessageView(View):

    def get(self, request, id):
        form = MessageForm()
        dog = get_object_or_404(Dog, pk=id)
        return render(request, "message.html", {"form": form})

    def post(self, request, id):
        dog = Dog.objects.get(pk=id)
        content = request.POST.get('content')
        e_mail = request.POST.get('e_mail')
        Message.objects.create(dog=dog, content=content, e_mail=e_mail)

        return HttpResponseRedirect('/pies/{}'.format(id))


class MessagesList(View):

    def get(self, request, id):
        dog = get_object_or_404(Dog, pk=id)
        messages = Message.objects.filter(dog=dog)
        return render(request, "messages_list.html", {"messages": messages, "dog": dog})


class AdoptionForm(View):
    def get(self, request, id):
        form = AdoptDogForm(request.GET)
        dog = get_object_or_404(Dog, pk=id)
        return render(request, "message.html", {"form": form})

    def post(self, request, id):
        dog = Dog.objects.get(pk=id)
        """content = request.POST.get('content')
        e_mail = request.POST.get('e_mail')
        AdoptionForm.objects.create(dog=dog, content=content, e_mail=e_mail)"""

        return HttpResponseRedirect('/pies/{}'.format(id))


