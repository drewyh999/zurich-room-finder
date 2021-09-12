from bs4 import BeautifulSoup,Tag
import requests
import json 
import sys
from datetime import datetime
import re
import time
import yagmail

from config import CITY_NAMES
from config import HEADERS
from config import SENDER_EMAIL_ACCOUNT
from config import FREQUENCY
from config import RECEIVER_EMAIL
from config import WGZIMMER_CONDITIONS

from room_entity import WgzimmerRoomEntity
from utils import print_info

pre_ads_found = -1


def notify_through_email(msg:str):
	yagmail.SMTP(SENDER_EMAIL_ACCOUNT["account"],host=SENDER_EMAIL_ACCOUNT["host"],port=SENDER_EMAIL_ACCOUNT["port"]).send(RECEIVER_EMAIL,'Changes on the wgzimmer website',msg)
	print("Sending email to " + RECEIVER_EMAIL)

def get_total_ads_number(WGZIMMER_CONDITIONS):
	url = "https://www.wgzimmer.ch/en/wgzimmer/search/mate.html?"
	print_info("Getting total ads number for lowest price from " + str(WGZIMMER_CONDITIONS["priceMin"]) + " to " + str(WGZIMMER_CONDITIONS["priceMax"]) + " at " + str(WGZIMMER_CONDITIONS["state"]))
	print_info("\nForm data submited" + str(WGZIMMER_CONDITIONS))
	print_info("\nSending request with post method to" + url + "Headers:" + str(HEADERS))
	response = requests.post(url, WGZIMMER_CONDITIONS,headers = HEADERS)

	print_info("\n Response received::::")
	soup = BeautifulSoup(response.text, features = "html.parser")
	container = soup.find('div',id='container')
	script = container.find('script',text=re.compile('total*'))
	total_ads_found = int(script.contents[0].split('\"')[-2].split(' ')[1])
	return total_ads_found

def wgzimmer_refresh(pre_ads_found):
	print(f"\nRefreshing results on Wgimmer website:::{datetime.now()}\n")
	total_ads_found = get_total_ads_number(WGZIMMER_CONDITIONS)
	msg_change = 'Given the search conditions as below, there has been changes happened on the wgzimmer website\n' \
		+ f'Lowest price from {WGZIMMER_CONDITIONS["priceMin"]} highest price to {WGZIMMER_CONDITIONS["priceMax"]}\n' \
		+ f'Place of the property:{WGZIMMER_CONDITIONS["state"]}\n Search only students:{WGZIMMER_CONDITIONS["student"]}\n' \
		+ f'Search permanent room:{WGZIMMER_CONDITIONS["permanent"]}\nCurrent number of ads:{total_ads_found}'
	if pre_ads_found == -1:
		pre_ads_found = total_ads_found
	elif pre_ads_found - total_ads_found != 0:
		pre_ads_found = total_ads_found
		notify_through_email(msg_change)
	else:
		print("\nNo change detected on wgzimmer website::::\n")
	return pre_ads_found


# def wgzimmer_main():
	

# 	print("Specify the criterions you need on the Wgzimmer below")

# 	while True:

# 		while True:
# 			WGZIMMER_CONDITIONS["priceMin"]  = int(input("Enter you lowest price expected(at least 200 at most 1500):"))
# 			if WGZIMMER_CONDITIONS["priceMin"] in range(200,1501):
# 				break
# 			else:
# 				print("Price not correct")
# 		while True:
# 			WGZIMMER_CONDITIONS["priceMax"]  = int(input("Enter you highest price expected(at least 200 at most 1500):"))
# 			if WGZIMMER_CONDITIONS["priceMax"] in range(200,1501):
# 				break
# 			else:
# 				print("Price not correct")
# 		if (WGZIMMER_CONDITIONS["priceMin"] <= WGZIMMER_CONDITIONS["priceMax"]):
# 			break
# 		else:
# 			print("Price not correct(lowest price must be higher lower than highest price)")
# 	print("Choose one of the cities from below")
# 	for it in CITY_NAMES.keys():
# 		print(it)
# 	while True:
# 		State = input("Type the city name above you want to search for a room:")
# 		if (State in CITY_NAMES.keys()):
# 			break
# 		else:
# 			print("Illegal selection!!")
# 	while True:
# 		WGZIMMER_CONDITIONS["student"] = input("Decide to search for rooms only for students or not(y/n/all)")
# 		if WGZIMMER_CONDITIONS["student"] == "y":
# 			WGZIMMER_CONDITIONS["student"] = "true"
# 			break
# 		elif WGZIMMER_CONDITIONS["student"] == "n":
# 			WGZIMMER_CONDITIONS["student"] = "false"
# 			break
# 		elif WGZIMMER_CONDITIONS["student"] == "all":
# 			WGZIMMER_CONDITIONS["student"] = "none"
# 			break
# 		print("Illegal selection!!")
# 	while True:
# 		Permanent = input("Search for unlimited rooms?(y/n/all)")
# 		if Permanent == "y":
# 			Permanent = "true"
# 			break
# 		elif Permanent == "n":
# 			Permanent = "false"
# 			break
# 		elif Permanent == "all":
# 			Permanent = "none"
# 			break
# 		print("Illegal selection!!")

	#room_entities = get_room_list(WGZIMMER_CONDITIONS["priceMin"],WGZIMMER_CONDITIONS["priceMax"],State,WGZIMMER_CONDITIONS["student"],Permanent)
	
	# while True:
	# 	print(f"\nRefreshing results on Wgimmer website:::{datetime.now()}\n")
	# 	total_ads_found = get_total_ads_number(WGZIMMER_CONDITIONS["priceMin"],WGZIMMER_CONDITIONS["priceMax"],State,WGZIMMER_CONDITIONS["student"],Permanent)
	# 	msg_change = f"Given the search conditions as below, there has been changes happened on the wgzimmer website\nLowest price from {WGZIMMER_CONDITIONS["priceMin"]} highest price to {WGZIMMER_CONDITIONS["priceMax"]}\n Place of the property:{State}\n Search only students:{WGZIMMER_CONDITIONS["student"]}\n Search permanent room:{Permanent}\nCurrent number of ads:{total_ads_found}"
	# 	if pre_ads_found == -1:
	# 		msg_init = f"Started to monitor changes based on the following conditions:\nLowest price from {WGZIMMER_CONDITIONS["priceMin"]} highest price to {WGZIMMER_CONDITIONS["priceMax"]}\n Place of the property:{State}\n Search only students:{WGZIMMER_CONDITIONS["student"]}\n Search permanent room:{Permanent}\n Current number of ads:{total_ads_found}"
	# 		notify_through_email(msg_init)
	# 		pre_ads_found = total_ads_found
	# 	elif pre_ads_found - total_ads_found != 0:
	# 		pre_ads_found = total_ads_found
	# 		notify_through_email(msg_change)
	# 	else:
	# 		print("No change detected")
	# 	#Sleep for a constant time
	# 	time.sleep(3600/FREQUENCY)
	#print(f"\n {total_ads_found} Rooms found:\n")
	#print('{:40}{:25}{:25}'.format('id','From','Until'))
	#for entity in room_entities:
	#	print('{:40}{:25}{:25}'.format(str(entity.id),str(entity.from_date) ,str(entity.until_date)))