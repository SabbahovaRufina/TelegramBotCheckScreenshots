import pyautogui
from pytesseract import pytesseract

pytesseract.tesseract_cmd = r"C:\Users\Dimaslav\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

# разрешение экрана, умноженное на 2 - для лучшего чтения данных с изображения
WIDTH = pyautogui.size().width * 2
HIGH = pyautogui.size().height * 2

# пути скриншотов для простого запроса скриншота и для скриншота, делаемого программой по расписанию
PATH_SCREENSHOT = r"screenshots\screen.png"
PATH_SCHEDULE_SCREENSHOT = r"screenshots\scheduler_screen.png"

# время в минутах, через которое программа будет делать скриншот по расписанию
INTERVAL_TIME = 2


# регулярное выражение гибели (в любом регистре)
REG_EXP = r"(вы погиб?)|(погиб)"

# регулярное выражение запуска (в любом регистре)
REG_EXP_GAME = r"(запуск)|(запуск игры)"