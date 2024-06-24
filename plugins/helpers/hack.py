import requests
from pyrogram import Client, filters

@Client.on_message(filters.command("hack"))
async def hack_ai(client, message):
    try:
        query = message.text.split(' ', 1)[1]
        api = f"https://horrid-api.onrender.com/hackai?query={query}"

        res = requests.get(api)
        data = res.json()
        response = data['response']
        await message.reply_text(response)
    except IndexError:
        await message.reply_text("Please provide a query to proceed.")
    except Exception as e:
        await message.reply_text(f"An error occurred: {str(e)}")
