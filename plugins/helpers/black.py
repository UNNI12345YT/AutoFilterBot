import uuid
import re
import aiohttp

from aiohttp import FormData
from pyrogram import Client as pgram, filters, types, enums, errors

def id_generator() -> str:
    return str(uuid.uuid4())

async def upload_image(session, file_name, user_id, image):
    data = FormData()
    data.add_field('fileName', file_name)
    data.add_field('userId', user_id)
    data.add_field('image', image, filename=file_name, content_type='image/jpeg')
    api_url = "https://www.blackbox.ai/api/upload"
    async with session.post(api_url, data=data) as response:
        response.raise_for_status()
        return await response.json()

async def chat_with_blackbox(session, messages, user_id):
    data = {
        "messages": messages,
        "user_id": user_id,
        "codeModelMode": True,
        "agentMode": {},
        "trendingAgentMode": {},
    }
    headers = {"Content-Type": "application/json"}
    url = "https://www.blackbox.ai/api/chat"
    async with session.post(url, headers=headers, json=data) as response:
        response.raise_for_status()
        return await response.text()

def clean_response(response_text):
    cleaned_response_text = re.sub(r'^\$?@?\$?v=undefined-rv\d+@?\$?|\$?@?\$?v=v\d+\.\d+-rv\d+@?\$?', '', response_text)
    text = cleaned_response_text.strip()[2:]
    if "$~~~$" in text:
        text = re.sub(r'\$~\$.*?\$~\$', '', text, flags=re.DOTALL)
    return text

@pgram.on_message(filters.command("bk"))
async def blackbox(bot, message):
    async with aiohttp.ClientSession() as session:
        m = message
        msg = await m.reply_text("🔍")

        if len(m.text.split()) == 1:
            return await msg.edit_text(
                "Type some query buddy 🐼\n"
                "/blackbox text with reply to the photo or just text"
            )
        else:
            prompt = m.text.split(maxsplit=1)[1]
            user_id = id_generator()
            image = None

            if m.reply_to_message and (m.reply_to_message.photo or (m.reply_to_message.sticker and not m.reply_to_message.sticker.is_video)):
                file_name = f'blackbox_{m.chat.id}.jpeg'
                file_path = await m.reply_to_message.download(file_name=file_name)
                with open(file_path, 'rb') as file:
                    image = file.read()

            if image:
                try:
                    response_json = await upload_image(session, file_name, user_id, image)
                except aiohttp.ClientError as e:
                    return await msg.edit_text(f"❌ Error uploading image: {str(e)}")

                messages = [
                    {
                        "role": "user",
                        "content": response_json['response'] + "\n#\n" + prompt
                    }
                ]

                try:
                    response_text = await chat_with_blackbox(session, messages, user_id)
                except aiohttp.ClientError as e:
                    return await msg.edit_text(f"❌ Error chatting with Blackbox: {str(e)}")

                cleaned_text = clean_response(response_text)
                return await msg.edit_text(text=cleaned_text)
            else:
                reply = m.reply_to_message
                if reply and reply.text:
                    prompt = f"Old conversation:\n{reply.text}\n\nQuestion:\n{prompt}"

                messages = [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]

                try:
                    response_text = await chat_with_blackbox(session, messages, user_id)
                except aiohttp.ClientError as e:
                    return await msg.edit_text(f"❌ Error chatting with Blackbox: {str(e)}")

                cleaned_text = clean_response(response_text)
                return await msg.edit_text(text=cleaned_text)
