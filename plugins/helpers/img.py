import asyncio
from pyrogram import Client, filters
import requests
import wget 

@Client.on_message(filters.command(["image", "img", "image_serch", "photo"]))
async def safoneapi(client, message):
    try:
        user_query = ' '.join(message.command[1:])
        if not user_query:
            await message.reply_text("Please provide a keyword to search for an image.")
        encoded_query = user_query.replace(" ", "%20")

        response = requests.get(f"https://api.safone.dev/image?query={encoded_query}&limit=10")
        if response.status_code == 200:
            data = response.json()
            image_data = data['results'][0]
            image_url = image_data['imageUrl']
            downloaded_image = wget.download(image_url)
            kndi = await message.reply_text("`Serching...`")
            await client.send_photo(message.chat.id, downloaded_image)     
            kndi.delete()

    except Exception as e:
        await message.reply_text(f"An error occurred\nMybe it's error is api problem: {e}")