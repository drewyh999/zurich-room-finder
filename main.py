from bs4 import BeautifulSoup
import requests
import json 
import sys

from config import TENANT_INFO
from config import CITY_NAMES

print(' ____  _     ____  _  ____  _      \n/_   \/ \ /\/  __\/ \/   _\/ \ /|  \n /   /| | |||  \/|| ||  /  | |_||  \n/   /_| \_/||    /| ||  \_ | | ||  \n\____/\____/\_/\_\\_/\____/\_/ \|  \n                                   \n ____  ____  ____  _               \n/  __\/  _ \/  _ \/ \__/|          \n|  \/|| / \|| / \|| |\/||          \n|    /| \_/|| \_/|| |  ||          \n\_/\_\\____/\____/\_/  \|          \n                                   \n _____ _  _      ____  _____ ____  \n/    // \/ \  /|/  _ \/  __//  __\ \n|  __\| || |\ ||| | \||  \  |  \/| \n| |   | || | \||| |_/||  /_ |    / \n\_/   \_/\_/  \|\____/\____\\_/\_\ ')

print('Welcome to Zurich room finder! \n This software is writen by a normal guy in love')

print("Currently support wgzimmer.ch only")

print("Usage: Save the message that you wish to send to the landlord in a file named msg.txt in the save directory of this executable and select the rest of the functions step by step")

l_price = 0

h_price = 0

State = ""

while True:
	l_price  = input("Enter you lowest price expected(at least 200 at most 1500)")
	if int(l_price) in range(200,1500):
		break
	else:
		print("Price not correct")
for it in CITY_NAMES.values():
	print(it)
