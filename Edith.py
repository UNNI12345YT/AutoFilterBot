from pyrogram import Client, filters
import requests

# Initialize Pyrogram client
api_id = 27408015
api_hash = "2f07e7c921c8d2b982df12d65a46ca46"
bot_token = "6235483959:AAGkutp90SCxO3RaJuhPC0CG99iDKxOStUY"

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# /mgpt command handler
@app.on_message(filters.command('edith'))
async def lexica_askbot(client, message):
    text = message.text.split()[1:]
    text = " ".join(text)
    
    if not text:
        await message.reply_text("Give An Input !!")
        return
    
    txt = await message.reply_text("🔍")
    
    payload = {
        'messages': [
            {
                'role': "system",
                'content': "Your name is E.D.I.T.H, your meaning is EVEN DEATH I AM HERO. You are an AI developed by @UNNIdud",
            },
            {
                'role': "user",
                'content': text,
            },
        ],
        "model_id": 23
    }

    api = 'https://api.qewertyy.dev/models'

    try:
        response = requests.post(api, json=payload)
        response.raise_for_status()  # Raises an error for bad status codes
        data = response.json()
        await txt.edit(data.get('content', 'No response content'))
    except requests.RequestException as e:
        await txt.edit(f"Error: {e}")
    except ValueError:
        await txt.edit("Failed to parse response")

# /photographer command handler
@app.on_message(filters.command('pgpt'))
async def photographer_askbot(client, message):
    text = message.text.split()[1:]
    text = " ".join(text)
    
    if not text:
        await message.reply_text("Give An Input !!")
        return
    
    txt = await message.reply_text("🔍")
    
    url = "https://api.safone.dev/chatgpt"
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    data = {
        "message": text,
        "version": 3,
        "chat_mode": "photographer",
        "dialog_messages": "[{\"bot\":\"\",\"user\":\"\"}]"
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raises an error for bad status codes
        data = response.json()
        await txt.edit(data.get('response', 'No response content'))
    except requests.RequestException as e:
        await txt.edit(f"Error: {e}")
    except ValueError:
        await txt.edit("Failed to parse response")

# Start the Pyrogram client
if name == "main":
    app.run()
