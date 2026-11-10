import os
import time
import requests
from aiogram import Bot

TOKEN = "9166658709:AAHrVgEgtrt1UV_gXwRlHZP8p2n7d3Vj5oI"
CHANNEL_NAME = "@TopFreeFireSkin"

bot = Bot(token=TOKEN)

def get_free_fire_skin_info():
    text = (
        "🔥 Скинлари для Янги в Free Fire! 🔥\n\n"
        "⏰ Har 10 daqiqada yangilanib turuvchi ma'lumot!\n"
        "✨ O'yinga kirib o'z uslubingizni sinab ko'ring."
    )
    return text

def main():
    print("Bot ishga tushdi va har 10 daqiqada ishlaydi...")
    while True:
        try:
            skin_message = get_free_fire_skin_info()
            bot.send_message(chat_id=CHANNEL_NAME, text=skin_message)
            print("Post muvaffaqiyatli yuborildi!")
        except Exception as e:
            print(f"Xatolik yuz berdi: {e}")
        
        time.sleep(600)

if __name__ == '__main__':
    main()
