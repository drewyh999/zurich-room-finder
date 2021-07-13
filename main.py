from bs4 import BeautifulSoup,Tag
import requests
import json 
import sys
from datetime import datetime

from config import TENANT_INFO
from config import CITY_NAMES
from config import VERBOSE_MODE
from config import HEADERS
from room_entity import RoomEntity

form_data = {
		"query":"",
		"priceMin":"",
		"priceMax":"",
		"state":"",
		"permanent":"",
		"student":"",
		"orderBy":"@sortDate",
		"orderDir":"descending",
		"startSearchMate":"true",
		"wgStartSearch":"true",
		"start":"0"
}

def print_info(*args, **kwargs):
    if not VERBOSE_MODE:
        return
    print(*args, **kwargs)

def print_welcome():
	print(' ____  _     ____  _  ____  _      \n/_   \/ \ /\/  __\/ \/   _\/ \ /|  \n /   /| | |||  \/|| ||  /  | |_||  \n/   /_| \_/||    /| ||  \_ | | ||  \n\____/\____/\_/\_\\_/\____/\_/ \|  \n                                   \n ____  ____  ____  _               \n/  __\/  _ \/  _ \/ \__/|          \n|  \/|| / \|| / \|| |\/||          \n|    /| \_/|| \_/|| |  ||          \n\_/\_\\____/\____/\_/  \|          \n                                   \n _____ _  _      ____  _____ ____  \n/    // \/ \  /|/  _ \/  __//  __\ \n|  __\| || |\ ||| | \||  \  |  \/| \n| |   | || | \||| |_/||  /_ |    / \n\_/   \_/\_/  \|\____/\____\\_/\_\ ')

	print('Welcome to Zurich room finder! \nThis software is writen by a normal guy in love')

	print("Currently support wgzimmer.ch only")

def get_room_list(l_price,h_price,State,if_student,Permanent):
	url = "https://www.wgzimmer.ch/en/wgzimmer/search/mate.html?"
	form_data["priceMin"] = l_price
	form_data["priceMax"] = h_price
	form_data["state"] = CITY_NAMES[State]
	form_data["permanent"] = Permanent
	form_data["student"] = if_student
	print("Getting room list for lowest price from " + str(l_price) + " to " + str(h_price) + " at " + str(State))
	print_info("\nForm date submited" + str(form_data))
	print_info("\nSending request with post method to" + url + "Headers:" + str(HEADERS))
	response = requests.post(url, form_data,headers = HEADERS)

	print_info("\n Response received::::")
	soup = BeautifulSoup(response.text, features = "html.parser")
	avaliable_rooms_entries = soup.find_all('li',class_="search-mate-entry")
	
	room_entities = []
	for entry in avaliable_rooms_entries:
		room_entities.append(RoomEntity.parse_from_html(entry))
		# room_response = requests.get(room_url)
		# room_soup = BeautifulSoup(room_response.text, features = "html.parser")
	print("\nRoom found:\n")
	for entity in room_entities:
		print(str(entity.id) + " " + str(entity.from_date) + " " + str(entity.until_date))
	


def check_config():
	for value in TENANT_INFO.values():
		if value == "":
			print("Tenant info not filled!")
			exit(1)


def main():
	print_welcome()

	l_price = 0

	h_price = 0

	State = "Zurich (City)"

	if_student = ""

	Permanent = ""

	while True:

		while True:
			l_price  = int(input("Enter you lowest price expected(at least 200 at most 1500):"))
			if l_price in range(200,1501):
				break
			else:
				print("Price not correct")
		while True:
			h_price  = int(input("Enter you highest price expected(at least 200 at most 1500):"))
			if h_price in range(200,1501):
				break
			else:
				print("Price not correct")
		if (l_price <= h_price):
			break
		else:
			print("Price not correct(lowest price must be higher lower than highest price)")
	print("Choose one of the cities from below")
	for it in CITY_NAMES.keys():
		print(it)
	while True:
		State = input("Type the city name above you want to search for a room:")
		if (State in CITY_NAMES.keys()):
			break
		else:
			print("Illegal selection!!")
	while True:
		if_student = input("Decide to search for rooms only for students or not(y/n/all)")
		if if_student == "y":
			if_student = "true"
			break
		elif if_student == "n":
			if_student = "false"
			break
		elif if_student == "all":
			if_student = "none"
			break
		print("Illegal selection!!")
	while True:
		Permanent = input("Search for unlimited rooms?(y/n/all)")
		if Permanent == "y":
			Permanent = "true"
			break
		elif Permanent == "n":
			Permanent = "false"
			break
		elif Permanent == "all":
			Permanent = "none"
			break
		print("Illegal selection!!")

	get_room_list(l_price,h_price,State,if_student,Permanent)


if __name__ == "__main__":
	main()






