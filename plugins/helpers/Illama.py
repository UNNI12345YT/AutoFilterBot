import requests
from pyrogram import filters, Client
from pyrogram.types import Message
from pyrogram import Client, filters
import httpx

api_url_chat5 = "https://nandha-api.onrender.com/ai/gpt"

def fetch_data(api_url: str, query: str) -> tuple:
    try:
        response = requests.get(f"{api_url}/{query}")
        response.raise_for_status()
        data = response.json()
        if data.get("code") == 2:
            return data.get("content", "No response from the API."), None
        else:
            return None, f"API error: {data.get('message', 'Unknown error')}"
    except requests.exceptions.RequestException as e:
        return None, f"Request error: {e}"
    except Exception as e:
        return None, f"An error occurred:"




@Client.on_message(filters.command(["openai","gpt"]))
async def chatgpt5(_: Client, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("Give An Input!!")

    query = " ".join(message.command[1:])    
    txt = await message.reply_text("⏳")
    api_response, error_message = fetch_data(api_url_chat5, query)
    d = api_response or error_message
    await txt.edit(f"ʜᴇʏ: {message.from_user.mention}\n\nϙᴜᴇʀʏ: {query}\n\nʀᴇsᴜʟᴛ:\n\n{d}")
    


@Client.on_message(filters.command(["bard", "gemini"]))
async def bardandgemini(_: Client, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("Give An Input!!")

    query = " ".join(message.command[1:])    
    txt = await message.reply_text("⏳")
    app = f"https://api.qewertyy.dev/models?model_id=20&prompt={query}"
    response = requests.post(app)
    data = response.json()
    api = data['content']
    await txt.edit(f"ʜᴇʏ: {message.from_user.mention}\n\nϙᴜᴇʀʏ: {query}\n\nʀᴇsᴜʟᴛ:\n\n{api}")



@Client.on_message(filters.command(["llama", "llamaai"]))
async def llama_ailecixa(_: Client, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("Give An Input!!")

    query = " ".join(message.command[1:])    
    txt = await message.reply_text("⏳")
    app = f"https://api.safone.dev/llama?query={query}"
    response = requests.get(app)
    data = response.json()
    api = data['answer']
    await txt.edit(f"ʜᴇʏ: {message.from_user.mention}\n\nϙᴜᴇʀʏ: {query}\n\nʀᴇsᴜʟᴛ:\n\n{api}")
