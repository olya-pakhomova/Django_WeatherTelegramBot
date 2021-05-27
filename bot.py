import os

import telebot
import requests
from django.core.management.base import BaseCommand
from telebot import types

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WeatherTelegramBot.settings')

from WeatherTelegramBot.settings import TOKEN
from datetime import datetime

from tgbot.models import User

bot = telebot.TeleBot(TOKEN)


class Command(BaseCommand):
    help = "Телеграм-бот"

    def handle(self, *args, **options):
        print(bot.get_me())

        bot.polling(none_stop=True, interval=0)


@bot.message_handler(commands=["geo"])
def geo(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
    keyboard.add(button_geo)
    bot.send_message(message.chat.id, "Привет! Нажми на кнопку и передай мне свое местоположение",
                     reply_markup=keyboard)


#


@bot.message_handler(content_types=["location"])
def location(message):
    if message.location:
        chat_id = message.chat.id
        User.objects.update_or_create(
            user_id=chat_id,
            defaults={
                'username': message.from_user.username,
                'full_name': message.from_user.full_name,
                'latitude': message.location.latitude,
                'longitude': message.location.longitude
            }
        )
        geo_params = {'lat': message.location.latitude, 'lon': message.location.longitude}
        get_weather(message, geo_params)


def get_weather(message, params):
    try:
        appid = 'ee98dc3d0fec06c23d078d41364b81f5'
        def_params = {'units': 'metric', 'lang': 'ru', 'APPID': appid}
        all_params = params.copy()
        all_params.update(def_params)
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                           params=all_params)
        data = res.json()
        s_city = data['name']
        temp = data['main']['temp']
        conditions = data['weather'][0]['description']
        date = get_date()
        weather = f'Сегодня {date}, погода в {s_city} составляет {temp}˚C, {conditions}.'
        bot.send_message(message.from_user.id, weather)
    except Exception as e:
        print("Exception (weather):", e)
        pass


def get_date():
    month_list = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
                  'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
    now = datetime.now().strftime("%d.%m.%Y").split('.')
    return now[0] + ' ' + month_list[int(now[1]) - 1] + ' ' + now[2] + ' года'
