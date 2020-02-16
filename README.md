Projekt "Serwis adopcyjny" korzysta z frameworku Django oraz systemu zarządzania bazami danych PostgreSQL.
Projekt zawiera aplikację "adopcje", która umożliwia tworzenie bazy ogłoszeń adopcyjnych. Jest dedykowany psom pochodzącym z konkretnego schroniska (Radysy) i czekającym na adopcję w hotelikach w całej Polsce.
Projekt posiada 3 rodzaje użytkowników o różnym zakresie uprawnień:
1. użytkownicy nieposiadający konta lub niezalogowani - mogą przeglądać i wyszukiwać ogłoszenia, sortować listę ogłoszeń oraz zakładać konta w serwisie;
2. użytkownicy posiadający konto w serwisie - mogą przeglądać i wyszukiwać ogłoszenia, sortować listę ogłoszeń, dodawać ogłoszenia oraz edytować i usuwać dodane przez siebie ogłoszenia, a także zarządzać swoim kontem w serwisie;
3. administrator (superuser) - może przeglądać i wyszukiwać ogłoszenia, sortować listę ogłoszeń, dodawać ogłoszenia oraz edytować i usuwać dowolne ogłoszenia, a także zarządzać kontami użytkowników serwisu.

Przed uruchomieniem projektu w systemie PostgreSQL należy utworzyć bazę danych "adopcje_db", a następnie:
1. zainstalować wymagane pakiety: pip3 install -r requirements.txt,
2. przeprowadzić migracje: python3 manage.py migrate,
3. utworzyć administratora: python3 manage.py createsuperuser,
4. uruchomić serwer: python3 manage.py runserver.
