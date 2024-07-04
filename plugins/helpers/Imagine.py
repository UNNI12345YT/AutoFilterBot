from pyrogram import Client, filters
import requests

@Client.on_message(filters.command('imagine'))
async def imagine(client, message):
    prompt = " ".join(message.text.split()[1:])
    
    if not prompt:
        await message.reply_text("Please provide a prompt.")
        return
    
    txt = await message.reply_text("🔍 Generating image...")
    
    url = 'https://nandha-api.onrender.com/imagine'
    params = {
        'prompt': prompt
    }

    headers = {
        'accept': 'application/json'
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()

        # Check the content type of the response
        content_type = response.headers.get('Content-Type')
        if 'application/json' in content_type:
            data = response.json()
            await txt.edit(str(data))
        else:
            # Handle binary data
            await txt.edit("Received binary data. Cannot display directly.")
            
    except requests.exceptions.RequestException as e:
        error_details = {
            'error': str(e),
            'response_content': None
        }
        # Attempt to decode response content if it exists
        if response.content:
            try:
                error_details['response_content'] = response.content.decode('utf-8')
            except UnicodeDecodeError:
                error_details['response_content'] = "Binary data received"
        
        await txt.edit(f"Error: {error_details}")

# Run the bot
if __name__ == "__main__":
    app = Client("my_bot")
    app.start()
    print("Bot is running...")
    app.idle()
    app.stop()
