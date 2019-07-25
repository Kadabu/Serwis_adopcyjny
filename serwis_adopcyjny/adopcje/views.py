from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import UpdateView
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin



class MainView(View):

    def get(self, request):
        dogs = Dog.objects.order_by('date_added').reverse()
        return render(request, "dogs.html", {"dogs": dogs})


class DogView(View):

    def get(self, request, id):
        dog = get_object_or_404(Dog, pk=id)
        ctx = {"dog": dog}
        return render(request, "dog.html", ctx)


class AddDog(View, LoginRequiredMixin):

    def get(self, request):
        form = AddDogForm()
        return render(request, "add_dog.html", {"form": form})

    def post(self, request):
        form = AddDogForm(request.POST, request.FILES)
        name = request.POST.get("name")
        sex = request.POST.get("sex")
        age = request.POST.get("age")
        weight = request.POST.get("weight")
        picture_1 = request.FILES.get("picture_1")
        picture_2 = request.FILES.get("picture_2")
        picture_3 = request.FILES.get("picture_3")
        picture_4 = request.FILES.get("picture_4")
        picture_5 = request.FILES.get("picture_5")
        picture_6 = request.FILES.get("picture_6")
        picture_7 = request.FILES.get("picture_7")
        picture_8 = request.FILES.get("picture_8")
        region = request.POST.get("region")
        town = request.POST.get("town")
        accepts_cats = request.POST.get("accepts_cats")
        house_with_male_dog = request.POST.get("house_with_male_dog")
        house_with_female_dog = request.POST.get("house_with_female_dog")
        transport = request.POST.get("transport")
        adoption_abroad = request.POST.get("adoption_abroad")
        description = request.POST.get("description")
        contact_data = request.POST.get("contact_data")
        user = request.user
        Dog.objects.create(name=name, sex=sex, age=age, weight=weight, picture_1=picture_1,
                           picture_2=picture_2, picture_3=picture_3, picture_4=picture_4, picture_5=picture_5,
                           picture_6=picture_6, picture_7=picture_7, picture_8=picture_8, region = region, town=town,
                           accepts_cats=accepts_cats, house_with_male_dog=house_with_male_dog,
                           house_with_female_dog=house_with_female_dog, transport=transport, adoption_abroad=adoption_abroad,
                           description=description, contact_data=contact_data, user=user)
        return HttpResponseRedirect('/radysiaki/')


class EditDog(View, LoginRequiredMixin):

    def get(self, request, id):
        dog = get_object_or_404(Dog, pk=id)
        form = AddDogForm(instance=dog)
        if request.user == dog.user or request.user.is_superuser:
            return render(request, "add_dog.html", {"form": form})
        else:
            return HttpResponse("Nie możesz edytować tego ogłoszenia")

    def post(self, request, id):
        form = AddDogForm(request.POST, request.FILES)
        dog = get_object_or_404(Dog, pk=id)
        dog.name = request.POST.get("name")
        dog.sex = request.POST.get("sex")
        dog.age = request.POST.get("age")
        dog.weight = request.POST.get("weight")
        if request.FILES.get("picture_1") != None:
            dog.picture_1 = request.FILES.get("picture_1")
        if request.FILES.get("picture_2") != None:
            dog.picture_2 = request.FILES.get("picture_2")
        if request.FILES.get("picture_3") != None:
            dog.picture_3 = request.FILES.get("picture_3")
        if request.FILES.get("picture_4") != None:
            dog.picture_4 = request.FILES.get("picture_4")
        if request.FILES.get("picture_5") != None:
            dog.picture_5 = request.FILES.get("picture_5")
        if request.FILES.get("picture_6") != None:
            dog.picture_6 = request.FILES.get("picture_6")
        if request.FILES.get("picture_7") != None:
            dog.picture_7 = request.FILES.get("picture_7")
        if request.FILES.get("picture_8") != None:
            dog.picture_8 = request.FILES.get("picture_8")
        dog.region = request.POST.get("region")
        dog.town = request.POST.get("town")
        dog.accepts_cats = request.POST.get("accepts_cats")
        dog.house_with_male_dog = request.POST.get("house_with_male_dog")
        dog.house_with_female_dog = request.POST.get("house_with_female_dog")
        dog.transport = request.POST.get("transport")
        dog.adoption_abroad = request.POST.get("adoption_abroad")
        dog.description = request.POST.get("description")
        dog.contact_data = request.POST.get("contact_data")
        dog.save()
        return HttpResponseRedirect('/pies/{}'.format(dog.id))


class DeleteDog(View, LoginRequiredMixin):

    def get(self, request, id):
        dog = get_object_or_404(Dog, pk=id)
        if request.user == dog.user or request.user.is_superuser:
            dog.delete()
            return HttpResponseRedirect('/radysiaki/')
        else:
            return HttpResponse("Nie możesz usunąć tego ogłoszenia")


class AddCategory(View, LoginRequiredMixin):

    def get(self, request, id):
        form = AddCategoriesForm()
        dog = get_object_or_404(Dog, pk=id)
        if request.user == dog.user or request.user.is_superuser:
            return render(request, "categories_form.html", {"form": form, "dog": dog})
        else:
            return HttpResponse("Nie możesz edytować tego ogłoszenia")

    def post(self, request, id):
        dog = Dog.objects.get(pk=id)
        category = Category.objects.get(id=request.POST.get('category'))
        DogCategories.objects.create(dog=dog, category=category)
        return HttpResponseRedirect('/kategorie_dodaj/{}'.format(id))


class Categories(View, LoginRequiredMixin):

    def get(self, request, id):
        dog = get_object_or_404(Dog, pk=id)
        return render(request, "remove_categories_form.html", {"dog": dog})


class RemoveCategory(View, LoginRequiredMixin):

    def get(self, request, d_id, c_id):
        dog = get_object_or_404(Dog, pk=d_id)
        category = get_object_or_404(Category, pk=c_id)
        cat_set = DogCategories.objects.filter(dog=dog, category=category)
        if request.user == dog.user or request.user.is_superuser:
            for cat in cat_set:
                cat.delete()
                return HttpResponseRedirect('/pies/{}'.format(d_id))
        else:
            return HttpResponse("Nie możesz edytować tego ogłoszenia")


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


class MessagesList(View, LoginRequiredMixin):

    def get(self, request, id):
        dog = get_object_or_404(Dog, pk=id)
        messages = Message.objects.filter(dog=dog)
        if request.user == dog.user or request.user.is_superuser:
            return render(request, "messages_list.html", {"messages": messages, "dog": dog})
        else:
            return HttpResponse("Nie możesz zobaczyć wiadomości do tego ogłoszenia")


class AdoptionFormView(View):

    def get(self, request, id):
        form = AdoptDogForm()
        dog = get_object_or_404(Dog, pk=id)
        return render(request, "message.html", {"form": form})

    def post(self, request, id):
        form = AddDogForm(request.POST)
        dog = get_object_or_404(Dog, pk=id)
        dog_owner = request.POST.get('dog_owner')
        family_agree = request.POST.get('family_agree')
        place_type = request.POST.get('place_type')
        house_owner = request.POST.get('house_owner')
        floor = request.POST.get('floor')
        fence = request.POST.get('fence')
        dogs_place = request.POST.get('dogs_place')
        time_alone = request.POST.get('time_alone')
        walks = request.POST.get('walks')
        beh_problems = request.POST.get('beh_problems')
        children = request.POST.get('children')
        pets_owned = request.POST.get('pets_owned')
        prev_dogs = request.POST.get('prev_dogs')
        location = request.POST.get('location')
        e_mail = request.POST.get('e_mail')
        phone = request.POST.get('phone')

        AdoptionForm.objects.create(dog=dog, dog_owner=dog_owner, family_agree=family_agree, place_type=place_type,
                                    house_owner=house_owner, floor=floor, fence=fence, dogs_place=dogs_place,
                                    time_alone=time_alone, walks=walks, beh_problems=beh_problems,  children=children,
                                    pets_owned=pets_owned, prev_dogs=prev_dogs, location=location, e_mail=e_mail, phone=phone)
        return HttpResponseRedirect('/radysiaki/')


class AdoptionFormList(View, LoginRequiredMixin):

    def get(self, request, id):
        dog = get_object_or_404(Dog, pk=id)
        adoption_forms = AdoptionForm.objects.filter(dog=dog)
        if request.user == dog.user or request.user.is_superuser:
            return render(request, "adoption_form_list.html", {"adoption_forms": adoption_forms, "dog": dog})
        else:
            return HttpResponse("Nie możesz zobaczyć ankiet do tego ogłoszenia")


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
                    dogs.append(dog)
        return render(request, "search_result.html", {"dogs": dogs})


class SortView(View):

    def get(self, request):
        form = SortForm()
        return render(request, "sort_form.html", {"form": form})

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
        return render(request, "dogs.html", {"dogs": dogs})


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
            return HttpResponseRedirect('/radysiaki/')
        else:
            return HttpResponseRedirect('/zaloguj/')


class Logout(View):

    def get(self, request):
        return render(request, 'logout.html')

    def post(self, request):
        logout(request)
        return HttpResponseRedirect('/radysiaki/')


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


