from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from db import db
from translation import _
import requests
def gender(message):

    lang = db.get_lang(message.chat.id)
    button = ReplyKeyboardMarkup()
    keyboard = InlineKeyboardMarkup(row_width=2)
    if lang == 'ru':
        url="https://raqamli-office.uz/api/form-request/details?language=ru"
    else:
        url="https://raqamli-office.uz/api/form-request/details?language=uz"
    def get_data(url):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception if status code is not 2xx
            data = response.json()  # Assuming the response is in JSON format
            return data
        except requests.exceptions.RequestException as e:
            print(f"Error occurred: {e}")
            return None

        # Example usage

# Replace with your API endpoint URL
    data = get_data(url)

    if data:
        for key in range(len(data)):
            buttons = [
                InlineKeyboardButton(data['genders'][key]['translation']['value'], callback_data=data['genders'][key]['id']),

            ]
            db.add_three(str(data['genders'][key]['id']), str(data['genders'][key]['translation']['value']), lang)
            keyboard.add(*buttons)

    return keyboard


def change_lang():

    button=ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Русский язык")

            ],
            [
                KeyboardButton(text="O'zbek tili")
            ],

        ],
        resize_keyboard=True
    )
    return button
def get_lang_for_button():

    button=ReplyKeyboardMarkup(

[   [
                KeyboardButton(text="Savol berish")
            ],
            [
                KeyboardButton(text="O'simlikni aniqlash")
            ],
    [
        KeyboardButton(text="O'simlik kasalliklari", web_app=WebAppInfo(
        url=str('https://old.assalomagro.uz/services/diseases'))),
        KeyboardButton(text="Zarakkunandalar", web_app=WebAppInfo(
        url=str('https://old.assalomagro.uz/services/pests')))
    ],
    [

    ],
    [
        KeyboardButton(text="Kimyoviy_vositalar", web_app=WebAppInfo(
        url=str('https://old.assalomagro.uz/services/chemical-products'))),
        KeyboardButton(text="Begona_o'tlar", web_app=WebAppInfo(
        url=str('https://old.assalomagro.uz/services/weeds')))
    ],
    [
        KeyboardButton(text="E'lon joylash", web_app=WebAppInfo(url=str('https://assalomagro.uz/elon/create')))
    ],




    [
        KeyboardButton(text="Agro expert", web_app=WebAppInfo(
        url=str('https://assalomagro.uz')))
    ],
    [
        KeyboardButton(text="Tilni tanlash")
    ],

        ],
        resize_keyboard=True
    )
    return button
def get_lang_for_buttonru():

    button=ReplyKeyboardMarkup(

[   [
                KeyboardButton(text="Задать вопрос")
            ],
    [
        KeyboardButton(text="Идентификация растения")
    ],
    [
        KeyboardButton(text="Болезни растений", web_app=WebAppInfo(
        url=str('https://old.assalomagro.uz/ru/services/diseases'))),
        KeyboardButton(text="Вредители", web_app=WebAppInfo(
        url=str('https://old.assalomagro.uz/ru/services/pests')))
    ],

    [
        KeyboardButton(text="Химические средства", web_app=WebAppInfo(
        url=str('https://old.assalomagro.uz/ru/services/chemical-products'))),
        KeyboardButton(text="Сорняки", web_app=WebAppInfo(
        url=str('https://old.assalomagro.uz/ru/services/weeds')))
    ],
    [
        KeyboardButton(text="Размещение объявления", web_app=WebAppInfo(
        url=str('https://assalomagro.uz/ru/elon/create')))
    ],

    [
        KeyboardButton(text="Agro expert", web_app=WebAppInfo(
        url=str('https://assalomagro.uz/ru')))
    ],
    [
        KeyboardButton(text="Выбрать язык")
    ],
        ],
        resize_keyboard=True
    )
    return button
def direction(message):
    lang = db.get_lang(message.chat.id)
    button=ReplyKeyboardMarkup()
    keyboard = InlineKeyboardMarkup(row_width=2)
    if lang == 'ru':
        url="https://raqamli-office.uz/api/industries?project=business-challenge&language=ru"
    else:
        url="https://raqamli-office.uz/api/industries?project=business-challenge&language=uz"
    def get_data(url):

        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception if status code is not 2xx
            data = response.json()  # Assuming the response is in JSON format
            return data
        except requests.exceptions.RequestException as e:
            print(f"Error occurred: {e}")
            return None


 # Replace with your API endpoint URL
    data = get_data(url)
    if data:
        for key in range(len(data)):


            id=data[key]['id']
            value=data[key]['translation']['value']
            db.add_one(id, value,lang)
            buttons = [
                InlineKeyboardButton(value, callback_data=id),


            ]

            keyboard.add(*buttons)

        keyboard.add(InlineKeyboardButton(_("Boshqa",lang), callback_data=_("boshqa",lang)))

    return keyboard
def gmail(message):
    lang = db.get_lang(message.from_user.id)
    button=ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_("O'tkazib yuborish",lang)),
            ]],
        resize_keyboard=True
    )
    return button
def check(message):
    lang = db.get_lang(message.from_user.id)
    button=ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_("Tasdiqlash", lang)),
            ],
            [
                KeyboardButton(text=_("Qayta toldirish", lang)),
            ],
            [
                KeyboardButton(text=_("Arizani bekor qilish", lang)),
            ]
        ],

        resize_keyboard=True
    )
    return button
def region(message):

    lang = db.get_lang(message.chat.id)
    button = ReplyKeyboardMarkup()
    keyboard = InlineKeyboardMarkup(row_width=2)
    if lang == "ru":
        url="https://raqamli-office.uz/api/regions?language=ru"
    else:
        url="https://raqamli-office.uz/api/regions?language=uz"
    def get_data(url):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception if status code is not 2xx
            data = response.json()  # Assuming the response is in JSON format
            return data
        except requests.exceptions.RequestException as e:
            print(f"Error occurred: {e}")
            return None

        # Example usage


    data = get_data(url)
    if data:
        for key in range(len(data)):
            buttons = [
                InlineKeyboardButton(data[key]['translation']['value'], callback_data=data[key]['id']),

            ]
            db.add_two(data[key]['id'], data[key]['translation']['value'],lang)
            keyboard.add(*buttons)

    return keyboard


# def get_project_for_user(message):
#     lang = db.get_lang(message.from_user.id)
#     button=ReplyKeyboardMarkup(
#         keyboard=[
#             [
#                 KeyboardButton(text=_("Protestim",lang)
#     )
#             ],
#             [
#                 KeyboardButton(text=_("2 chi proyekt",lang))
#             ],
#             [
#                 KeyboardButton(text=_("3 chi proyekt",lang)
#     )
#             ],
#             [
#                 KeyboardButton(text=_("4 chi proyekt",lang))
#             ],
#
#         ],
#         resize_keyboard=True
#     )
#     return button


def change_lang():

    button=ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Русский язык")

            ],
            [
                KeyboardButton(text="O'zbek tili")
            ],

        ],
        resize_keyboard=True
    )
    return button
def changelang():

    button=ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Tilni o'zgartirish")

            ],

        ],
        resize_keyboard=True
    )
    return button
def key(lang):

    if lang=='uz':
        keyboardcontakt=ReplyKeyboardMarkup(

            keyboard=[[

                KeyboardButton(text="Kontakni yuborish",
                               request_contact=True

                               )
                ],

            ],resize_keyboard=True

        )
        return keyboardcontakt
    elif lang=='ru':
        keyboardcontakt=ReplyKeyboardMarkup(

            keyboard=[[

                KeyboardButton(text="Отправить контакт",
                               request_contact=True

                               )
                ],

            ],resize_keyboard=True

        )
        return keyboardcontakt