from aiogram import Bot, Dispatcher, executor, types
import asyncio
import aioschedule
import main_functions as mf
from config import INTERVAL_TIME
import os
from dotenv import load_dotenv


load_dotenv()
bot = Bot(token=os.environ['TOKEN'])
dp = Dispatcher(bot)


async def on_startup(_):
    asyncio.create_task(scheduler())


async def send_message(user_id, text=None, path=None):
    if path:
        with open(path, 'rb') as img:
            await bot.send_photo(chat_id=user_id, photo=img)
    if text:
        await bot.send_message(chat_id=user_id, text=text)


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
    await send_message(message.chat.id, path=path)
    await message.delete()


async def scheduler():
    aioschedule.every(INTERVAL_TIME).minutes.do(mf.loop_desks)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)


