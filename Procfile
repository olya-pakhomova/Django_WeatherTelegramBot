web :  gunicorn WeatherTelegramBot.wsgi --log-file - 
worker :  celery -A WeatherTelegramBot:celery_app worker -l info
beat :  python manage.py celery beat --loglevel = info