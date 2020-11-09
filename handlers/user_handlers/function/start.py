from misc import bot, dp
from aiogram import types
from data_base.functions import Datafunc
from data_base.models import User
from handlers.user_handlers.helpers.generator_keyboards import UserGenerationKeyboard
from config import PAY_TOKEN, TEXTS, ADMINS_ID
import datetime
import random
from aiogram.dispatcher import FSMContext


@dp.message_handler(commands = ['start'])
async def start(message:types.Message):
    user = Datafunc.get_user(message.from_user.id)
    keyboard = UserGenerationKeyboard.genstart()
    if user:
        await message.answer(TEXTS["start1"])
        await message.answer(TEXTS["start2"])
        await message.answer(TEXTS["start3"])
        await message.answer(TEXTS["start4"], reply_markup=keyboard)
        
    else:
        await message.answer(TEXTS["start1"])
        await message.answer(TEXTS["start2"])
        await message.answer(TEXTS["start3"])
        await message.answer(TEXTS["start4"], reply_markup=keyboard)
        user = User(id=message.from_user.id, chat_id = message.chat.id, username = message.from_user.username)
        Datafunc.add(user)



@dp.message_handler(text='Правда')
async def send_truth(message: types.Message, state: FSMContext):
    user = Datafunc.get_user(message.from_user.id)
    if (user.is_payed) == False and ((user.id in ADMINS_ID) == False):
        await message.answer(TEXTS["pay_please"]) 
        return

    data = await state.get_data()

    if ('dict_user_pictures' in data.keys()) == False: #Проверка, что хранилище создано
        await state.update_data(dict_user_pictures={})
        data = await state.get_data()
    
    if (str(user.id) in data['dict_user_pictures'].keys()) == False: #Проверка, что ID пользователя, который написал нет в хранилище
        data['dict_user_pictures'][f'{user.id}'] = {'truth' : [], 'actions' : []}
        await state.update_data(dict_user_pictures=data['dict_user_pictures'])

    truths = [pic.id for pic in Datafunc.get_truth()] #Генератор листов. Создаем лист только из ID полученных картинок
    sends_truths = list(set(truths) - set(data['dict_user_pictures'][f'{user.id}']['truth']))

    if (len(sends_truths) == 0): #Обнуляем лист, если кончились картинки
        sends_truths = truths
        data['dict_user_pictures'][f'{user.id}']['truth'].clear()
        await state.update_data(dict_user_pictures=data['dict_user_pictures'])

    randomik = random.randint(0, len(sends_truths)-1) #Отправляем случайную картинку, из тех, что не было
    pic = Datafunc.get_pic_truth(sends_truths[randomik])
    await message.answer_photo(types.InputFile(pic.filename))

    data['dict_user_pictures'][f'{user.id}']['truth'].append(sends_truths[randomik]) # Обновляем список отправленных картинок
    await state.update_data(dict_user_pictures=data['dict_user_pictures'])


@dp.message_handler(text='Действие')
async def send_act(message: types.Message, state: FSMContext):
    user = Datafunc.get_user(message.from_user.id)
    if (user.is_payed) == False and ((user.id in ADMINS_ID) == False):
        await message.answer(TEXTS["pay_please"])  
        return

    data = await state.get_data()

    if ('dict_user_pictures' in data.keys()) == False: #Проверка, что хранилище создано
        await state.update_data(dict_user_pictures={})
        data = await state.get_data()
    
    if (str(user.id) in data['dict_user_pictures'].keys()) == False: #Проверка, что ID пользователя, который написал нет в хранилище
        data['dict_user_pictures'][f'{user.id}'] = {'truth' : [], 'actions' : []}
        await state.update_data(dict_user_pictures=data['dict_user_pictures'])

    acts = [pic.id for pic in Datafunc.get_acts()] #Генератор листов. Создаем лист только из ID полученных картинок
    sends_acts = list(set(acts) - set(data['dict_user_pictures'][f'{user.id}']['actions']))

    if (len(sends_acts) == 0): #Обнуляем лист, если кончились картинки
        sends_acts = acts
        data['dict_user_pictures'][f'{user.id}']['actions'].clear()
        await state.update_data(dict_user_pictures=data['dict_user_pictures'])

    randomik = random.randint(0, len(sends_acts)-1) #Отправляем случайную картинку, из тех, что не было
    pic = Datafunc.get_pic_act(sends_acts[randomik])
    await message.answer_photo(types.InputFile(pic.filename))

    data['dict_user_pictures'][f'{user.id}']['actions'].append(sends_acts[randomik]) # Обновляем список отправленных картинок
    await state.update_data(dict_user_pictures=data['dict_user_pictures'])


@dp.message_handler(text='Главное меню')
async def send_menu(message: types.Message):
    keyboard = UserGenerationKeyboard.genstart()
    await message.answer(TEXTS["start4"], reply_markup=keyboard)

@dp.callback_query_handler(lambda callback: callback.data=='user_start_rules_button')
async def rules_bt(callback:types.CallbackQuery):
    await callback.answer() 
    await callback.message.answer(TEXTS["rules"])

@dp.callback_query_handler(lambda callback: callback.data=='user_start_help_button')
async def help_bt(callback:types.CallbackQuery):
    await callback.answer() 
    await callback.message.answer(TEXTS["helper"])

@dp.callback_query_handler(lambda callback: callback.data=='user_start_reviews_button')
async def reviews_bt(callback:types.CallbackQuery):
    await callback.answer() 
    await callback.message.answer(TEXTS["reviews2"])
    await callback.message.answer(TEXTS["reviews1"])


@dp.message_handler(text = 'SendAll')
async def spam(message: types.Message):
    users = Datafunc.get_all_user()
    for person in users:
        if person.is_payed == False:
            try:
                await bot.send_message(chat_id=person.id,text=TEXTS["fixed"])
            except:
                pass