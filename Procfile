web: gunicorn proj.wsgi
worker: celery -A WeatherTelegramBot worker -l INFO --pool=solo