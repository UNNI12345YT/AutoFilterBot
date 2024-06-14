import random
from pyrogram import Client, filters

@Client.on_message(filters.command("wish"))
async def wishh(client, message):
    if len(message.text.split()) == 1:
        await message.reply_text("Give An Input!!")
    else:
        text = message.text.split(" ", 1)[1]
        fuck = random.randint(0, 100)
        await message.reply_video(video="https://telegra.ph/file/d1d405b2a608ded8f045f.mp4", caption=f"<b> Hello 🤗 {message.from_user.mention}\nYour Wish `{text}` 😁\nPossible To {fuck}% 😳</b>")

@Client.on_message(filters.command("pro"))
async def prooz(client, message):
    if message.reply_to_message:
        reply = message.reply_to_message
        kk = random.randint(0, 100)
        await reply.reply_video(video="https://telegra.ph/file/f55b445f3002b5363aac2.mp4", caption=f"<b>{reply.from_user.mention} Is\n\n{kk}% Pro ☠️</b>")
    else:
        fuck = random.randint(0, 100)
        await message.reply_video(video="https://telegra.ph/file/f55b445f3002b5363aac2.mp4", caption=f"<b>{message.from_user.mention} Is\n\n{fuck}% Pro ☠️</b>")



@Client.on_message(filters.command("noob"))
async def nbooz(client, message):
    if message.reply_to_message:
        reply = message.reply_to_message
        kk = random.randint(0, 100)
        await reply.reply_video(video="https://telegra.ph/file/151f8b2b231e9bc78e7b1.mp4", caption=f"<b>{reply.from_user.mention} Is\n\n{kk}% Noob 😥</b>")
    else:
        fuck = random.randint(0, 100)
        await message.reply_video(video="https://telegra.ph/file/151f8b2b231e9bc78e7b1.mp4", caption=f"<b>{message.from_user.mention} Is\n\n{fuck}% Noob 😢</b>")
