import os
import random
import string
from time import sleep

import telebot
from celery import shared_task
from django.http import HttpResponse

from WeatherTelegramBot import celery_app


@celery_app.task()
def create_new_object():
    from tgbot.models import User
    random_id = random.randint(1, 10000)
    random_name = ''.join([random.choice(string.ascii_letters) for _ in range(10)])
    new_object = User.objects.create(user_id=random_id, username=random_name)
    return new_object.username
