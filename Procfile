web: gunicorn proj.wsgi
celery: celery -A WeatherTelegramBot worker -l INFO --pool=solo