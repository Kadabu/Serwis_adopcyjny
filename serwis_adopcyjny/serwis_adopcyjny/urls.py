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
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from adopcje.views import *
from adopcje.models import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('dodaj_konto/', AddUser.as_view(), name='add-user'),
    path('zaloguj/', Login.as_view(), name='login'),
    path('wyloguj/', Logout.as_view(), name='logout'),
    url('^', include('django.contrib.auth.urls')),
    path('', MainView.as_view(), name='main-page'),
    path('o_nas/', ReadMoreView.as_view(), name='main-page'),
    path('pies/<int:id>/', DogView.as_view(), name='dog'),
    path('dodaj/', AddDog.as_view()),
    path('edytuj/<int:id>/', EditDog.as_view()),
    path('usun/<int:id>/', DeleteDog.as_view()),
    path('zdjecie/<int:id>/', AddPicture.as_view()),
    path('usun_zdjecie/<int:id>/', DeletePicture.as_view()),
    path('zdjecie_profilowe/<int:id>/', SetProfilePicture.as_view()),
    path('wiadomosci/<int:id>/', MessagesList.as_view()),
    path('usun_wiadomosc/<int:id>/', DeleteMessage.as_view()),
    path('wiadomosc/<int:id>/', AddMessage.as_view()),
    path('ankieta/<int:id>/', AddAdoptionForm.as_view()),
    path('ankiety/<int:id>/', AdoptionFormsList.as_view()),
    path('usun_ankiete/<int:id>', DeleteAdoptionForm.as_view()),
    path('wyszukaj/', SearchView.as_view()),
    path('moje_psy/', MyDogsView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


