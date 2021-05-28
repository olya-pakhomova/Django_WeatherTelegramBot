import os
import django
import requests
import telebot

from telebot import types
from datetime import datetime


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WeatherTelegramBot.settings')

django.setup()

bot_token = os.environ['BOT_TOKEN']
bot = telebot.TeleBot(bot_token)


@bot.message_handler(commands=["start"])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_geo = types.KeyboardButton(text="Отправить местоположение по геолокации", request_location=True)
    keyboard.add(button_geo)
    bot.reply_to(message, "Привет! Я рассказываю о текущей погоде.\n"
                          "Если хочешь узнать погоду в своём городе отправь мне свою геопозицию, "
                          "либо напиши город вручную",
                 reply_markup=keyboard)


@bot.message_handler(content_types=["text"])
def get_city(message):
    geo_params = {'q': message.text}
    get_weather(message, geo_params)


@bot.message_handler(content_types=["location"])
def location(message):
    if message.location:
        chat_id = message.chat.id
        from tgbot.models import User
        User.create_by_chat_id(chat_id, message)
        geo_params = {'lat': message.location.latitude, 'lon': message.location.longitude}
        get_weather(message.from_user.id, geo_params)


def get_weather(user, params):
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
        bot.send_message(user, weather)
    except Exception as e:
        print("Exception (weather):", e)
        bot.send_message(user, "Извините, такой город не найден. Попробуйте еще раз!")
        pass


def get_date():
    month_list = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
                  'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
    now = datetime.now().strftime("%d.%m.%Y").split('.')
    return now[0] + ' ' + month_list[int(now[1]) - 1] + ' ' + now[2] + ' года'


if __name__ == '__main__':
    bot.polling(none_stop=True)
