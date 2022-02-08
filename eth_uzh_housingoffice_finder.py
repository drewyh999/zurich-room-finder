from bs4 import BeautifulSoup,Tag
import requests
import json 
import sys
from datetime import datetime
import re
import time
import yagmail
import os.path

from config import ETH_HEADERS
from config import SENDER_EMAIL_ACCOUNT
from config import FREQUENCY
from config import RECEIVER_EMAIL
from room_entity import ETHHousingWebsiteRoomEntity
from utils import print_info
from utils import notify_through_email



def get_new_room_list():
	eth_url = "https://wohnen.ethz.ch/index.php?act=listfoundoffer&pid=1&what=9&sort=1"
	print_info(f"Sending request to eth-uzh housing office site {eth_url} with cookie\n{ETH_HEADERS}")
	response = requests.get(eth_url,headers=ETH_HEADERS)
	print_info("\nResponse received::::\n")
	soup = BeautifulSoup(response.text, features = "html.parser")
	if soup.find(class_='listing') is None:
		print("Eth-uzh housing website cookie needs to be updated",file=sys.stderr)
		exit(1)
	room_list = soup.find(class_='listing').find_all("tr")[1::2]
	if len(room_list) == 0:
		print("No room ads posted on the eth-uzh housing website")
		return
	room_entities = []
	for entry in room_list:
		room_entities.append(ETHHousingWebsiteRoomEntity.parse_from_html(entry))
	new_room_list = []
	visited_room_id_list = []
	#Determine if we visited the newly got rooms
	if os.path.isfile('visited_room_id.txt'):
		with open("visited_room_id.txt",'r') as f:
			for line in f:
				visited_room_id_list.append(int(line))
	for entity in room_entities:
		new_room_id = int(entity.id)
		visited = False
		for room_id in visited_room_id_list:
			if new_room_id == room_id:
				visited = True
		if not visited:
			new_room_list.append(entity)

	#Write back the new room list to the visited room id file
	with open("visited_room_id.txt",'a+') as f:
		for entity in new_room_list:
			f.write(f"{entity.id}\n")

	return new_room_list

def eth_uzh_refresh():
	print(f"\nRefreshing results on eth-uzh housing website::::{datetime.now()}\n")
	new_room_list = get_new_room_list()
	for new_room in new_room_list:
		msg = f"New room avaliable on eth-uzh housing website with following information:\n" \
		+ f"Room ads No.:{new_room.id}\nPrice:{new_room.price}\nDistrict:{new_room.district}\n" \
		+ f"Room type:{new_room.room_type}\nRooms:{new_room.rooms}\nFrom date:{new_room.from_date}\n" \
		+ f"Until date:{new_room.until_date}\nFurnished:{new_room.furnished}"
		notify_through_email('Changes happened on the eth-uzh housing website',msg)
	if len(new_room_list) == 0:
		print("\nNo change detected on eth-uzh housing website:::::\n")




