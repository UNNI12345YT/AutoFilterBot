from pyrogram import Client, filters

Client.on_message(filters.command("hack"))
async def hackai(client, message):
import requests

mes = "what is your name"
ow = "@UNNIdud"
botname = "Natasha"
api = f"https://horridluffyllamaapi-f66a74967a84.herokuapp.com/hackai?query={mes}"
res = requests.get(api)
dd = res.json()
m = dd ['response']
await message.reply_text(m)
