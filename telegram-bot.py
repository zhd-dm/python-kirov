import asyncio
from typing import List

import telebot
from telebot import types, TeleBot


from env import TBOT_SETTINGS, TELEGRAM_BOT_TOKEN
from google_sheets.google_sheet import GoogleSheet
from google_sheets.constants import RANGE_METHODS_NAMES
from utils import Settings, get_dict_by_indexes_of_matrix

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

print('Бот стартовал')

commands = ['start', 'get_commands']

@bot.message_handler(content_types = ['text'])
def check_connection(message):
    markup = types.InlineKeyboardMarkup()
    buttons = [
        types.InlineKeyboardButton(text = 'Проверить подключение к БД', callback_data = 'check_db'),
        types.InlineKeyboardButton(text = 'Получить список методов из Google Sheets', callback_data = 'get_methods_list')
    ]
    
    markup.add(*buttons)
    bot.send_message(message.chat.id, 'Выберите команду', reply_markup = markup)

@bot.callback_query_handler(func = lambda callback: callback.data == 'check_db')
def check_db_cb(callback):
    chat_id = callback.message.chat.id
    bot.send_message(chat_id, 'Проверка БД...')
    settings = Settings(TBOT_SETTINGS)

    try:
        connection = settings.connection
        methods_list = get_methods_list()
        print('methods_list')
        print(methods_list)
        bot.send_message(chat_id, 'Подключение к БД удалось')
        markup = types.InlineKeyboardMarkup()
        buttons = [types.InlineKeyboardButton(method_name, callback_data = method_name) for method_name in methods_list]
        markup.add(*buttons)
        print('end')

    except Exception as error:
        bot.send_message(chat_id, 'Произошла ошибка при подключении к БД')
    finally:
        settings._engine_dispose()


@bot.callback_query_handler(func = lambda callback: callback.data == 'get_methods_list')
async def get_methods_list_cb(callback):
    chat_id = callback.message.chat.id
    bot.send_message(chat_id, 'Получение списка методов...')

    buttons = await get_methods_list()
    markup = types.InlineKeyboardMarkup()

    markup.add(*buttons)
    bot.send_message(chat_id, 'Список методов:', reply_markup = markup)

    try:
        for method_name in get_methods_list():
            bot.send_message(chat_id, f'-> {method_name}')

    except Exception as error:
        bot.send_message(chat_id, 'Произошла ошибка при обращении к Google Sheets')

async def get_methods_list():
    google_sheet = GoogleSheet()
    methods_matrix: List[List[str]] = google_sheet._get_range_values(RANGE_METHODS_NAMES)
    return [row[0] for row in methods_matrix]

bot.polling(none_stop = True, interval = 0)
