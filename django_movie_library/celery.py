import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_movie_library.settings')

app = Celery('django_movie_library')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-spam-every-3-minute': {
        'task': 'contact.tasks.send_beat_email',
        'schedule': crontab(minute='*/3'),
    },
}
