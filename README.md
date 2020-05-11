The "Serwis adopcyjny" project is based on the Django framework and the PostgreSQL database management system.
The project contains the "adopcje" application, that allows users to create, update and view adoption ads. It is dedicated to dogs coming from a specific shelter (in Radysy) and waiting for adoption in dog hotels all over Poland.
The project has 3 types of users with different scope of privileges:
1. users without a user account or not logged in - they can view and search ads, sort the list of ads and create their user accounts;
2. users with user account - they can view and search ads, sort the list of ads, add ads and edit and delete ads they have added, as well as manage their user account;
3. administrator (superuser) - can view and search ads, sort the list of ads, add ads and edit and delete any ads, as well as manage all user accounts.

Before starting the project, create the "adopcje_db" database in the PostgreSQL, and then:
1. install the required packages: pip3 install -r requirements.txt,
2. migrate: python3 manage.py migrate,
3. create the administrator: python3 manage.py createsuperuser,
4. start the server: python3 manage.py runserver.

----------------------------------------------------------------------------------------------------------------------------------------------

Projekt "Serwis adopcyjny" korzysta z frameworku Django oraz systemu zarządzania bazami danych PostgreSQL.
Projekt zawiera aplikację "adopcje", która umożliwia tworzenie bazy ogłoszeń adopcyjnych. Jest dedykowany psom pochodzącym z konkretnego schroniska (w Radysach) i czekającym na adopcję w hotelikach w całej Polsce.
Projekt posiada 3 rodzaje użytkowników o różnym zakresie uprawnień:
1. użytkownicy nieposiadający konta lub niezalogowani - mogą przeglądać i wyszukiwać ogłoszenia, sortować listę ogłoszeń oraz zakładać konta w serwisie;
2. użytkownicy posiadający konto w serwisie - mogą przeglądać i wyszukiwać ogłoszenia, sortować listę ogłoszeń, dodawać ogłoszenia oraz edytować i usuwać dodane przez siebie ogłoszenia, a także zarządzać swoim kontem w serwisie;
3. administrator (superuser) - może przeglądać i wyszukiwać ogłoszenia, sortować listę ogłoszeń, dodawać ogłoszenia oraz edytować i usuwać dowolne ogłoszenia, a także zarządzać kontami użytkowników serwisu.

Przed uruchomieniem projektu w systemie PostgreSQL należy utworzyć bazę danych "adopcje_db", a następnie:
1. zainstalować wymagane pakiety: pip3 install -r requirements.txt,
2. przeprowadzić migracje: python3 manage.py migrate,
3. utworzyć administratora: python3 manage.py createsuperuser,
4. uruchomić serwer: python3 manage.py runserver.
