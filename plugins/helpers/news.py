from pyrogram import Client, filters
import requests

@Client.on_message(filters.command("news"))
def latest_news(client, message):
    query = message.text.split(" ")[1]  # assuming the query is the second word in the message
    response = requests.get(f"https://horrid-api.onrender.com/news?query={query}")
    if response.status_code == 200:
        news_data = response.json()
        news_title = news_data.get("title")
        news_source = news_data.get("source")
        news_url = news_data.get("url")
        client.send_message(chat_id=message.chat.id, text=f"📰 Latest News:\n\nTitle: {news_title}\nSource: {news_source}\nURL: {news_url}")
    else:
        client.send_message(chat_id=message.chat.id, text="Failed to fetch the latest news. Please try again later.")
