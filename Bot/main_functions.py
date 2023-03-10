from Screenshot import Screenshot
from JSONFile import JSONFile
from config import PATH_SCHEDULE_SCREENSHOT, PATH_SCREENSHOT, DESKS
import pyautogui
from handlers import send_message


async def get_message_text(user_id, n):
    file = JSONFile()
    if await file.is_user_in_right_users(user_id):
        await file.put_new_data(user_id, n)
        return "Бот запущен." if n else "Бот остановлен."
    else:
        return "Вы не в списке разрешенных пользователей."


async def get_new_screenshot(user_id, path=PATH_SCREENSHOT):
    file = JSONFile()
    if await file.is_user_in_right_users(user_id):
        screen = Screenshot(path)
        await screen.get_screenshot()
        return path
    else:
        return None


async def make_screenshot(desk, path=PATH_SCHEDULE_SCREENSHOT):
    screen = Screenshot(path)
    file = JSONFile()
    await screen.get_screenshot()
    if await screen.is_right():
        for chat in await file.get_work_users():
            await send_message(chat, f"Возможно, вы погибли. Рабочий стол {desk}", screen.path)


async def loop_desks(desks=DESKS):
    assert desks >= 1
    for desk in range(desks):
        if desk != 0:
            pyautogui.hotkey('ctrl', 'win', 'right')
        await make_screenshot(desk + 1)
    else:
        for _ in range(desks - 1):
            pyautogui.hotkey('ctrl', 'win', 'left')


