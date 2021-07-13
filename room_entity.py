import datetime
from bs4 import Tag

class RoomEntity:
	def __init__(self, url:str,room_id: str, price: str, location: str, create_date: datetime, from_date: datetime, until_date: datetime):
		self.id = room_id
		self.url = url
		self.price = price
		self.location = location
		self.create_date = create_date
		self.from_date = from_date
		self.until_date = until_date


	@staticmethod
	def parse_from_html(entry:Tag):
		print_info("Parsing html file to room entity")
		wgzimmer_url_header = "https://www.wgzimmer.ch"
		room_a_tag = entry.contents[3]
		room_url = wgzimmer_url_header + room_a_tag['href']
		room_id = entry.contents[0]['id']
		room_price = room_a_tag.find(class_="cost").text
		room_location = room_a_tag.find(class_="thumbState").text.replace('\n',' ')
		from_date_str, until_date_str = room_a_tag.find(class_='from-date').text.split('\n')[0],room_a_tag.find(class_='from-date').text.split('\n')[2]
		room_from_date = datetime.strptime(from_date_str,'%d.%m.%Y')
		room_until_date = None
		room_create_date = datetime.strptime(room_a_tag.find(class_='create-date').contents[0].text,'%d.%m.%Y')
		if(until_date_str[0].isalpha()):
			room_until_date = None
		else:
			room_until_date = datetime.strptime(until_date_str,'%d.%m.%Y')
		return RoomEntity(room_url,room_id,room_price,room_location,room_create_date,room_from_date,room_until_date)
