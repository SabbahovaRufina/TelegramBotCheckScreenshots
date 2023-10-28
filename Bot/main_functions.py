from Screenshot import Screenshot
from JSONFile import JSONFile
from Bot import PATH_SCHEDULE_SCREENSHOT, PATH_SCREENSHOT, REG_EXP_GAME, REG_EXP
from handlers import send_message


async def get_message_text(user_id, n):
    file = JSONFile()
    if await file.is_user_in_right_users(user_id):
        await file.put_new_data(user_id, n)
        return "Уведомления бота включены" if n else "Уведомления бота выключены"
    else:
        return "Вы не в списке разрешенных пользователей"


async def get_new_screenshot(user_id, path=PATH_SCREENSHOT):
    file = JSONFile()
    if await file.is_user_in_right_users(user_id):
        screen = Screenshot(path)
        await screen.get_screenshot()
        return path
    else:
        return None


async def make_screenshot(path=PATH_SCHEDULE_SCREENSHOT):
    screen = Screenshot(path)
    file = JSONFile()
    await screen.get_screenshot()
    if await screen.is_right(regex=REG_EXP.lower()):
        for chat in await file.get_work_users():
            await send_message(user_id=chat, text=f"Возможно, вы погибли!", photo=screen.path)
    elif await screen.is_right(regex=REG_EXP_GAME.lower()):
        for chat in await file.get_work_users():
            await send_message(user_id=chat, text=f"Запуск игры!", photo=screen.path)

