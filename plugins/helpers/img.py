from pyrogram import Client, filters, types as t,errors
import traceback,random,datetime,os,io
import asyncio,base64,mimetypes,os
from lexica import AsyncClient
from lexica.constants import languageModels
import httpx
from urllib.parse import urlsplit
from .pastebins import nekobin
from bot import TelegraphClient




async def SearchImages(query,search_engine) -> dict:
    client = AsyncClient()
    output = await client.SearchImages(query,0,search_engine)
    await client.close()
    return output


def getText(message):
    """Extract Text From Commands"""
    text_to_return = message.caption if message.caption else message.text
    if message.text is None:
        return None
    if " " in text_to_return:
        try:
            return message.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None


def getImageContent(url):
    """Get Image Content"""
    try:
        client = httpx.Client()
        response = client.get(cleanUrl(url))
        if response.status_code != 200:
            return None
        imageType = response.headers["content-type"].split("/")[1]
        if imageType == "gif":
            return None
        return response.content
    except (TimeoutError, httpx.ReadTimeout, httpx.ReadError):
        return None



@Client.on_message(filters.command(["img","image","imagesearch"]))
async def searchImages(_: Client,m:t.Message):
    try:
        reply = await m.reply_text("⏳")
        prompt = getText(m)
        if prompt is None:
            return await reply.edit("What do you want to search?")
        output = await SearchImages(prompt,"google")
        if output['code'] != 2:
            return await reply.edit("Ran into an error.")
        images = output['content']
        if len(images) == 0:
            return await reply.edit("No results found.")
        images = random.choices(images,k=8 if len(images) > 8 else len(images))
        media = []
        for image in images:
            content = getImageContent(image['imageUrl'])
            if content is None:
                images.remove(image)
                continue
            else:
                media.append(t.InputMediaPhoto(io.BytesIO(content)))
        await m.reply_media_group(
            media,
            quote=True
            )
        await reply.delete()
    except (errors.ExternalUrlInvalid, errors.WebpageCurlFailed,errors.WebpageMediaEmpty) as e:
        print(e)
        return await reply.edit("Ran into an error.")
    except Exception as e:
        traceback.print_exc()
        return await reply.edit("Ran into an error.")
    
