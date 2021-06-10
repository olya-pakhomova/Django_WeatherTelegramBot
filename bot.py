import os
import time
import django
import schedule
import telebot

from main import get_weather

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WeatherTelegramBot.settings')

django.setup()

bot_token = os.environ['BOT_TOKEN']
bot = telebot.TeleBot(bot_token)


def get_every_day_weather():
    from tgbot.models import User
    users = User.get_user()
    for user in users:
        geo_params = {'lat': user.latitude, 'lon': user.longitude}
        get_weather(user.user_id, geo_params)


schedule.every(3).hours.do(get_every_day_weather)

while True:
    schedule.run_pending()
    time.sleep(3600 * int(os.environ['HOURS']))
