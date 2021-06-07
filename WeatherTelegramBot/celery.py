import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WeatherTelegramBot.settings')
celery_app = Celery('WeatherTelegramBot')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()


celery_app.conf.beat_schedule = {
    'creating-new-objects': {
        'task': 'tasks.tasks.create_new_object',
        'schedule': 60.0
    }
}

if __name__ == '__main__':
    celery_app.start()
