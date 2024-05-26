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
        
    
