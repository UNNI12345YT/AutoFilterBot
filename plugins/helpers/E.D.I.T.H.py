from pyrogram import Client, filters
import requests

@Client.on_message(filters.command('edith'))
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
                'content': "Your name is E.D.I.T.H, your meaning is EVEN DEATH I AM HERO.You are an AI,Developed by @UNNIdud",
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
