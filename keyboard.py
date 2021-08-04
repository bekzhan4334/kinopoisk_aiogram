from aiogram import Bot, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

start = types.ReplyKeyboardMarkup(resize_keyboard=True) # СОЗДАЕМ ВООБЩЕ ОСНОВУ ДЛЯ КНОПОК

search = types.KeyboardButton("Поиск фильмов")           # ДОБАВЛЯЕМ КНОПКУ ИНФОРМАЦИИ
news = types.KeyboardButton("Новости")     # ДОБАВЛЯЕМ КНОПКУ СТАТИСТИКИ


start.add(search,news) #ДОБАВЛЯЕМ ИХ В БОТА