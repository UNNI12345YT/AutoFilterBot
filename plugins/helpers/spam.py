from pyrogram import *
from info import *
import random


TEXT = ["Da purinta mowna nenda dady yude group annoda nayinta mowne anda dady da puri", "Andi illatha nayinda mowne nenta achan", "baka nayinta mowna pund chekka poyi umfi da thoyilalinda mowne", "dai nenta achanta andinda avadatha romam poyi parachu vada naya", "yathin annu bro spam chayunath 🥺 last warning yani chaythal ban okay ", "eda mowna nayinta mowne nenta dadynda group anno da andi kuthi kalikuna myrenda mowme nenta achan rathril sex chayunath nenak aroyoda naya"]


@Client.on_message(filters.command("spam") & filters.user(ADMINS))
async def nolink(bot, message):
    text = random.choice(TEXT)
    reply = message.reply_to_message
    await message.reply_text(f"Hey {reply.from_user.mention}\n{text}")
    await message.delete()
