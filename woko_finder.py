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

def woko_refresh():
	print(f"\nRefreshing results on Woko website:::{datetime.now()}\n")
	woko_url = 'http://www.woko.ch/'
	response = requests.get(woko_url + 'en/zimmer-in-zuerich')
	soup = BeautifulSoup(response.text,features='html.parser')
	entries = soup.find_all('div',class_='inserat')
	if len(entries) == 0:
		print("No room on woko website now")
		return
	detailed_urls = []
	visited_woko = []
	if os.path.isfile("visited_woko_url.txt"):
		with open("visited_woko_url.txt",'r') as f:
			for line in f:
				visited_woko.append(int(line))
	print_info(f"\n\nvisited_woko length is {len(visited_woko)}\n\n")
	for woko in visited_woko:
			print_info(woko)
	for entry in entries:
		room_url = entry.find('a')['href'].split('/')[-1]
		print_info(f"New room url is {room_url}")
		visited = False
		for woko in visited_woko:
			print_info(f"woko:{woko}")
			print_info(f"room_url:{room_url}")
			print_info(woko == room_url)
			if int(woko) == int(room_url):
				print_info("Found visited woko")
				visited = True
		if not visited:
			detailed_urls.append(room_url)

	if len(detailed_urls) == 0:
		print("\nNo changed detected at woko website:::::\n")
		return

	with open("visited_woko_url.txt",'a+') as f:
		for url in detailed_urls:
			f.write(f"{url}\n")

	print_info(f"\n\nThe length of the detailed_urls is{len(detailed_urls)}\n\n")
	for room_url in detailed_urls:
		full_url = woko_url + "/en/zimmer-in-zuerich-details/"+room_url
		response = requests.get(full_url)
		soup = BeautifulSoup(response.text,features='html.parser')
		div = soup.find('div',class_='inserat-details')
		rent_type = div.contents[1].contents[1].contents[1].text
		renter_email = div.contents[3].contents[5].text
		msg = "There has been new room posted on the woko website with the following information:" + rent_type + renter_email
		notify_through_email("New room on the woko website",msg)
