from pyrogram import Client, filters, enums
from info import ADMINS

@Client.on_message(filters.command("echo") & filters.user(ADMINS))
async def echo(_, message):
   reply = message.reply_to_message
   chat_id = message.chat.id
   if len(message.text.split()) > 1 and reply:
       await reply.reply_text(message.text.split(None, 1)[1]) 
   await message.delete()     
