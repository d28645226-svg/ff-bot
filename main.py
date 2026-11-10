import os
import time
import requests
from telegram import Bot
 TOKEN="9166658709:AAHrVgxEgtrt1UV_gXwRlKV2-jCd_eFqlU"
CHANNEL_USERNAME="@TopFreeFireSkinlar2026"

bot = Bot(token=TOKEN)

def get_free_fire_skin_info():
text = (
"🔥 Free Fire Yangi Skinlari! 🔥\n\n"
"⏰ Har 10 daqiqada yangilanib turuvchi maxsus skin ma'lumotlari.\n"
"✨ O'yinga kirib o'z uslubingizni sinab ko'ring!"
)
return text

def main():
print("Bot ishga tushdi va har 10 minutda xabar yubormoqda...")
while True:
try:
skin_message = get_free_fire_skin_info()
bot.send_message(chat_id=CHANNEL_USERNAME, text=skin_message, parse_mode="Markdown")
print("Post muvaffaqiyatli yuborildi!")
except Exception as e:
print(f"Xatolik yuz berdi..: {e}")

time.sleep(600)

if name == 'main':
main()

