from PIL import Image, ImageFont, ImageDraw
from datetime import datetime
from pytz import timezone

def get_current_time():
	'''
	рассчет текущего времени в зависимости от часового пояса
	'''
	return datetime.now(timezone('Europe/Kiev')).strftime('%H:%M')

def generate_image(text):
	'''создаем картинку 500х500 с часами
	'''
	image = Image.new('RGB', (500,500), color='black')
	h,w = image.size
	drawning = ImageDraw.Draw(image)
	
	font = ImageFont.truetype(font = 'resources/Chiller.ttf', size=230)
	wt, ht = drawning.textsize(text, font=font) # size of text
	drawning.text(((w - wt) / 2, (h - ht) / 2 ), text, font=font, fill='#1BDD1E') # прорисовка текста
	
	image.save('time_image.jpg')
	
	
if __name__ == "__main__":
	curent_time = get_current_time()
	generate_image(curent_time)

