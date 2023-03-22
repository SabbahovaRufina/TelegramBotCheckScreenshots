# TelegramBotCheckScreenshots

Бот делает скриншоты и ищет в них ключевые слова. Если ключевые слова найдены, бот отправляет сообщение.


1. Для программы нужно установить pytesseract по ссылке https://github.com/UB-Mannheim/tesseract/wiki и указать путь до exe файла в переменную среды path. В файле config в переменную pytesseract.tesseract_cmd вписать путь до exe файла;
2. Создать файл .env и вписать туда переменную TOKEN - токен телеграм бота;
3. В файле users должны быть разрешенные пользователи;
4. В файле Screenshot можно изменить ключевые слова.

