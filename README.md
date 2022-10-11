# https://pypi.org/project/django-json-widget/

### Setup virtual env
pipenv shell
pipenv install django psycopg2-binary django-json-widget
django admin-startproject postgresql_project

### build project in the container
docker-compose up -d --build
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py startapp JSONapp

### Regsiter this app in the settings.py

### You might need to change JSONapp owner to be able to have write access
sudo chown -R YourUserName JSONapp

### Now we can migrate model and run our project:

docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate

# Add some data
http://127.0.0.1/newdog
http://127.0.0.1/dogDetail/1

### To stop all containers
docker-compose stop

### or to stop and remove containers
docker-compose down

