from aiogram import Bot, Dispatcher, executor, types
import asyncio
import aioschedule
import main_functions as mf
from config import INTERVAL_TIME
from os import environ
from dotenv import load_dotenv
from keyboard import markup


load_dotenv()
bot = Bot(token=environ['TOKEN'])
dp = Dispatcher(bot)


async def on_startup(_):
    asyncio.create_task(scheduler())


async def send_message(user_id, text=None, photo=None, document=None):
    if photo:
        with open(photo, 'rb') as img:
            await bot.send_photo(chat_id=user_id, photo=img, caption=text, reply_markup=markup)
    elif document:
        with open(document, 'rb') as img:
            await bot.send_document(chat_id=user_id, document=img, caption=text, reply_markup=markup)
    elif text:
        await bot.send_message(chat_id=user_id, text=text, reply_markup=markup)


@dp.message_handler(commands='start')
async def process_start(message: types.Message):
    text = await mf.get_message_text(message.chat.id, 1)
    await send_message(message.chat.id, text=text)
    await message.delete()


@dp.message_handler(commands='finish')
async def process_finish(message: types.Message):
    text = await mf.get_message_text(message.chat.id, 0)
    await send_message(message.chat.id, text=text)
    await message.delete()


@dp.message_handler(commands='screenshot')
async def process_screenshot(message: types.Message):
    path = await mf.get_new_screenshot(message.chat.id)
    await send_message(message.chat.id, document=path)
    await message.delete()


async def scheduler():
    aioschedule.every(INTERVAL_TIME).minutes.do(mf.loop_desks)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)


