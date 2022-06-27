# kittybot/kittybot.py

import logging
import os

import requests

from telegram import ReplyKeyboardMarkup
from telegram.ext import CommandHandler, Updater

from dotenv import load_dotenv 

load_dotenv()

secret_token = os.getenv('TOKEN')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)


URL = 'https://api.thecatapi.com/v1/images/search'
CAT_URL = 'https://api.thecatapi.com/v1/images/search'
DOG_URL = 'https://api.thedogapi.com/v1/images/search'


def get_new_image(URL):
    try:
        response = requests.get(URL)
    except Exception as error:
        # Печатать информацию в консоль теперь не нужно:
        # всё необходимое будет в логах
        # print(error)
        logging.error(f'Ошибка при запросе к основному API: {error}')
        new_url = 'https://api.thedogapi.com/v1/images/search'
        response = requests.get(new_url)

    response = response.json()
    random_cat = response[0].get('url')
    return random_cat


def new_animal(update, context, animal, url):
    chat = update.effective_chat
    name = update.message.chat.first_name
    image = get_new_image(url)
    logging.info(f'Отправлен {animal} {image} для {name}')
    context.bot.send_photo(chat.id, image)
    
def new_cat(update, context):
    new_animal(update, context, 'котик', CAT_URL)
    
def new_dog(update, context):
    new_animal(update, context, 'пёсик', DOG_URL)
    

def wake_up(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    button = ReplyKeyboardMarkup([['/newcat', '/newdog']], resize_keyboard=True)
    context.bot.send_message(
        chat_id=chat.id,
        text=f'Привет, {name}. Посмотри какого котика я тебе нашел',
        reply_markup=button
    )
    image = get_new_image()
    logging.info(f'Отправлен котик {image} для {name}')
    context.bot.send_photo(chat.id, image)


def main():
    updater = Updater(token=secret_token)

    updater.dispatcher.add_handler(CommandHandler('start', wake_up))
    updater.dispatcher.add_handler(CommandHandler('newcat', new_cat))
    updater.dispatcher.add_handler(CommandHandler('newdog', new_dog))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()