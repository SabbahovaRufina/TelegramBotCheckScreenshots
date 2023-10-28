from pyautogui import screenshot
from pytesseract import pytesseract
from PIL import Image, ImageEnhance
from Bot import HIGH, WIDTH
from re import search
from dotenv import load_dotenv
from os import environ


load_dotenv()
user = environ['USER']
pytesseract.tesseract_cmd = rf"C:\Users\{user}\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"


class Screenshot:
    def __init__(self, path):
        self.path = path

    async def get_screenshot(self):
        screenshot(self.path)

    async def get_text_from_screenshot(self) -> str:
        with Image.open(self.path) as img:
            img = img.resize((WIDTH, HIGH))
            img = ImageEnhance.Contrast(img)
            img = img.enhance(2)
            return pytesseract.image_to_string(img, lang='rus').lower().replace('погибели', '')

    @staticmethod
    async def is_reg_exp_in_words(text: str, regex: str) -> bool:
        if search(regex, text):
            return True
        return False

    async def is_right(self, regex) -> bool:
        text = await self.get_text_from_screenshot()
        return await self.is_reg_exp_in_words(text, regex)

