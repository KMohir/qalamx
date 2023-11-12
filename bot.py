# -*- coding: utf-8 -*-
import time

import openai
from lxml import etree
from aiogram.dispatcher.filters import Command
import config
import logging

import asyncio
from gpytranslate import Translator
import json
import requests
from bs4 import BeautifulSoup
from aiogram import Bot, Dispatcher, executor, types
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ParseMode, Message, ReplyKeyboardRemove, ContentType
from aiogram.types.web_app_info import WebAppInfo
from db import db


from keyboards.default.reply import key, get_lang_for_button, change_lang, get_lang_for_buttonru
from keyboards.inline.support import langMenu, support_keyboard, yesno
from loader import dp, bot

# from keyboards.default.reply import get_lang_for_button, get_project_for_user
from states.state import answer, RegistrationStates, questions, language, imagestate
from translation import _
from utils.set_bot_commands import set_default_commands
import ast
import random
import time
from multiprocessing.pool import Pool

from aiogram import Bot, Dispatcher

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions

from selenium.webdriver.common.by import By
import time

from selenium.webdriver.chrome.service import Service
import ast
from aiogram import Bot, Dispatcher


from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.options import Options
import g4f
# options = Options()
#
#
# # disable webdriver mode
#
# # for older ChromeDriver under version 79.0.3945.16
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option("useAutomationExtension", False)
#
# # for ChromeDriver version 79.0.3945.16 or over
# options.add_argument("--disable-blink-features=AutomationControlled")
#
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.9999.999 Safari/537.36"
#
#
#
#
# options.add_argument('headless')
# options.add_argument('window-size=1920x1080')
# options.add_argument("disable-gpu")
#
# driver = webdriver.Chrome(options=options)
#
#
#
#
#
#
#
#
# driver.get('https://www.picturethisai.com/ru/mobileSearch')
#
# photo1 = WebDriverWait(driver, 70).until(
#      EC.presence_of_element_located((By.XPATH, '//*[@id="mobile_vector_btn"]'))).click()
# apple = WebDriverWait(driver, 70).until(
#      EC.presence_of_element_located((By.XPATH, '//*[@id="appleid-signin"]/div/div[1]'))).click()
#
# time.sleep(5)
#
# all_windows = driver.window_handles
# driver.switch_to.window(all_windows[-1])
#
#
# apple_id_field = driver.find_element(By.XPATH,'//*[@id="account_name_text_field"]')
#
#
# apple_id_field.send_keys(str(input('email kiriting: ')))
# apple_id_field_next = driver.find_element(By.XPATH,'//*[@id="sign-in"]')
# apple_id_field_next.click()
# time.sleep(10)
# password_field = driver.find_element(By.XPATH, '//*[@id="password_text_field"]')  # Replace with the actual ID of the password input field.
#   # Replace with the actual ID of the password input field.
#
# password_field.send_keys('201219Fda1*')
# password_field = driver.find_element(By.XPATH, '//*[@id="sign-in"]').click()
# time.sleep(15)
#
# code1 = driver.find_element(By.XPATH, '//*[@id="char0"]')
# code1.send_keys(int(input('birinchi raqam: ')))
# code2 = driver.find_element(By.XPATH, '//*[@id="char1"]')
# code2.send_keys(int(input('ikkinchi raqam: ')))
# code3 = driver.find_element(By.XPATH, '//*[@id="char2"]')
# code3.send_keys(int(input('uchinchi raqam: ')))
# code4 = driver.find_element(By.XPATH, '//*[@id="char3"]')
# code4.send_keys(int(input('tortinchi raqam: ')))
# code5 = driver.find_element(By.XPATH, '//*[@id="char4"]')
# code5.send_keys(int(input('beshinchi raqam: ')))
# code6 = driver.find_element(By.XPATH, '//*[@id="char5"]')
# code6.send_keys(int(input('oltinchi raqam: ')))
#
#
#
# apple = WebDriverWait(driver, 70).until(
#      EC.presence_of_element_located((By.CLASS_NAME, 'float-left'))).click()
# apple = WebDriverWait(driver, 70).until(
#      EC.presence_of_element_located((By.CLASS_NAME, 'weight-medium'))).click()
#
#
# # You may need to locate the "Next" button and click it to complete the login process.
#
# print('Rasm tashash mumkun')
# driver.switch_to.window(all_windows[0])
t = Translator()
global lang
openai.api_key = config.OPENAI_TOKEN
errors=0
@dp.message_handler(text="Savol berish")
@dp.message_handler(text="Задать вопрос")
async def chat0(message:Message):
    lang = db.get_lang(message.from_user.id)
    await message.answer(_("Agro soxa bo`yicha savollingizni yuboring", lang),reply_markup=ReplyKeyboardRemove())
    await RegistrationStates.chatgptfull.set()
@dp.message_handler(state=RegistrationStates.chatgptfull)
async def chat(message:Message,state:FSMContext):

    lang = db.get_lang(message.from_user.id)

    lang = db.get_lang(message.from_user.id)
    model_engine = "text-davinci-003"
    max_tokens = 128  # default 1024
    prompt = await t.translate(message.text, targetlang="en")
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt.text,
        max_tokens=max_tokens,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    await message.answer(_("Assalomagro javobni izlamoqda ...", lang))
    translated_result = await t.translate(completion.choices[0].text, targetlang=str(lang))
    await message.answer(f'Savol: {message.text}\n\nJavob: {translated_result.text}')

    if lang=='uz':
        await message.answer("O'zingizga kerakli bo'limni tanlang", reply_markup=get_lang_for_button())
    elif lang=='ru':
        await message.answer("Выберите нужный раздел", reply_markup=get_lang_for_buttonru())
    await state.finish()
@dp.message_handler(text="Изменить язык")
@dp.message_handler(text="Tilni o'zgartirish")
async def process_name(message: Message, state: FSMContext):
    lang = db.get_lang(message.from_user.id)
    if message.text == "Tilni o'zgartirish" or message.text == 'Изменить язык' or message.text=='/image':
        if message.text == "Tilni o'zgartirish":
            lang = db.get_lang(message.from_user.id)
            await message.answer(_('Tilni tanlang', lang), reply_markup=change_lang())
        elif message.text=="Изменить язык":
            lang = db.get_lang(message.from_user.id)
            await message.answer(_('Изменить язык', lang), reply_markup=change_lang())
            await language.lang.set()
        elif message.text=='/image':

            await imagestate.image1.set()
        @dp.message_handler(state=language.lang)
        async def bot_echo(message: types.Message, state: FSMContext):
            lang = db.get_lang(message.from_user.id)
            if message.text == "O'zbek tili":
                db.change_lang(message.from_user.id, 'uz')
                await message.answer("Til o'zgartirildi", reply_markup=get_lang_for_button(lang))
                await state.finish()
            elif message.text == "Русский язык":
                db.change_lang(message.from_user.id, 'ru')
                await message.answer("Язык был обновлен", reply_markup=get_lang_for_buttonru())

            else:
                await message.answer("O'zingizga kerakli bo'limni tanlang", reply_markup=get_lang_for_button())

    await state.finish()

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message, state: FSMContext):

    if not db.user_exists(message.from_user.id):
        await bot.send_message(message.from_user.id,'Assalomu aleykum AssalomAgro botiga hush kelibsiz!\nЗдравствуйте, добро пожаловать в бот  AssalomAgro!')
        await bot.send_message(message.from_user.id,'Tilni tanlang:\nВыберите язык:',reply_markup=langMenu)
        await RegistrationStates.lang.set()

    else:

            lang = db.get_lang(message.from_user.id)
            if message.text=="Tilni o'zgartirish" or message.text=='Изменить язык':
                lang = db.get_lang(message.from_user.id)
                await message.answer(_('Tilni tanlang', lang), reply_markup=change_lang())
                await language.lang.set()
            elif message.text=='Изменить язык':
                lang = db.get_lang(message.from_user.id)
                await message.answer(_('Выберите язык', lang), reply_markup=change_lang())
                await language.lang.set()
                @dp.message_handler(state=language.lang)
                async def bot_echo(message: types.Message, state: FSMContext):
                    lang = db.get_lang(message.from_user.id)
                    if message.text == "O'zbek tili":
                        db.change_lang(message.from_user.id, 'uz')
                        await message.answer("Til o'zgartirildi", reply_markup=get_lang_for_button(lang))
                        await state.finish()
                    elif message.text == "Русский язык":
                        db.change_lang(message.from_user.id, 'ru')
                        await message.answer("Язык был обновлен", reply_markup=get_lang_for_buttonru())
                        await state.finish()
                    else:
                        await state.finish()
            else:
                if lang == 'uz':
                    await message.answer("O'zingizga kerakli bo'limni tanlang", reply_markup=get_lang_for_button())
                elif lang == 'ru':
                    await message.answer("Выберите нужный раздел", reply_markup=get_lang_for_buttonru())
                await state.finish()
@dp.message_handler(text="Orqaga")
@dp.message_handler(text="Назад")
async def back(message: types.Message):
    lang=db.get_lang(message.from_user.id)
    if lang=='uz':
        await message.answer("O'zingizga kerakli bo'limni tanlang", reply_markup=get_lang_for_button())
    elif lang=='ru':
        await message.answer("Выберите нужный раздел", reply_markup=get_lang_for_buttonru())



@dp.message_handler(text="/change_language")
@dp.message_handler(text="change_language")
@dp.message_handler(text="Tilni tanlash")
@dp.message_handler(text="Выбрать язык")
async def bot_echo(message: types.Message):
    lang=db.get_lang(message.from_user.id)
    await message.answer(_('Tilni tanlang',lang),reply_markup=change_lang())
    await language.lang.set()
@dp.message_handler(state=language.lang)
async def bot_echo(message: types.Message,state: FSMContext):
    lang=db.get_lang(message.from_user.id)
    if message.text == "O'zbek tili":
        db.change_lang(message.from_user.id, 'uz')
        await message.answer("Til o'zgartirildi",reply_markup=get_lang_for_button())
        await state.finish()
    elif message.text == "Русский язык":

        db.change_lang(message.from_user.id, 'ru')
        await message.answer("Язык был обновлен",reply_markup=get_lang_for_buttonru())
        await state.finish()

@dp.callback_query_handler(text_contains="lang_",state=RegistrationStates.lang)
async def set_lang(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    if not db.user_exists(call.from_user.id):

        lang=call.data[5:]
        async with state.proxy() as data:

            data['lang'] = lang


        if lang =='uz':
            await bot.send_message(call.from_user.id,"Ism familiyangizni kiriting")
        elif lang =='ru':
            await bot.send_message(call.from_user.id, "Введите свое имя и фамилию")


        await RegistrationStates.name.set()




@dp.message_handler(state=RegistrationStates.name)
async def register_command_handler(message: types.Message, state: FSMContext):
    name=message.text
    data = await state.get_data()

    lang=data.get('lang')
    async with state.proxy() as data:

        data['name'] = name
    if lang=="uz":
        await message.answer("Telefon raqamingizni kiriting",reply_markup=key(lang))
    elif lang=="ru":
        await message.answer("Введите свой номер телефона",reply_markup=key(lang))
    await RegistrationStates.end.set()

# Name handler

# Phone handler

@dp.message_handler(state=RegistrationStates.end, content_types=types.ContentType.TEXT)
async def process_name(message: Message, state: FSMContext):
    data = await state.get_data()

    lan=data.get('lang')
    contact =message.text

    data = await state.get_data()
    name = data.get('name')

    # contact = message.contact.phone_number
    data = await state.get_data()

    db.update(message.chat.id,lan,name,contact)

    if lan=='uz':
        await message.answer("Tabriklaymiz, ro'yxatdan muvaffaqiyatli o'tdingiz! !🎉", reply_markup=ReplyKeyboardRemove())
        await message.answer("O'zingizga kerakli bo'limni tanlang", reply_markup=get_lang_for_button())
    elif lan=='ru':
        await message.answer("Поздравляем, регистрация прошла успешно! !🎉",
                             reply_markup=ReplyKeyboardRemove())
        await message.answer("Выберите раздел, который вам нужен",
                             reply_markup=get_lang_for_buttonru())
    await state.finish()






@dp.message_handler(state=RegistrationStates.end, content_types=types.ContentType.CONTACT)
async def process_name(message: Message, state: FSMContext):

    data = await state.get_data()
    name = data.get('name')
    lan=data.get('lang')
    contact = str(message.contact.phone_number)
    data = await state.get_data()
    db.update(message.from_user.id,lan,name,contact)

    if lan == 'uz':
        await message.answer("Tabriklaymiz, ro'yxatdan muvaffaqiyatli o'tdingiz! !🎉",
                             reply_markup=ReplyKeyboardRemove())
        await message.answer("O'zingizga kerakli bo'limni bo'limni tanlap oling",
                             reply_markup=get_lang_for_button())
    elif lan == 'ru':
        await message.answer("Поздравляем, регистрация прошла успешно! !🎉",
                             reply_markup=ReplyKeyboardRemove())
        await message.answer("Выберите раздел, который вам нужен",
                             reply_markup=get_lang_for_buttonru())
    await state.finish()
@dp.message_handler(text="O'simlikni aniqlash")
@dp.message_handler(text='Идентификация растения')
@dp.message_handler(state=imagestate.image2)
@dp.message_handler(Command('image'))
async def process_photo(message: types.Message):
    # Получаем список фотографий в сообщении
    lang = db.get_lang(message.from_user.id)
    await message.answer(_("Soon", lang))







if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
