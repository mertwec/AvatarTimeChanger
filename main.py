import resources.config as config
from resources.utilites import get_current_time, generate_image
from telethon import TelegramClient
from telethon.tl.functions.photos import (UploadProfilePhotoRequest, 
                                          DeletePhotosRequest)
import asyncio
import time


async def main():
    previouse_time = ''
    async with TelegramClient(config.session_name, config.api_id, config.api_hash) as client:
        while True:
            if not previouse_time == get_current_time():
                current_time = get_current_time()
                previouse_time = current_time
                generate_image(current_time)
                
                image = await client.upload_file('time_image.jpg')
                await client(DeletePhotosRequest(await client.get_profile_photos('me')))
                await client(UploadProfilePhotoRequest(image))
                time.sleep(10)
                #print('update time')
                


if __name__ == "__main__":
    #print('-=start time=-')
    asyncio.run(main())
    #asyncio.get_event_loop().run_until_complete(main())
