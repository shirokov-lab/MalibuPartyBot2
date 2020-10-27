from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove




class UserGenerationKeyboard:
    @staticmethod
    def genstart():
        keyboard = InlineKeyboardMarkup()
        play_button = InlineKeyboardButton(text='Играть', callback_data='user_start_play_button')
        rules_button = InlineKeyboardButton(text='Правила', callback_data='user_start_rules_button')
        help_button = InlineKeyboardButton(text='Помощь', callback_data='user_start_help_button')
        reviews_button = InlineKeyboardButton(text='Отзывы', callback_data='user_start_reviews_button')
        
        keyboard.add(play_button, rules_button, help_button, reviews_button)
        return keyboard


    @staticmethod
    def play_bt():
        """ Ф-я по генерации кнопок "Играть" """
        keyboard = InlineKeyboardMarkup()
        buy_button = InlineKeyboardButton(text='Купить', callback_data='user_start_buy_button')
        keyboard.add(buy_button)
        return keyboard


    @staticmethod
    def game_bt():
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        truth_button = KeyboardButton(text='Правда')
        act_button = KeyboardButton(text='Действие')
        menu_button = KeyboardButton(text='Главное меню')
        keyboard.add(truth_button, act_button, menu_button)
        return keyboard


