from pyrogram import Client, filters
import requests
import json

@Client.on_message(filters.command('mgpt'))
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
                'content': "You are a Malayalam talking assistant. Your owner is @UNNIdud.",
            },
            {
                'role': "user",
                'content': text,
            },
        ],
        "model_id": 3
    }

    api = 'https://api.qewertyy.dev/models'

    try:
        response = requests.post(api, json=payload)
        response.raise_for_status()
        data = response.json()
        await txt.edit(data['content'])
    except requests.exceptions.RequestException as e:
        error_details = {
            'error': str(e),
            'response_content': response.content.decode('utf-8') if response.content else None,
            'payload': json.dumps(payload, indent=2)
        }
        await txt.edit(f"Error: {error_details}")



