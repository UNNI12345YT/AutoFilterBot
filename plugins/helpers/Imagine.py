from pyrogram import Client, filters
import requests

@Client.on_message(filters.command('imagine'))
async def imagine(client, message):
    prompt = " ".join(message.text.split()[1:])
    
    if not prompt:
        await message.reply_text("Please provide a prompt.")
        return
    
    txt = await message.reply_text("🔍 Generating image...")
    
    url = 'https://nandha-api.onrender.com/imagine'
    params = {
        'prompt': prompt
    }

    headers = {
        'accept': 'application/json'
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        await txt.edit(str(data))
    except requests.exceptions.RequestException as e:
        error_details = {
            'error': str(e),
            'response_content': response.content.decode('utf-8') if response.content else None
        }
        await txt.edit(f"Error: {error_details}")

# Run the bot
app = Client("my_bot")

app.run()
