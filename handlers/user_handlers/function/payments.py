from misc import bot, dp
from aiogram import types
from data_base.functions import Datafunc
from data_base.models import User
from handlers.user_handlers.helpers.generator_keyboards import UserGenerationKeyboard
from config import PAY_TOKEN, TEXTS, ADMINS_ID
import datetime



@dp.callback_query_handler(lambda callback: callback.data=='user_start_play_button')
async def play_bt(callback:types.CallbackQuery):
    await callback.answer()
    user = Datafunc.get_user(callback.from_user.id)
    if (user.is_payed) == True or (user.id in ADMINS_ID):
        await callback.message.answer(text=TEXTS["thanks"],reply_markup=UserGenerationKeyboard.game_bt())
    else:
        if PAY_TOKEN.split(':')[1] == 'TEST':
            await callback.message.answer('Для оплаты используйте данные тестовой карты: 1111 1111 1111 1026, 12/22, CVC 000.')
        price = types.LabeledPrice(label='Malibu Party Bot', amount=20000)
        await bot.send_invoice(
            callback.message.chat.id,
            title='Malibu Party Bot',
            description='Игра остается с вами навсегда',
            provider_token=PAY_TOKEN,
            currency="rub",
            prices=[price],
            start_parameter='eto_start_parametr',
            payload=datetime.datetime.now().timestamp()
        )



'''hendel ya.kasy '''
@dp.pre_checkout_query_handler(state='*')
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

@dp.message_handler(state='*',content_types=types.ContentTypes.SUCCESSFUL_PAYMENT)
async def suc_pay(message: types.Message):
    user = Datafunc.get_user(message.from_user.id)
    user.is_payed = True
    Datafunc.commit()
    await message.answer(text=TEXTS["thanks_payment"], reply_markup=UserGenerationKeyboard.genstart())