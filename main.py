from wgzimmer_finder import wgzimmer_refresh
from eth_uzh_housingoffice_finder import eth_uzh_refresh
from woko_finder import woko_refresh
import time
from config import FREQUENCY
from config import ETH_HEADERS
from config import WGZIMMER_HEADERS

def print_welcome():
	print(' ____  _     ____  _  ____  _      \n/_   \/ \ /\/  __\/ \/   _\/ \ /|  \n /   /| | |||  \/|| ||  /  | |_||  \n/   /_| \_/||    /| ||  \_ | | ||  \n\____/\____/\_/\_\\_/\____/\_/ \|  \n                                   \n ____  ____  ____  _               \n/  __\/  _ \/  _ \/ \__/|          \n|  \/|| / \|| / \|| |\/||          \n|    /| \_/|| \_/|| |  ||          \n\_/\_\\____/\____/\_/  \|          \n                                   \n _____ _  _      ____  _____ ____  \n/    // \/ \  /|/  _ \/  __//  __\ \n|  __\| || |\ ||| | \||  \  |  \/| \n| |   | || | \||| |_/||  /_ |    / \n\_/   \_/\_/  \|\____/\____\\_/\_\ ')

	print('Welcome to Zurich room finder! \nThis software is writen by a normal guy in love')

	print("Currently support wgzimmer.ch and ETH-UZH housing office website only")


def check_config():
	for value in ETH_HEADERS.values():
		if value == "":
			print("Eth-uzh housing website cookie not set!")
			exit(1)
	for value in WGZIMMER_HEADERS.values():
		if value == "":
			print("Wgzimmer website cookie not set!")
			exit(1)


def main():
	print_welcome()
	pre_ads_found = -1
	while True:
		pre_ads_found = wgzimmer_refresh(pre_ads_found)
		eth_uzh_refresh()
		woko_refresh()
		time.sleep(3600/FREQUENCY)


if __name__ == "__main__":
	main()






