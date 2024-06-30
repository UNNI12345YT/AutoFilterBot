import logging
import requests
from pyrogram import Client, filters
import urllib.parse

# Define the command handler for /wiki
@Client.on_message(filters.command("wiki"))
async def wiki_search(client, message):
    query = " ".join(message.command[1:])
    if not query:
        await message.reply_text("Please provide a query to search for.")
        logging.info("No query provided.")
        return

    logging.info(f"Searching for: {query}")

    # Encode the query for URL
    encoded_query = urllib.parse.quote(query)

    # Make the API request to Safone Wikipedia Search API
    url = f"https://api.safone.dev/wiki?query={encoded_query}"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    logging.info(f"Requested URL: {url}")

    if response.status_code == 200:
        data = response.json()
        logging.info(f"Response received: {data}")

        if 'results' in data and data['results']:
            response_text = ""
            for result in data['results']:
                title = result.get("title", "No Title")
                description = result.get("description", "No Description")
                link = result.get("link", "No Link")
                result_text = f"{title}\n{description}\nRead more: {link}\n\n"
                if len(response_text) + len(result_text) > 4096:
                    await message.reply_text(response_text)
                    response_text = result_text
                else:
                    response_text += result_text
            
            if response_text:
                await message.reply_text(response_text)
        else:
            await message.reply_text("No results found.")
            logging.info("No results found.")
    else:
        await message.reply_text("Failed to fetch data. Please try again later.")
        logging.error(f"Failed to fetch data. Status code: {response.status_code}")
