from aiogram import Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.utils import executor
from keys import tokens
from img import cats
import random, requests, datetime
from keys.tokens import token_weather_api
from weather_correct import get_weather
from valutes import currency_rates


is_weather = False
token = tokens.token_bot
bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

@dp.message_handler(commands=['start'])
async def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🖇 Меню")
    btn2 = types.KeyboardButton("Погода")
    btn3 = types.KeyboardButton("Курсы валют")
    btn4 = types.KeyboardButton("Воронеж")
    btn5 = types.KeyboardButton("Милое животное")
    btn6 = types.KeyboardButton("Москва")

    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    await bot.send_message(message.chat.id, text="Привет, Я бот, чем помочь?", reply_markup=markup)




class Form(StatesGroup):
    city = State()
    rates = State()

@dp.message_handler()
async def get_weth(message: types.Message):
    if message.text == "Погода":
        await bot.send_message(message.from_user.id, 'В каком городе нужно посмотреть погоду?')
        await Form.city.set()
    elif message.text == "Милое животное":
        await bot.send_photo(message.from_user.id, photo=open(random.choice(cats), 'rb'))
    elif message.text == "Курсы валют":
        await bot.send_message(message.from_user.id, currency_rates('usd'))
        await bot.send_message(message.from_user.id, currency_rates('eur'))
        await bot.send_message(message.from_user.id, currency_rates('cny'))



@dp.message_handler(state=Form.city)
async def get_weathe(message: types.Message, state: FSMContext):
    async with state.proxy() as a:
        a['city'] = message.text
    await bot.send_message(message.from_user.id, get_weather(message.text, token_weather_api))
    await state.finish()



if __name__ == '__main__':
    executor.start_polling(dp)
    get_weather()
