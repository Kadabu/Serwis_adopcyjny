"""serwis_adopcyjny URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from adopcje.views import AddDog, AddPicture, AddUser, DeleteDog, DeletePicture, \
    EditDog, DeleteUser, DeleteUserConfirmation, DogView, EmailChange, Login, \
    Logout, MainView, NewDogsView, PasswordChange, UserAccountView, PrivacyView, \
    ReadMoreView, SearchView, SetProfilePicture, TermsOfUseView, UserDogsView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('dodaj_konto/', AddUser.as_view(), name='add-user'),
    path('zaloguj/', Login.as_view(), name='login'),
    path('wyloguj/', Logout.as_view(), name='logout'),
    path('konto/', UserAccountView.as_view()),
    path('usun_konto_potwierdz/', DeleteUserConfirmation.as_view()),
    path('usun_konto/', DeleteUser.as_view()),
    path('haslo/', PasswordChange.as_view()),
    path('email/', EmailChange.as_view()),
    path('moje_psy/', UserDogsView.as_view()),
    path('nowe/', NewDogsView.as_view()),
    path('', MainView.as_view(), name='main-page'),
    path('o_nas/', ReadMoreView.as_view(), name='main-page'),
    path('polityka_prywatnosci/', PrivacyView.as_view()),
    path('regulamin/', TermsOfUseView.as_view()),
    path('pies/<int:id>/', DogView.as_view(), name='dog'),
    path('dodaj/', AddDog.as_view()),
    path('edytuj/<int:id>/', EditDog.as_view()),
    path('usun/<int:id>/', DeleteDog.as_view()),
    path('zdjecie/<int:id>/', AddPicture.as_view()),
    path('usun_zdjecie/<int:id>/', DeletePicture.as_view()),
    path('zdjecie_profilowe/<int:id>/', SetProfilePicture.as_view()),
    path('wyszukaj/', SearchView.as_view()),
    url('^', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
