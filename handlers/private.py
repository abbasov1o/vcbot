from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""Mən **{bn}** !!
Səsli söhbətdə mahnı oxutdururam 😉
Komandalardan istifadə edin:
⚜️ /play - __Mahnı faylı və ya youtube link atın linkə yanıt verin.__
⚜️ /pause - __Mahnını saxlamaq.__
⚜️ /resume - __Mahnını davam etdirmək.__
⚜️ /skip - __Oxunulan mahnını ötürmək üçün.__
⚜️ /stop - __Botu dayandırmaq.__
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Qrup 💬", url="https://t.me/songazerbaycan"
                    ),
                    InlineKeyboardButton(
                        "Kanal 📣", url="https://t.me/elisbots"
                    )
                ]
            ]
        )
    )
