import requests
from pyrogram import Client, filters

@Client.on_message(filters.command("hackai"))
async def hack_ai(client, message):
    query = message.text.split(' ', 1)[1]  
    api = f"https://horrid-api.onrender.com/hackai?query={query}"

    try:
        res = requests.get(api)
        data = res.json()
        response = data['response']
        await message.reply_text(response)
    except Exception as e:
        await message.reply_text(f"An error occurred: {str(e)}")
