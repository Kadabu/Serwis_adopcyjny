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
from django.urls import path
from adopcje.views import *
from adopcje.models import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('radysiaki/', MainView.as_view(), name="main-page"),
    path('pies/<int:id>/', DogView.as_view(), name="dog"),
    path('dodaj/', AddDog.as_view()),
    path('kategorie_dodaj/<int:id>/', AddCategory.as_view()),
    path('kategorie/<int:id>/', Categories.as_view()),
    path('kategorie_usun/<int:d_id>/<int:c_id>/', RemoveCategory.as_view()),
    path('edytuj/<pk>/', EditDog.as_view()),
    path('usun/<int:id>/', DeleteDog.as_view()),
    path('wiadomości/<int:id>/', MessagesList.as_view()),
    path('pytanie/<int:id>/', MessageView.as_view()),
    path('ankieta/<int:id>', AdoptionFormView.as_view()),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
