import logging
import os
import pandas as pd 
import numpy as np

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

TOKEN = os.getenv('TOKEN_BOT')
bot = Bot(token = TOKEN)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)

@dp.message(Command(commands=['start']))
async def process_command_start(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Привет, {user_name}!\n Введите ФИО правильно, в одну строку с пробелами между фамилией, именем и отчеством'
    logging.info(f'{user_name} {user_id} запустил бота')
    await bot.send_message(chat_id=user_id, text=text)

@dp.message()
async def send_echo(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = message.text
    translit = pd.read_csv("/home/zemfira/Фаза 0/echodockerbot_aiogram3/Mybot/Транслитерация кириллических знаков (извлечение).csv")
    dict_file = dict(translit[["Национальный знак", "Рекомендуемая транслитерация"]].to_numpy())
    def latin_text(text):
        if len(list(text.split(" "))) != 3:
            return  "Введите ФИО правильно!"
        else:
            text_list = list(text.upper())
            new_text = []
            for i in range(0, len(text_list)):
                for key in dict_file.keys():
                    if text_list[i] == key:
                        new_text.append(dict_file.get(key))
                if text_list[i] == " ":
                    new_text.append(' ')
            return ''.join(new_text).lower().title()
    new_text = map(latin_text, text)
    logging.info(f'{user_name} {user_id}: {text}')
    await message.answer(text=new_text)

if __name__ == '__main__':
    dp.run_polling(bot)