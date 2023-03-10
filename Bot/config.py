from pytesseract import pytesseract
import pyautogui

pytesseract.tesseract_cmd = r'C:\Users\Dima vse horosho\AppData\Local\Tesseract-OCR\tesseract.exe'

# разрешение экрана, умноженное на 2 - для лучшего чтения данных с изображения
WIDTH = pyautogui.size().width * 2
HIGH = pyautogui.size().height * 2

# пути скриншотов для простого запроса скриншота и для скриншота, делаемого программой по расписанию
PATH_SCREENSHOT = r"screenshots\screen.png"
PATH_SCHEDULE_SCREENSHOT = r"screenshots\scheduler_screen.png"

# время в минутах, через которое программа будет делать скриншот по расписанию
INTERVAL_TIME = 2

# кол-во рабочих столов
DESKS = 1

