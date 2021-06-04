import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WeatherTelegramBot.settings')
app = Celery('WeatherTelegramBot')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'creating-new-objects': {
        'task': 'tasks.tasks.create_new_object',
        'schedule': 60.0
    }
}
