import config
from utilites import get_current_time, generate_image
from telethon.sync import TelegramClient
from telethon.tl.functions.photos import (UploadProfilePhotoRequest, 
										DeletePhotosRequest)

def main():
	previouse_time = ''
	with TelegramClient(config.session_name, config.api_id, config.api_hash) as client:
		while True:
			if not previouse_time == get_current_time():
				current_time = get_current_time()
				previouse_time = current_time
				generate_image(current_time)
				
				image = client.upload_file('time_image.jpg')
				client(DeletePhotosRequest(client.get_profile_photos('me')))
				client(UploadProfilePhotoRequest(image))
	
if __name__ == "__main__":
        print('-=start time=-')
        main()
