web: gunicorn WeatherTelegramBot:app--log-file -
worker: celery -A WeatherTelegramBot:app worker -l info