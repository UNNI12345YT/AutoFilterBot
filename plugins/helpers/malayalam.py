from pyrogram import Client, filters
import requests

@Client.on_message(filters.command('mgpt'))
async def lexica_askbot(client, message):
    text = message.text.split()[1:]
    text = " ".join(text)
    if not text:
        await message.reply_text("Give An Input !!")
    if len(text) == 0:
        return await message.reply_text("Give An Input !!", parse_mode="Markdown")
    txt = await message.reply_text("🔍")
    payload = {
        'messages': [
            {
                'role': "system",
                'content': "your Are a malayalam talking assistant, Your owner is @UNNIdud",
            },
            {
                'role': "user",
                'content': text,
            },
        ],
        "model_id": 19
    }

    api = 'https://api.qewertyy.dev/models'

    response = requests.post(api, json=payload)
    data = response.json()
    await txt.edit(data['content'])
