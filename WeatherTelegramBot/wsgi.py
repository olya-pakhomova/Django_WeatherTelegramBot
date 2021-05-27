"""
WSGI config for WeatherTelegramBot project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bootcamp.settings")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "WeatherTelegramBot.settings")

application = get_wsgi_application()
