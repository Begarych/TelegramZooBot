import telebot
from utils import Quiz, Animal
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from random import randint
from config import dist_feature as feature
# from telebot.async_telebot import AsyncTeleBot

TOKEN = "7092685897:AAHQKu564iEwHbMGPg5kGIvjBDP5Aw1-wSA"


bot = telebot.TeleBot(TOKEN)
# bot = AsyncTeleBot(TOKEN)
user_animal = Animal()


@bot.message_handler(commands=["start"])
def start(message: telebot.types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn = KeyboardButton("Начать Викторину")
    markup.add(btn)
    bot.send_message(message.chat.id, text=f"Привет {message.chat.username}, это бот который поможет узнать твое"
                                           " тотемное животное!\n"
                                           "Скорей жми на кнопку снизу, чтобы начать!",  reply_markup=markup)


@bot.message_handler(content_types=["text"])
def main(message: telebot.types.Message):
    if message.text == "Начать Викторину" or message.text == "Еще разок?":
        # markup = ReplyKeyboardMarkup(resize_keyboard=True)
        # btn_yes = KeyboardButton("Жаркий")
        # btn_no = KeyboardButton("Холодный")
        # markup.add(btn_yes, btn_no)
        user_animal.animals.clear()
        markup = Quiz.button(feature['cold'], feature['heat'])
        bot.send_message(message.chat.id, text="Первый вопрос:\n"
                                               "Ты любишь жаркий или холодный климат?", reply_markup=markup)

    elif message.text == feature['cold'] or message.text == feature['heat']:
        user_animal.climate = message.text
        markup = Quiz.button(feature['big'], feature['small'])
        bot.send_message(message.chat.id, text="Второй вопрос:\n"
                                               "Тебе больше по душе большое тело или"
                                               " маленькое?", reply_markup=markup)
        print(user_animal.climate)

    elif message.text == feature['big'] or message.text == feature['small']:
        user_animal.size = message.text
        markup = Quiz.button(feature['meat'], feature['vegetables'])
        bot.send_message(message.chat.id, text="Третий вопрос:\n"
                                               "Любишь мясо или овощи?", reply_markup=markup)
        print(user_animal.size)

    elif message.text == feature['meat'] or message.text == feature['vegetables']:
        user_animal.food = message.text
        markup = Quiz.button(feature['day'], feature['night'])
        bot.send_message(message.chat.id, text="Четвертый вопрос:\n"
                                               "Спишь днем или ночью?", reply_markup=markup)
        print(user_animal.food)

    elif message.text == feature['day'] or message.text == feature['night']:
        user_animal.daily_reg = message.text
        markup = Quiz.button("Еще разок?")
        user_animal.set_animal(user_animal.climate, user_animal.food, user_animal.size, user_animal.daily_reg)
        # chosen_animal = user_animal.match()
        chosen_animal = user_animal.match()[randint(0, len(user_animal.match())-1)]
        # for i in user_animal.match():
        #     chosen_animal += f"\n{i}\n"
        bot.send_message(message.chat.id, text=f"Позравляю ваше тотемное животное: {chosen_animal}\n"
                                               f"Вы можете почитать о нем и помочь ему благадоря новой программе курирования животного!\n"
                                               f"Подробнее на сайте московского зоопарка:\n"
                                               f"{user_animal.animal_photo(chosen_animal)[1]}", reply_markup=markup)
        bot.send_photo(message.chat.id, photo=f'{user_animal.animal_photo(chosen_animal)[0]}')
        print(len(user_animal.match()))

    else:
        bot.send_message(message.chat.id, text="Паша иди ка ты нахуй, чеел?")


print(user_animal.animals)
bot.polling(skip_pending=True)
