from wgzimmer_finder import wgzimmer_main
from eth_uzh_housingoffice_finder import eth_uzh_main

def print_welcome():
	print(' ____  _     ____  _  ____  _      \n/_   \/ \ /\/  __\/ \/   _\/ \ /|  \n /   /| | |||  \/|| ||  /  | |_||  \n/   /_| \_/||    /| ||  \_ | | ||  \n\____/\____/\_/\_\\_/\____/\_/ \|  \n                                   \n ____  ____  ____  _               \n/  __\/  _ \/  _ \/ \__/|          \n|  \/|| / \|| / \|| |\/||          \n|    /| \_/|| \_/|| |  ||          \n\_/\_\\____/\____/\_/  \|          \n                                   \n _____ _  _      ____  _____ ____  \n/    // \/ \  /|/  _ \/  __//  __\ \n|  __\| || |\ ||| | \||  \  |  \/| \n| |   | || | \||| |_/||  /_ |    / \n\_/   \_/\_/  \|\____/\____\\_/\_\ ')

	print('Welcome to Zurich room finder! \nThis software is writen by a normal guy in love')

	print("Currently support wgzimmer.ch and ETH-UZH housing office website only")




def check_config():
	for value in TENANT_INFO.values():
		if value == "":
			print("Tenant info not filled!")
			exit(1)


def main():
	print_welcome()
	#wgzimmer_main()
	eth_uzh_main()

	

if __name__ == "__main__":
	main()






