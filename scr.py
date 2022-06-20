import logging
import requests
from bs4 import BeautifulSoup
import telebot
from telebot import types
import random
from dotenv import load_dotenv
import os

# конфигурация логирования в боте
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.ERROR, filename='bot_logs.log', filemode='w')

# загрузка и получение переменных из .env файлаъ
load_dotenv()
bot_token = os.getenv('TOKEN')

bot = telebot.TeleBot(bot_token)  # API-токен бота в телеграм


# запуск бота
@bot.message_handler(commands=["start"])
def start(message):
    # вывод кнопки
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    sent_joke = types.KeyboardButton("screenshot")
    markup.add(sent_joke)

    bot.send_message(
        message.chat.id, "hi", parse_mode="html", reply_markup=markup
    )


# обработка кнопки screenshot
@bot.message_handler(content_types=["text"])
def message_processing(message):
    try:
        url = generate_url()
        photo = get_photo(url)

        bot.send_photo(message.chat.id, photo)

    # если отправить скриншот не удалось -
    # пользователю выводится сообщение об ошибке
    except Exception as error:
        logging.error(f'ошибка при отправке скриншота: {error}')
        bot.send_message(message.chat.id, "error")


# генерация случайной ссылки со скриншотом
def generate_url():
    try:
        letters = [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
        ]
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        url = "https://prnt.sc/"
        return (
            url
            + random.choice(letters)
            + random.choice(letters)
            + random.choice(numbers)
            + random.choice(numbers)
            + random.choice(numbers)
            + random.choice(numbers)
        )

    except Exception as error:
        logging.error(f'ошибка при генерации ссылки: {error}')


# получение фото с сайта
def get_photo(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 YaBrowser/19.10.2.195 Yowser/2.5 Safari/537.36"
        }

        html = requests.get(url, headers=headers).text
        soup = BeautifulSoup(html, "lxml")

        img_tag = soup.find("img", {"id": "screenshot-image"})
        photo_url = img_tag["src"]

        return photo_url

    except Exception as error:
        logging.error(f'ошибка при получении фото с сайта: {error}')


def main():
    # строка чтоб бот принимал сообщения
    bot.polling(non_stop=True)


if __name__ == "__main__":
    main()
