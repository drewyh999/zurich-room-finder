from bs4 import BeautifulSoup,Tag
import requests
import json 
import sys
from datetime import datetime
import re
import time
import yagmail

from config import CITY_NAMES
from config import ETH_HEADERS
from config import SENDER_EMAIL_ACCOUNT
from config import FREQUENCY
from config import RECEIVER_EMAIL
from room_entity import ETHHousingWebsiteRoomEntity
from utils import print_info


def get_new_room_list():
	eth_url = "https://wohnen.ethz.ch/index.php?act=listfoundoffer&pid=1&what=9&sort=1"
	print_info(f"Sending request to eth-uzh housing office site {eth_url} with cookie\n{ETH_HEADERS}")
	response = requests.get(eth_url,headers=ETH_HEADERS)
	print_info("\n Response received::::")
	soup = BeautifulSoup(response.text, features = "html.parser")
	room_list = soup.find(class_='listing').find_all("tr")[1::2]
	room_entities = []
	for entry in room_list:
		room_entities.append(ETHHousingWebsiteRoomEntity.parse_from_html(entry))
	

def eth_uzh_main():
	new_room_list = get_new_room_list()