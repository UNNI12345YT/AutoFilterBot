from pyrogram import Client as feed, filters
from pyrogram.types import *
from info import LOG_CHANNEL

@feed.on_message(filters.command("feedback"))
async def feedda(client, message):
  fa = message.text.split(" ", 1)[1]
  await message.reply_text(f"Hi {message.from_user.mention},\n Thanks for Feed Back 😊")

  await client.send_message(LOG_CHANNEL, text=f"#Feedbackfromvazha\n\nfeeed back : <code>{fa}</code> user : {message.from_user.mention}") # 😁


@feed.on_message(filters.command("bug"))
async def bug(client, message):
  bug = message.text.split(" ", 1)[1]
  await message.reply_text(f"Hi {message.from_user.mention},\n Successfully Reported bugs to my devploers ")

  await client.send_message(LOG_CHANNEL, text=f"#error \n\nfrom {message.from_user.mention}\n error mes: <code>{bug}</code>")
  
