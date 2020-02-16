from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Dog, Picture, CATEGORIES
from .forms import AcceptDogForm, AddDogForm, AddUserForm, LoginForm, EditUserForm, PictureForm, SearchForm, SortForm


class AddUser(View):

    def get(self, request):
        """Render AddUserForm."""
        form = AddUserForm()
        return render(request, "user_form.html", {"form": form})

    def post(self, request):
        """Create a new User object.

        Check the data in the form and if valid, create a new User object and \
        redirect to login page.
        Otherwise, return the error message.
        """
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
        elif len(username) > 150:
            message += "Nazwa użytkownika może zawierać do 150 znaków"
            return render(request, "user_form.html", {"form": form, "message":
            message})
        elif password_1 != password_2:
            message += "Wpisane hasła są niezgodne"
            return render(request, "user_form.html", {"form": form, "message":
            message})
        elif password_1.isdecimal() or len(password_1) < 8 or len(password_1) > 128:
            message += "Hasło musi zawierać 8-128 znaków, w tym co najmniej jedna literę"
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


class UserAccountView(View):

    def get(self, request):
        """Render the user`s account management page.

        If user is authenticated, render the user`s account management page.
        Otherwise, return the error message.
        """
        user = request.user
        if user.is_authenticated:
            return render(request, "user_account.html", {"user": user})
        else:
            return render(request, "info.html", {"message": "Strona dostępna \
            tylko dla zalogowanych użytkowników"})


class PasswordChange(View):

    def get(self, request):
        """Render the password change form.

        If user is authenticated, render the password change form (EditUserForm).
        Otherwise, return the error message.
        """
        user = request.user
        if user.is_authenticated:
            form = EditUserForm()
            return render(request, "user_password.html", {"form": form, "user": user})
        else:
            return render(request, "info.html", {"message": "Strona dostępna \
            tylko dla zalogowanych użytkowników"})

    def post(self, request):
        """Change user`s password.

        Check the data in the form and if valid, change user`s password and \
        redirect to user`s account management page.
        Otherwise, return the error message.
        """
        user = request.user
        form = EditUserForm(request.POST)
        password_1 = request.POST.get('password_1')
        password_2 = request.POST.get('password_2')
        message = ''
        if password_1 != password_2:
            message += "Wpisane hasła są niezgodne"
            return render(request, "user_password.html", {"form": form, \
            "user": user, "message": message})
        elif password_1.isdecimal() or len(password_1) < 8 or len(password_1) > 128:
            message += "Hasło musi zawierać 8-128 znaków, w tym co najmniej jedna literę"
            return render(request, "user_password.html", \
            {"form": form, "user": user, "message": message})
        else:
            user.set_password(password_1)
            user.save()
            login(request, user)
            return HttpResponseRedirect('/konto/')


class EmailChange(View):

    def get(self, request):
        """Render the e-mail change form.

        If user is authenticated, render the e-mail change form (EditUserForm).
        Otherwise, return the error message.
        """
        user = request.user
        if user.is_authenticated:
            form = EditUserForm()
            return render(request, "user_email.html", {"form": form, "user": user})
        else:
            return render(request, "info.html", {"message": "Strona dostępna \
            tylko dla zalogowanych użytkowników"})

    def post(self, request):
        """Change user`s e-mail and redirect to user`s account management page."""
        user = request.user
        user.email = request.POST.get('email')
        user.save()
        login(request, user)
        return HttpResponseRedirect('/konto/')


class Login(View):

    def get(self, request):
        """Render the LoginForm."""
        form = LoginForm()
        return render(request, "login.html", {"form": form})

    def post(self, request):
        """Authenticate and login user.

        Authenticate the user with the username and password.
        If user is authenticated, login user and redirect to the main page.
        Otherwise, render the login form.
        """
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
        """Logout the request user and redirect to the main page."""
        logout(request)
        return HttpResponseRedirect('/')


class DeleteUserConfirmation(View):

    def get(self, request):
        """Render the page with user deletion link.

        Check if user is authenticated. If so, render the page with user deletion link.
        Otherwise, return the error message.
        """
        user = request.user
        if user.is_authenticated:
            return render(request, "delete_user.html", {"user": user})
        else:
            return render(request, "info.html", {"message": "Strona dostępna \
            tylko dla zalogowanych użytkowników"})


class DeleteUser(View):

    def get(self, request):
        """Delete user.

        Check if user is authenticated. If so, delete user.
        Otherwise, redirect to the main page.
        """
        user = request.user
        if user.is_authenticated:
            user.delete()
        return HttpResponseRedirect('/')


class MainView(View):

    def get(self, request):
        """Render the SortForm and the profile pictures of dogs from the queryset."""
        form = SortForm()
        dogs = Dog.objects.filter(accepted=1).order_by('date_added').reverse()
        pictures = Picture.objects.filter(profile=True)
        return render(request, "dogs.html", {"dogs": dogs, "pictures": pictures,
         "form": form})

    def post(self, request):
        """Render the SortForm and the profile pictures of dogs from the queryset \
         sorted by date or age or randomly.
        """
        form = SortForm(request.POST)
        sort_by = request.POST.get('sort_by')
        dogs = Dog.objects.filter(accepted=1)
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
            dogs = dogs.order_by('?')
        return render(request, "dogs.html", {"dogs": dogs,  "pictures": pictures,
         "form": form})


class ReadMoreView(TemplateView):

    template_name = 'read_more.html'


class PrivacyView(TemplateView):

    template_name = 'privacy.html'


class TermsOfUseView(TemplateView):

    template_name = 'terms_of_use.html'


class DogView(View):

    def get(self, request, id):
        dog = get_object_or_404(Dog, pk=id)
        pictures = Picture.objects.filter(dog=dog)
        profile_picture = pictures.get(profile=True)
        form = AcceptDogForm(instance=dog)
        return render(request, "dog.html", {"dog": dog, "pictures": pictures, "profile_picture": profile_picture, "form": form})

    def post(self, request, id):
        dog = get_object_or_404(Dog, pk=id)
        dog.accepted = request.POST.get('accepted')
        dog.save()
        return HttpResponseRedirect('/nowe/')


class AddDog(View):

    def get(self, request):
        """Render AddDogForm in order to create a Dog object."""
        form = AddDogForm()
        return render(request, "add_dog.html", {"form": form})

    def post(self, request):
        """Create a Dog object.

        Check the data in the form and if valid, create a Dog object and \
        redirect to the page with PictureForm.
        Otherwise, redirect to the same page.
        """
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
        """Render AddDogForm in order to update a Dog object.

        If the Dog object is related to the request user with the foreign key \
        or the request user is superuser, render AddDogForm.
        Otherwise, return the error message.
        """
        dog = get_object_or_404(Dog, pk=id)
        form = AddDogForm(instance=dog)
        if request.user == dog.user or request.user.is_superuser:
            return render(request, "edit_dog.html", {"form": form, "dog": dog})
        else:
            return render(request, "info.html", {"message": "Nie możesz edytować \
             tego ogłoszenia"})

    def post(self, request, id):
        """Update a Dog object.

        Check the data in the form and if valid, update the Dog object and \
        redirect to the page with the adoption advertisment.
        Otherwise, redirect to the same page.
        """
        dog = get_object_or_404(Dog, pk=id)
        form = AddDogForm(data=request.POST, instance=dog)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/pies/{}'.format(id))
        else:
            return HttpResponseRedirect('/edytuj/{}'.format(dog.pk))


class DeleteDog(View):

    def get(self, request, id):
        """Delete a Dog object.

        If the Dog object is related to the request user with the foreign key \
        or the request user is superuser, delete the Dog object.
        Otherwise, return the error messsage.
        """
        dog = get_object_or_404(Dog, pk=id)
        if request.user == dog.user or request.user.is_superuser:
            dog.delete()
            return HttpResponseRedirect('/')
        else:
            return render(request, "info.html", {"message": "Nie możesz usunąć \
            tego ogłoszenia"})


class AddPicture(View):

    def get(self, request, id):
        """Render PictureForm in order to create a Picture object.

        If the  Dog object is related to the request user with the foreign key \
        or the user is superuser, render PictureForm.
        Otherwise, return the error messsage.
        """
        form = PictureForm()
        dog = get_object_or_404(Dog, pk=id)
        if request.user == dog.user or request.user.is_superuser:
            return render(request, "picture.html", {"form": form, "dog": dog})
        else:
            return render(request, "info.html", {"message": "Nie możesz dodawać \
            zdjęć do tego ogłoszenia"})

    def post(self, request, id):
        """Create a Dog object.

        Check the data in the form and if valid, create a Dog object and \
        redirect to the page with PictureForm.
        Otherwise, redirect to the same page.
        """
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
        """Delete a Picture object.

        If the Picture object is related to the Dog object with the foreign key \
        and the Dog object is related to the request user with the foreign key \
        or the user is superuser and the Picture object is not the profile picture, \
        delete the Picture object.
        Otherwise, return the error messsage.
        """
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
        """Set the profile picture.

        Get the Picture object (profile_picture) by the id.
        If the Dog object, to which the profile_picture is related to with \
        the foreign key, is related the request user with the foreign key or \
        the request user is superuser, set the profile field of the Picture \
        objects related to the Dog object with the foreign key as False.
        Then set the profile field of the profile_picture as True.
        Otherwise, return the error messsage.
        """
        profile_picture = get_object_or_404(Picture, pk=id)
        dog = profile_picture.dog
        if request.user == dog.user or request.user.is_superuser:
            Picture.objects.filter(dog=dog).update(profile=False)
            Picture.objects.filter(pk=id).update(profile=True)
            return HttpResponseRedirect('/pies/{}/'.format(dog.pk))
        else:
            return render(request, "info.html", {"message": "Nie możesz ustawiać \
            zdjęcia profilowego w tym ogłoszeniu"})


class SearchView(View):

    def get(self, request):
        """Render SearchForm."""
        form = SearchForm()
        return render(request, "search_form.html", {"form": form})

    def post(self, request):
        """Filter the adoption advertisments.

        Check the data in the form and if valid, create the list of Dog objects \
        (dogs_by_categories) and the queryset of Picture objects (pictures).
        Otherwise, redirect to the same page.
        """
        form = SearchForm(request.POST)
        if form.is_valid():
            region = form.cleaned_data['region']
            sex = form.cleaned_data['sex']
            categories = form.cleaned_data['categories']
            dogs = []
            dogs_by_reg = []
            dogs_by_sex = []
            dogs_by_categories = []
            for reg in region:
                dogs_by_reg += Dog.objects.filter(region=int(reg))
            for s in sex:
                dogs_by_sex += Dog.objects.filter(sex=int(s))
            for dog in dogs_by_reg:
                if dog in dogs_by_sex and dog not in dogs:
                    dogs.append(dog)
            for cat in categories:
                for dog in dogs:
                    if CATEGORIES[int(cat)-1][1] in str(dog.categories) and dog not in dogs_by_categories:
                        dogs_by_categories.append(dog)
            pictures = Picture.objects.filter(profile=True)
            return render(request, "search_result.html", {"dogs": dogs_by_categories,
                "pictures": pictures})
        else:
            return HttpResponseRedirect('/wyszukaj/')


class UserDogsView(View):

    def get(self, request):
        """Render the page with links to user`s adoption advertisments.

        If the request user is authenticated, render the page with links to \
        adoption advertisments added by the user. If the user is superuser, \
        render the page with links to all adoption advertisments.
        Otherwise, return the error message.
        """
        user = request.user
        if user.is_authenticated:
            if user.is_superuser:
                dogs = Dog.objects.all()
            else:
                dogs = Dog.objects.filter(user=user)
            return render(request, "my_dogs.html", {"dogs": dogs})
        else:
            return render(request, "info.html", {"message": "Strona dostępna \
            tylko dla zalogowanych użytkowników"})


class NewDogsView(View):

    def get(self, request):
        """Render the page with links to new adoption advertisments.

        If the request user is superuser, render the page with links to new \
        adoption advertisments.
        Otherwise, return the error message.
        """
        user = request.user
        if user.is_authenticated and user.is_superuser:
            dogs = Dog.objects.filter(accepted=2)
            return render(request, "dogs_to_accept.html", {"dogs": dogs})
        else:
            return render(request, "info.html", {"message": "Strona dostępna \
            tylko dla administratora"})
