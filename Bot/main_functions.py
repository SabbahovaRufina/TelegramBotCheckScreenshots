from Screenshot import Screenshot
from JSONFile import JSONFile
from config import PATH_SCHEDULE_SCREENSHOT, PATH_SCREENSHOT, DESKS
from handlers import send_message
from pyautogui import hotkey
from asyncio import sleep


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
    if await screen.is_right():
        for chat in await file.get_work_users():
            await send_message(chat, f"Возможно, вы погибли", screen.path)


async def loop_desks(desks=DESKS):
    assert desks >= 1
    for desk in range(desks):
        if desk == 0:
            await make_screenshot()
            continue
        hotkey('ctrl', 'win', 'right')
        await sleep(2)
        await make_screenshot()
    else:
        for _ in range(desks - 1):
            await sleep(1)
            hotkey('ctrl', 'win', 'left')

