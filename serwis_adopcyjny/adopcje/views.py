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
from templated_docs import fill_template
from templated_docs.http import FileResponse



class MainView(View):

    def get(self, request):
        dogs = Dog.objects.order_by('date_added').reverse()
        return render(request, "dogs.html", {"dogs": dogs})

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
    fields = ('name', 'sex', 'weight', 'age',
              'region', 'town', 'accepts_cats', 'picture_1', 'picture_2', 'picture_3', 'picture_4', 'picture_5',
              'picture_6', 'house_with_male_dog', 'house_with_female_dog', 'transport', 'adoption_abroad', 'description',
              'contact_data')
    template_name = 'dog_update_form.html'


class DeleteDog(View):

    def get(self, request, id):
        dog = get_object_or_404(Dog, pk=id)
        dog.delete()
        return HttpResponseRedirect('/radysiaki/')

class AddCategory(View):

    def get(self, request, id):
        form = AddCategoriesForm(request.GET)
        dog = get_object_or_404(Dog, pk=id)
        return render(request, "categories_form.html", {"form": form, "dog": dog})

    def post(self, request, id):
        dog = Dog.objects.get(pk=id)
        category = Category.objects.get(id=request.POST.get('category'))
        DogCategories.objects.create(dog=dog, category=category)

        return HttpResponseRedirect('/kategorie_dodaj/{}'.format(id))

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

        return HttpResponseRedirect('/pies/{}'.format(d_id))

class MessageView(View):

    def get(self, request, id):
        form = MessageForm(request.GET)
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


class AdoptionFormView(View):

    def get(self, request, id):
        form = AdoptDogForm(request.GET)
        dog = get_object_or_404(Dog, pk=id)
        return render(request, "message.html", {"form": form})

    def post(self, request, id):
        form = AddDogForm(request.POST)
        dog = get_object_or_404(Dog, pk=id)
        field_1 = request.POST.get('field_1')
        field_2 = request.POST.get('field_2')
        field_3 = request.POST.get('field_3')
        field_4 = request.POST.get('field_4')
        field_5 = request.POST.get('field_5')
        field_6 = request.POST.get('field_6')
        field_7 = request.POST.get('field_7')
        field_8 = request.POST.get('field_8')
        field_9 = request.POST.get('field_9')
        field_10 = request.POST.get('field_10')
        field_11 = request.POST.get('field_11')
        field_12 = request.POST.get('field_12')
        field_13 = request.POST.get('field_13')
        field_14 = request.POST.get('field_14')
        field_15 = request.POST.get('field_15')
        field_16 = request.POST.get('field_16')
        AdoptionForm.objects.create(dog=dog, field_1=field_1, field_2=field_2, field_3=field_3, field_4=field_4,
                                    field_5=field_5, field_6=field_6, field_7=field_7, field_8=field_8, field_9=field_9,
                                    field_10=field_10,  field_11=field_11, field_12=field_12, field_13=field_13,
                                    field_14=field_14, field_15=field_15, field_16=field_16)
        return HttpResponseRedirect('/radysiaki/')

"""class AdoptionFormsView"""

"""class SearchView"""

#powiązać psy z Userami (chyba że będzie tylko 1)
#usuwanie zdjęć
#dokumentacja
#format daty
#formularz logowania, wylogowywania itd.
#opcja sortowania listy psów wg użytkownika(np. najnowsze, najstarsze)

