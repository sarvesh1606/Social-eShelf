# Social-eShelf

Social eShelf for the books where users can purchase the book , review it on that book's post and also interact with other users by sharing books online. CRUD functionalities , search, serialized Rest APIs are other features.

## - A Django application

Please be sure you have installed pip and Django in your system.

Please follow following steps

1. First step is to create migration files using the following command:
```buildoutcfg
python manage.py makemigrations
```

2. Then migrate using the following command:
```buildoutcfg
python manage.py migrate
```

3. Create super user using the command:
```
python manage.py createsuperuser
```
enter your username, email and password

4. run server using the command:
```
python manage.py runserver
```
5. visit admin panel at `127.0.0.1:8000/admin` 
