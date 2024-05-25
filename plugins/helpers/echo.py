from pyrogram import Client, filters, enums
from info import *
from pyrogram.types import *

@Client.on_message(filters.command("echo"))
async def echo(client, message):
    user = await client.get_chat_member(message.chat.id, message.from_user.id)
    if user.status not in [enums.ChatMemberStatus.OWNER, enums.ChatMemberStatus.ADMINISTRATOR]:
        raise PermissionError("You are not allowed to use this command")
    reply = message.reply_to_message
    chat_id = message.chat.id
    if reply and len(message.text.split()) > 1:
        await reply.reply_text(message.text.split(None, 1)[1])
    await message.delete()
