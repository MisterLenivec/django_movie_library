# Movie library

### To start the newsletter

#### Run redis on docker:
```
docker run -d -p 6379:6379 redis
```

#### Run django server:
```
python manage.py runserver
```

#### Run the Celery worker server:
```
celery -A django_movie_library worker -l info
```

#### Run a flower if you want to see tasks in a browser:
```
flower -A django_movie_library --port=5555
```
#### View Flower http://127.0.0.1:5555/

#### If you want to send newsletter at regular intervals
#### Run the periodic task scheduler:
```
celery -A django_movie_library beat -l info
```
