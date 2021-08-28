from datetime import datetime
from bs4 import Tag

class WgzimmerRoomEntity:
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
class ETHHousingWebsiteRoomEntity:
	def __init__(self,room_id:str, price:str, city:str, district:str,room_type:str,rooms:str,from_date:str,until_date:str,furnished:str,size:str):
		self.id = room_id
		self.price = price
		self.city = city
		self.district = district
		self.room_type = room_type
		self.rooms = rooms
		self.from_date = from_date
		self.until_date = until_date
		self.furnished = furnished

	@staticmethod
	def parse_from_html(entry:Tag):
		room_id = entry.contents[3].text
		room_city = entry.contents[7].text
		room_district = entry.contents[9].text
		room_price = entry.contents[11].text
		room_type = entry.contents[13].text
		room_rooms = entry.contents[15].text
		room_size = entry.contents[17].text
		room_from_date = entry.contents[19].text
		room_until_date = entry.contents[21].text
		room_furnished = entry.contents[23].text
		return ETHHousingWebsiteRoomEntity(room_id,room_price,room_city,room_district,room_type,room_rooms,room_from_date,room_until_date,room_furnished,room_size)

