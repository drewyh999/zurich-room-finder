from bs4 import BeautifulSoup,Tag
import requests
import json 
import sys
from datetime import datetime
import re
import time
import yagmail


from config import CITY_NAMES
from config import VERBOSE_MODE
from config import HEADERS
from config import SENDER_EMAIL_ACCOUNT
from config import FREQUENCY
from config import RECEIVER_EMAIL
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
		print_info("Parsing html file to room entity")
		room_entities.append(RoomEntity.parse_from_html(entry))
	return room_entities

def get_total_ads_number(l_price,h_price,State,if_student,Permanent):
	url = "https://www.wgzimmer.ch/en/wgzimmer/search/mate.html?"
	form_data["priceMin"] = l_price
	form_data["priceMax"] = h_price
	form_data["state"] = CITY_NAMES[State]
	form_data["permanent"] = Permanent
	form_data["student"] = if_student
	print("Getting total ads number for lowest price from " + str(l_price) + " to " + str(h_price) + " at " + str(State))
	print_info("\nForm data submited" + str(form_data))
	print_info("\nSending request with post method to" + url + "Headers:" + str(HEADERS))
	response = requests.post(url, form_data,headers = HEADERS)

	print_info("\n Response received::::")
	soup = BeautifulSoup(response.text, features = "html.parser")
	container = soup.find('div',id='container')
	script = container.find('script',text=re.compile('total*'))
	total_ads_found = int(script.contents[0].split('\"')[-2].split(' ')[1])
	return total_ads_found


def check_config():
	for value in TENANT_INFO.values():
		if value == "":
			print("Tenant info not filled!")
			exit(1)
def notify_through_email(msg:str):
	yagmail.SMTP(SENDER_EMAIL_ACCOUNT["account"],host=SENDER_EMAIL_ACCOUNT["host"],port=SENDER_EMAIL_ACCOUNT["port"]).send(RECEIVER_EMAIL,'Changes on the wgzimmer website',msg)
	print_info("Sending email to " + RECEIVER_EMAIL)

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

	#room_entities = get_room_list(l_price,h_price,State,if_student,Permanent)
	pre_ads_found = -1
	msg_change = f"Given the search conditions as below, there has been changes happened on the wgzimmer website\nLowest price from {l_price} highest price to {h_price}\n Place of the property:{State}\n Search only students:{if_student}\n Search permanent room:{Permanent}"
	while True:
		print(f"\n\nRefreshing results::::::::::{datetime.now()}")
		total_ads_found = get_total_ads_number(l_price,h_price,State,if_student,Permanent)
		if pre_ads_found == -1:
			msg_init = f"Started to monitor changes based on the following conditions:\nLowest price from {l_price} highest price to {h_price}\n Place of the property:{State}\n Search only students:{if_student}\n Search permanent room:{Permanent}\n Current number of ads:{total_ads_found}"
			notify_through_email(msg_init)
			pre_ads_found = total_ads_found
		elif pre_ads_found - total_ads_found != 0:
			notify_through_email(msg_change)
		else:
			print("No change detected")
		#Sleep for a constant time
		time.sleep(3600/FREQUENCY)
	#print(f"\n {total_ads_found} Rooms found:\n")
	#print('{:40}{:25}{:25}'.format('id','From','Until'))
	#for entity in room_entities:
	#	print('{:40}{:25}{:25}'.format(str(entity.id),str(entity.from_date) ,str(entity.until_date)))

if __name__ == "__main__":
	main()






