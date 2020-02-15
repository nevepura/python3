import requests
import time
from time import strftime
import datetime
import argparse


def get_status(URL):
	return requests.get(URL).status_code


def main():
	# defaults
	URL = 'https://imgur.com/'
	WAIT = 10

	# parse cmd line input
	parser = argparse.ArgumentParser(description='Control the status of a website.')
	parser.add_argument('-l', '--link', action='store' , nargs=1, help='The URL to check.')
	parser.add_argument('-t', '--time', action='store', nargs=1, help='How often check occurs.')
	args = parser.parse_args()

	# init vars if arguments exits
	if args.link is not None:
		URL = args.link[0]
	if args.time is not None:
		WAIT = int(args.time[0])

	prev_status = get_status(URL)
	cont = True

	print("Checking state of: " + URL)
	while True and cont == True:
		status = get_status(URL)
		print(str(strftime("%H:%M:%S")) + " - current status: " +  str(status))

		if status != prev_status:
			print("Status has changed!")
			break
		else:
			time.sleep(WAIT)


if __name__ == "__main__":
	main()