web: gunicorn WeatherTelegramBot:app--log-file -
worker: celery -A WeatherTelegramBot:celery_app worker -l info