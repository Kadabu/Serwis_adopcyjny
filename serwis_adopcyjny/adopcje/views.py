from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, DeleteView
from .models import Category, Dog, DogCategories, Message, AdoptionForm
from .forms import AddCategoriesForm, AddCategoryForm, AddDogForm, AdoptDogForm, DeleteCategoriesForm, EditDogForm, \
    MessageForm, SearchForm, SortForm, LoginForm, AddUserForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


class MainView(View):

    def get(self, request):
        form = SortForm()
        dogs = Dog.objects.all().order_by('date_added').reverse()
        return render(request, "dogs.html", {"dogs": dogs, "form": form})

    def post(self, request):
        form = SortForm(request.POST)
        sort_by = request.POST.get('sort_by')
        dogs = Dog.objects.all()
        if sort_by == '1':
            dogs = dogs.order_by('date_added').reverse()
        if sort_by == '2':
            dogs = dogs.order_by('date_added')
        if sort_by == '3':
            dogs = dogs.order_by('age')
        if sort_by == '4':
            dogs = dogs.order_by('age').reverse()
        if sort_by == '5':
            dogs = dogs.order_by('weight')
        if sort_by == '6':
            dogs = dogs.order_by('weight').reverse()
        if sort_by == '7':
            dogs = dogs.order_by('?')
        return render(request, "dogs.html", {"dogs": dogs, "form": form})


class ReadMoreView(TemplateView):

    template_name = 'info.html'

    def get_context_data(self):
        message = "Opis w budowie"
        return {'message': message}


class DogView(View):

    def get(self, request, id):

        dog = get_object_or_404(Dog, pk=id)
        ctx = {"dog": dog}
        return render(request, "dog.html", ctx)


class AddDog(View):

    def get(self, request):
        form = AddDogForm()
        return render(request, "add_dog.html", {"form": form})

    def post(self, request):
        form = AddDogForm(request.POST, request.FILES)

        if form.is_valid():
            dog = Dog.objects.create(
                name=form.cleaned_data["name"],
                sex=form.cleaned_data["sex"],
                age=form.cleaned_data["age"],
                weight=form.cleaned_data["weight"],
                picture_1=form.cleaned_data["picture_1"],
                picture_2=form.cleaned_data["picture_2"],
                picture_3=form.cleaned_data["picture_3"],
                picture_4=form.cleaned_data["picture_4"],
                picture_5=form.cleaned_data["picture_5"],
                picture_6=form.cleaned_data["picture_6"],
                picture_7=form.cleaned_data["picture_7"],
                picture_8=form.cleaned_data["picture_8"],
                region=form.cleaned_data["region"],
                town=form.cleaned_data["town"],
                accepts_cats=form.cleaned_data["accepts_cats"],
                house_with_male_dog=form.cleaned_data["house_with_male_dog"],
                house_with_female_dog=form.cleaned_data["house_with_female_dog"],
                transport=form.cleaned_data["transport"],
                adoption_abroad=form.cleaned_data["adoption_abroad"],
                description=form.cleaned_data["description"],
                contact_data=form.cleaned_data["contact_data"],
                user=request.user
                )
            categories = form.cleaned_data['categories']
            categories_chosen = []
            for cat in categories:
                categories_chosen += Category.objects.filter(pk=int(cat))
            for cat in categories_chosen:
                DogCategories.objects.create(dog=dog, category=cat)

            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/dodaj/')


class EditDog(View):

    def get(self, request, id):
        dog = get_object_or_404(Dog, pk=id)
        form = EditDogForm(instance=dog)
        if request.user == dog.user or request.user.is_superuser:
            return render(request, "edit_dog.html", {"form": form, "dog": dog})
        else:
            return render(request, "info.html", {"message": "Nie możesz edytować tego ogłoszenia"})

    def post(self, request, id):
        dog = get_object_or_404(Dog, pk=id)
        form = EditDogForm(data=request.POST, files=request.FILES, instance=dog)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/pies/{}'.format(dog.id))


class DeleteDog(View):
                    
    def get(self, request, id):
        dog = get_object_or_404(Dog, pk=id)
        if request.user == dog.user or request.user.is_superuser:
            dog.delete()
            return HttpResponseRedirect('/')
        else:
            return render(request, "info.html", {"message": "Nie możesz usunąć tego ogłoszenia"})


class AddCategory(View):

    def get(self, request, id):
        form = AddCategoriesForm()
        dog = get_object_or_404(Dog, pk=id)
        if request.user == dog.user or request.user.is_superuser:
            return render(request, "categories_form.html", {"form": form, "dog": dog})
        else:
            return render(request, "info.html", {"message": "Nie możesz edytować tego ogłoszenia"})

    def post(self, request, id):
        form = AddCategoriesForm(request.POST)
        dog = Dog.objects.get(pk=id)
        if form.is_valid():
            categories = form.cleaned_data['categories']
            categories_chosen = []
            for cat in categories:
                categories_chosen += Category.objects.filter(pk=int(cat))
            for cat in categories_chosen:
                DogCategories.objects.create(dog=dog, category=cat)              
            return HttpResponseRedirect('/edytuj/{}'.format(id))


class Categories(View):

    def get(self, request, id):
        dog = get_object_or_404(Dog, pk=id)
        return render(request, "remove_categories_form.html", {"dog": dog})


class RemoveDogCategory(View):

    def get(self, request, d_id, c_id):
        dog = get_object_or_404(Dog, pk=d_id)
        category = get_object_or_404(Category, pk=c_id)
        cat_set = DogCategories.objects.filter(dog=dog, category=category)
        if request.user == dog.user or request.user.is_superuser:
            for cat in cat_set:
                cat.delete()
                return HttpResponseRedirect('/edytuj/{}'.format(d_id))
        else:
            return render(request, "info.html", {"message": "Nie możesz edytować tego ogłoszenia"})


class NewCategory(View):

    def get(self, request):
        form = AddCategoryForm()
        return render(request, "add_category.html", {"form": form})

    def post(self, request):
        name = request.POST.get('name')
        Category.objects.create(name=name)
        return HttpResponseRedirect('/kategorie_nowa/')


class RemoveCategory(View):

    def get(self, request):
        form = AddCategoriesForm()
        categories = Category.objects.all()
        return render(request, "remove_category.html", {"form": form, "categories": categories})

    def post(self, request):
        category = Category.objects.get(id=request.POST.get('category'))
        category.delete()
        return HttpResponseRedirect('/kategorie_usun/')


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
        if request.user == dog.user or request.user.is_superuser:
            return render(request, "messages_list.html", {"messages": messages, "dog": dog})
        else:
            return render(request, "info.html", {"message": "Nie możesz przeglądać wiadomości do tego ogłoszenia"})


class MessageDelete(View):

    def get(self, request, id):
        message = get_object_or_404(Message, pk=id)
        dog = message.dog
        if request.user == dog.user or request.user.is_superuser:
            message.delete()
            return HttpResponseRedirect('/wiadomosci/{}/'.format(dog.id))
        else:
            return render(request, "info.html", {"message": "Nie możesz usunąć tej wiadomości"})


class AdoptionFormDelete(View):

    def get(self, request, id):
        adoption_form = get_object_or_404(AdoptionForm, pk=id)
        dog = adoption_form.dog
        if request.user == dog.user or request.user.is_superuser:
            adoption_form.delete()
            return HttpResponseRedirect('/ankiety/{}/'.format(dog.id))
        else:
            return render(request, "info.html", {"message": "Nie możesz usunąć tej ankiety"})


class AdoptionFormView(View):

    def get(self, request, id):
        form = AdoptDogForm()
        dog = get_object_or_404(Dog, pk=id)
        return render(request, "adoption_form.html", {"form": form})

    def post(self, request, id):
        form = AddDogForm(request.POST)
        dog = get_object_or_404(Dog, pk=id)
        AdoptionForm.objects.create(
            dog=dog,
            dog_owner=request.POST.get('dog_owner'),
            family_agree=request.POST.get('family_agree'),
            place_type=request.POST.get('place_type'),
            house_owner=request.POST.get('house_owner'),
            floor=request.POST.get('floor'),
            fence=request.POST.get('fence'),
            dogs_place=request.POST.get('dogs_place'),
            time_alone=request.POST.get('time_alone'),
            walks=request.POST.get('walks'),
            beh_problems=request.POST.get('beh_problems'),
            children=request.POST.get('children'),
            pets_owned=request.POST.get('pets_owned'),
            prev_dogs=request.POST.get('prev_dogs'),
            location=request.POST.get('location'),
            e_mail=request.POST.get('e_mail'),
            phone=request.POST.get('phone')
        )
        return HttpResponseRedirect('/')


class AdoptionFormList(View):

    def get(self, request, id):
        dog = get_object_or_404(Dog, pk=id)
        adoption_forms = AdoptionForm.objects.filter(dog=dog)
        if request.user == dog.user or request.user.is_superuser:
            return render(request, "adoption_form_list.html", {"adoption_forms": adoption_forms, "dog": dog})
        else:
            return render(request, "info.html", {"message": "Nie możesz przeglądać ankiet do tego ogłoszenia"})


class SearchView(View):

    def get(self, request):
        form = SearchForm()
        return render(request, "search_form.html", {"form": form})

    def post(self, request):
        form = SearchForm(request.POST)
        dogs = []
        if form.is_valid():
            category = form.cleaned_data['category']
            region = form.cleaned_data['region']
        else:
            form = SearchForm(request.GET)
            return render(request, "search_form.html", {"form": form})

        categories_chosen = []
        for cat in category:
            categories_chosen += Category.objects.filter(pk=int(cat))
        dogs_by_reg = []
        for reg in region:
            dogs_by_reg += Dog.objects.filter(region=int(reg))
        for dog in dogs_by_reg:
            for cat in categories_chosen:
                if cat in dog.categories.all():
                    if dog not in dogs:
                        dogs.append(dog)
        return render(request, "search_result.html", {"dogs": dogs})


class Login(View):

    def get(self, request):
        form = LoginForm()
        return render(request, "login.html", {"form": form})

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/zaloguj/')


class Logout(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')


class AddUser(View):

    def get(self, request):
        form = AddUserForm()
        return render(request, "user_form.html", {"form": form})

    def post(self, request):
        form = AddUserForm(request.POST)
        username = request.POST.get('username')
        password_1 = request.POST.get('password_1')
        password_2 = request.POST.get('password_2')
        email = request.POST.get('email')
        message = ''
        if User.objects.filter(username=username).exists():
            message += "Taki użytkownik już istnieje"
            return render(request, "user_form.html", {"form": form, "message": message})
        elif password_1 != password_2:
            message += "Wpisane hasła są niezgodne"
            return render(request, "user_form.html", {"form": form, "message": message})
        else:
            User.objects.create_user(username=username, password=password_1, email=email)
            return HttpResponseRedirect('/zaloguj/')


