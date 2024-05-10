# import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from config import animals, animals_photo


class QuizException(Exception):
    pass


class Quiz:
    @staticmethod
    def button(*args):
        result = None
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        for i in args:
            result = markup.add(KeyboardButton(i))
        return result
    # def button(btn_1, btn_2=None):
    #     markup = ReplyKeyboardMarkup(resize_keyboard=True)
    #     btn_yes = KeyboardButton(f"{btn_1}")
    #     btn_no = KeyboardButton(f"{btn_2}")
    #     result = markup.add(btn_yes, btn_no)
    #     return result


class Animal:
    def __init__(self, size=None, food=None, climate=None, daily_reg=None):
        self.size = size
        self.food = food
        self.climate = climate
        self.daily_reg = daily_reg
        self.animals = []
        self.ans = None

    def set_animal(self, *args):
        for i in args:
            self.animals.append(i)

    def match(self):
        match_animals = []
        for index, value in animals.items():
            if self.animals == value:
                match_animals.append(index)
        for index, value in animals.items():
            if self.animals[0:-1] == value[0:-1] and not match_animals:
                print(self.animals, "/x", value, index)
                match_animals.append(index)
        print(match_animals)
        return match_animals

    @staticmethod
    def animal_photo(animal):
        for i in animals_photo:
            if i == animal:
                return animals_photo[i]
