from pprint import pprint
import datetime
import requests
from keys.tokens import token_weather_api
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from keys import tokens
from img import cats
import random, requests, datetime
from keys.tokens import token_weather_api
from weather import get_weather

def get_weather(city, token_weather_api):

    code_to_smile = {
        'Clear': 'Ясно \U00002600',
        'Clouds': 'Облачно \U00002601',
        'Rain': 'Дождь \U00002614',
        'Drizzle': 'Дождь \U00002614',
        'Thunderstorm': 'Гроза \U000026A1',
        'Snow': 'Снег \U0001F328',
        'Mist': 'Туман \U0001F32B'
    }
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token_weather_api}&units=metric"
        )
        data = r.json()

        city = data['name']

        weather_description = data['weather'][0]['main']
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            pass

        cur_weather = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        lenght_of_the_day = datetime.datetime.fromtimestamp(data['sys']['sunset']) - datetime.datetime.fromtimestamp(data['sys']['sunrise'])


        return (f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}\n'
              f'Погода в городе {city}: {wd}\n\nТемпература: {cur_weather}C°\n'
              f'Ощущается как: {feels_like}C°\nВлажность: {humidity}%\n'
              f'Давление: {pressure} мм.рт.ст.\nВетер: {wind} м/с\n'
              f'Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\n'
              f'Продолжительность дня: {lenght_of_the_day}\n\n'
              f'Хорошего дня!')

    except Exception as ex:
        return ('Проверьте название города')

def main():
    city = input("Введите город: ")
    get_weather(city, token_weather_api)

if __name__ == '__main__':
    main()