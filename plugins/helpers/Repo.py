import logging
import os
import requests
from pyrogram import Client, filters


@Client.on_message(filters.command('repo','rp'))
async def git(Kashmira, message):
    pablo = await message.reply_text("Processing...")
    args = message.text.split(None, 1)[1]
    if len(message.command) == 1:
        await pablo.edit("No input found")
        return
    r = requests.get("https://api.github.com/search/repositories", params={"q": args})
    lool = r.json()
    if lool.get("total_count") == 0:
        await pablo.edit("File not found")
        return
    else:
        lol = lool.get("items")
        qw = lol[0]
        txt = f"""
Name : {qw.get("name")}

Full Name : {qw.get("full_name")}

Link : {qw.get("html_url")}

Fork Count : {qw.get("forks_count")}

Open Issues : {qw.get("open_issues")}

"""
        if qw.get("description"):
            txt += f'Description : {qw.get("description")}'

        if qw.get("language"):
            txt += f'Language : {qw.get("language")}'

        if qw.get("size"):
            txt += f'Size : {qw.get("size")}'

        if qw.get("score"):
            txt += f'Score : {qw.get("score")}'

        if qw.get("created_at"):
            txt += f'Created At : {qw.get("created_at")}'

        if qw.get("archived") == True:
            txt += f"This Project is Archived"
        await pablo.edit(txt, disable_web_page_preview=True)
