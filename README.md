Projekt "Serwis adopcyjny" korzysta z frameworku Django oraz systemu zarządzania bazami danych PostgreSQL.
Projekt zawiera aplikację "adopcje", która umożliwia stworzenie bazy ogłoszeń adopcyjnych. Jest dedykowany psom pochodzącym z konkretnego schroniska (Radysy) i czekającym na adopcję w hotelikach w całej Polsce. 
Projekt posiada 3 rodzaje użytkowników:
1. administrator (superuser) - może dodawać i usuwać pozostałych użytkowników, edytować i usuwać dowolne ogłoszenia oraz usuwać wiadomości i ankiety adopcyjne:
2. użytkownicy posiadający konto w serwisie - po zalogowaniu mogą dodawać ogłoszenia, edytować i usuwać dodane przez siebie ogłoszenia (ale nie ogłoszenia dodane przez innych użytkowników), przeglądać i usuwać wiadomości i ankiety adopcyjne dotyczące dodanych przez siebie ogłoszeń;
3. użytkownicy nieposiadający konta lub niezalogowani - mogą przeglądać i wyszukiwać ogłoszenia, sortować listę ogłoszeń, wysyłać wiadomości dotyczące ogłoszenia, wypełniać ankiety adopcyjne oraz zakładać konta w serwisie (przechodząc do 2 kategorii użytkowników).

Przed uruchomieniem projektu w systemie PostgreSQL należy utworzyć bazę danych "adopcje_db", a następnie:
1. zainstalować wymagane pakiety: pip3 install -r requirements.txt
2. przeprowadzić migracje: python3 manage.py migrate
3. utworzyć administratora: python3 manage.py createsuperuser
4. uruchomić serwer: python3 manage.py runserver
