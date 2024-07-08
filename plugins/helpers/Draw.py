from telegram import InputMediaPhoto, constants
from nandha import aiohttpsession as session
from nandha.helpers.decorator import command, send_action



module = 'Draw'

help = '''
*Commands*:

- /draw <query>: to draw anything using text to image generation.
'''



async def get_output(prompt: str):

    '''
    
    Purpose: generate text to image.
    Required: prompt - str
    Return: list of generated image url

    By @NandhaBots
    '''
    
    url = 'https://modelslab.com/api/v6/images/text2img'
    headers = {'Content-Type': 'application/json'}
  
    data = {
       "key": "6vLUPaIGLBMTCTCE4NPv3qk2eKlZfgWK6Jw2McaufGCMD6c5Ezd3gdY2MayF",
       "model_id": "anything-v3",
       "prompt": prompt,
       "negative_prompt": "painting, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, deformed, ugly, blurry, bad anatomy, bad proportions, extra limbs, cloned face, skinny, glitchy, double torso, extra arms, extra hands, mangled fingers, missing lips, ugly face, distorted face, extra legs, anime",
       "width": "512",
       "height": "512",
       "samples": "2",
       "num_inference_steps": "30",
       "seed": None,
       "guidance_scale": 7.5,
       "webhook": None,
       "track_id": None
       }
  
    async with session.post(
      url, 
      headers=headers, 
      json=data
    ) as response:
        images = []
  
        if response.status == 200:
            images = (await response.json()).get('output')
        return images


@command(('draw', 'imagine'))
@send_action(constants.ChatAction.UPLOAD_PHOTO)
async def AI_DRAW(update, context):
    
     
    
     m = update.message
     bot = context.bot
  
     if len(m.text.split()) == 1:
        return await m.reply_text(
           text='*🙋 Write some text to draw....*',
          parse_mode=constants.ParseMode.MARKDOWN
        )
     prompt = m.text.split(maxsplit=1)[1]

     msg = await m.reply_text(
        text='*✨ Drawing please wait some seconds..*',
        parse_mode=constants.ParseMode.MARKDOWN
     )
  
     images = await get_output(prompt)
    
     if images:
         media = []
         for image_url in images:
             media.append(
                 InputMediaPhoto(image_url)
             )
         try:
           is_send = await bot.send_media_group(
             chat_id=m.chat.id,
             media=media, 
             reply_to_message_id=m.message_id
             )
           if is_send:
               return await msg.delete()
         except Exception as e:
             return await msg.edit_text(f'❌ Error: {str(e)}')
     else:
         return await msg.edit_text('❌ No media Generated!')
