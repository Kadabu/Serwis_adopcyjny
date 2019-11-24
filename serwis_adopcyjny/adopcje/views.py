from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import AdoptionForm, Dog, Message, Picture, CATEGORIES
from .forms import AddDogForm, AdoptDogForm, AddUserForm, LoginForm, MessageForm, PictureForm, SearchForm, SortForm



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
            return render(request, "user_form.html", {"form": form, "message":
            message})
        elif password_1 != password_2:
            message += "Wpisane hasła są niezgodne"
            return render(request, "user_form.html", {"form": form, "message":
            message})
        else:
            User.objects.create_user(username=username, password=password_1,
            email=email)
            return HttpResponseRedirect('/zaloguj/')


class AddUserBlocked(TemplateView):

    template_name = 'info.html'

    def get_context_data(self):
        message = "Strona w budowie - założenie konta nie jest obecnie możliwe"
        return {'message': message}


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


class MainView(View):

    def get(self, request):
        form = SortForm()
        dogs = Dog.objects.all().order_by('date_added').reverse()
        pictures = Picture.objects.filter(profile=True)
        return render(request, "dogs.html", {"dogs": dogs, "pictures": pictures,
         "form": form})

    def post(self, request):
        form = SortForm(request.POST)
        sort_by = request.POST.get('sort_by')
        dogs = Dog.objects.all()
        pictures = Picture.objects.filter(profile=True)
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
        return render(request, "dogs.html", {"dogs": dogs,  "pictures": pictures,
         "form": form})


class ReadMoreView(TemplateView):

    template_name = 'info.html'

    def get_context_data(self):
        message = "Opis w budowie"
        return {'message': message}


class PrivacyView(TemplateView):

    template_name = 'privacy.html'


class DogView(View):

    def get(self, request, id):

        dog = get_object_or_404(Dog, pk=id)
        pictures = Picture.objects.filter(dog=dog)
        ctx = {"dog": dog, "pictures": pictures}
        return render(request, "dog.html", ctx)


class AddDog(View):

    def get(self, request):
        form = AddDogForm()
        return render(request, "add_dog.html", {"form": form})

    def post(self, request):
        form = AddDogForm(request.POST)
        if form.is_valid():
            dog = Dog.objects.create(
                name=form.cleaned_data['name'],
                sex=form.cleaned_data['sex'],
                age=form.cleaned_data['age'],
                weight=form.cleaned_data['weight'],
                region=form.cleaned_data['region'],
                town=form.cleaned_data['town'],
                accepts_cats=form.cleaned_data['accepts_cats'],
                house_with_male_dog=form.cleaned_data['house_with_male_dog'],
                house_with_female_dog=form.cleaned_data['house_with_female_dog'],
                transport=form.cleaned_data['transport'],
                adoption_abroad=form.cleaned_data['adoption_abroad'],
                description=form.cleaned_data['description'],
                categories=form.cleaned_data['categories'],
                contact_data=form.cleaned_data['contact_data'],
                user=request.user
                )
            return HttpResponseRedirect('/zdjecie/{}'.format(dog.pk))
        else:
            return HttpResponseRedirect('/dodaj/')


class EditDog(View):

    def get(self, request, id):
        dog = get_object_or_404(Dog, pk=id)
        form = AddDogForm(instance=dog)
        if request.user == dog.user or request.user.is_superuser:
            return render(request, "edit_dog.html", {"form": form, "dog": dog})
        else:
            return render(request, "info.html", {"message": "Nie możesz edytować\
             tego ogłoszenia"})

    def post(self, request, id):
        dog = get_object_or_404(Dog, pk=id)
        form = AddDogForm(data=request.POST, instance=dog)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/pies/{}'.format(id))
        else:
            return HttpResponseRedirect('/edytuj/{}'.format(dog.pk))


class DeleteDog(View):

    def get(self, request, id):
        dog = get_object_or_404(Dog, pk=id)
        if request.user == dog.user or request.user.is_superuser:
            dog.delete()
            return HttpResponseRedirect('/')
        else:
            return render(request, "info.html", {"message": "Nie możesz usunąć \
            tego ogłoszenia"})


class AddPicture(View):

    def get(self, request, id):
        form = PictureForm()
        dog = get_object_or_404(Dog, pk=id)
        if request.user == dog.user or request.user.is_superuser:
            return render(request, "picture.html", {"form": form, "dog": dog})
        else:
            return render(request, "info.html", {"message": "Nie możesz dodawać \
            zdjęć do tego ogłoszenia"})

    def post(self, request, id):
        form = PictureForm(request.POST, request.FILES)
        dog = Dog.objects.get(pk=id)
        pictures = Picture.objects.filter(dog=dog)
        if form.is_valid():
            picture = form.cleaned_data['picture']
            if pictures.count() == 8:
                return render(request, "info.html", {"message": "Możesz dodać maksymalnie 8 zdjęć"})
            else:
                if not pictures:
                    Picture.objects.create(dog=dog, picture=picture, profile=True)
                else:
                    Picture.objects.create(dog=dog, picture=picture)
                return HttpResponseRedirect('/zdjecie/{}'.format(id))


class DeletePicture(View):

    def get(self, request, id):
        picture = get_object_or_404(Picture, pk=id)
        dog = picture.dog
        if request.user == dog.user or request.user.is_superuser:
            if picture.profile == False:
                picture.delete()
                return HttpResponseRedirect('/pies/{}/'.format(dog.pk))
            else:
                return render(request, "info.html", {"message": "Nie możesz \
                usunąć zdjęcia profilowego. Ustaw najpierw nowe zdjęcie profilowe"})
        else:
            return render(request, "info.html", {"message": "Nie możesz usuwać \
            zdjęć w tym ogłoszeniu"})


class SetProfilePicture(View):

    def get(self, request, id):
        profile_picture = get_object_or_404(Picture, pk=id)
        dog = profile_picture.dog
        if request.user == dog.user or request.user.is_superuser:
            Picture.objects.filter(dog=dog).update(profile=False)
            Picture.objects.filter(pk=id).update(profile=True)
            return HttpResponseRedirect('/pies/{}/'.format(dog.pk))
        else:
            return render(request, "info.html", {"message": "Nie możesz ustawiać\
             zdjęcia profilowego w tym ogłoszeniu"})


class AddMessage(View):

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
            return render(request, "messages_list.html", {"messages": messages,
            "dog": dog})
        else:
            return render(request, "info.html", {"message": "Nie możesz \
            przeglądać wiadomości do tego ogłoszenia"})


class DeleteMessage(View):

    def get(self, request, id):
        message = get_object_or_404(Message, pk=id)
        dog = message.dog
        if request.user == dog.user or request.user.is_superuser:
            message.delete()
            return HttpResponseRedirect('/wiadomosci/{}/'.format(dog.id))
        else:
            return render(request, "info.html", {"message": "Nie możesz usunąć \
            tej wiadomości"})


class DeleteAdoptionForm(View):

    def get(self, request, id):
        adoption_form = get_object_or_404(AdoptionForm, pk=id)
        dog = adoption_form.dog
        if request.user == dog.user or request.user.is_superuser:
            adoption_form.delete()
            return HttpResponseRedirect('/ankiety/{}/'.format(dog.id))
        else:
            return render(request, "info.html", {"message": "Nie możesz usunąć \
            tej ankiety"})


class AddAdoptionForm(View):

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


class AdoptionFormsList(View):

    def get(self, request, id):
        dog = get_object_or_404(Dog, pk=id)
        adoption_forms = AdoptionForm.objects.filter(dog=dog)
        if request.user == dog.user or request.user.is_superuser:
            return render(request, "adoption_form_list.html", {"adoption_forms":
             adoption_forms, "dog": dog})
        else:
            return render(request, "info.html", {"message": "Nie możesz \
            przeglądać ankiet do tego ogłoszenia"})


class SearchView(View):

    def get(self, request):
        form = SearchForm()
        return render(request, "search_form.html", {"form": form})

    def post(self, request):
        form = SearchForm(request.POST)

        if form.is_valid():
            region = form.cleaned_data['region']
            sex = form.cleaned_data['sex']
            categories = form.cleaned_data['categories']
            print("Form.categories {}".format(form.cleaned_data['categories']))
            dogs = []
            dogs_by_reg = []
            dogs_by_sex = []
            dogs_by_categories = []

            for reg in region:
                dogs_by_reg += Dog.objects.filter(region=int(reg))
            for s in sex:
                dogs_by_sex += Dog.objects.filter(sex=int(s))

            for dog in dogs_by_reg:
                if dog in dogs_by_sex and dog not in dogs :
                    dogs.append(dog)

            for cat in categories:
                for dog in dogs:
                    if CATEGORIES[int(cat)-1][1] in str(dog.categories) and dog not in dogs_by_categories:
                        dogs_by_categories.append(dog)
            print(dogs_by_categories)

            pictures = Picture.objects.filter(profile=True)
            return render(request, "search_result.html", {"dogs": dogs_by_categories,
                "pictures": pictures})

        else:
            return HttpResponseRedirect('/wyszukaj/')


class MyDogsView(View):

    def get(self, request):
        user = request.user
        if user.is_authenticated:
            if user.is_superuser:
                dogs = Dog.objects.all()
            else:
                dogs = Dog.objects.filter(user=user)
            return render(request, "my_dogs.html", {"dogs": dogs})
        else:
            return render(request, "info.html", {"message": "Strona dostępna \
            tylko dla zalogowanych użytkowsników"})








