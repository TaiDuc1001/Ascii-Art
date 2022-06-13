import colorama
from colorama import Fore, Style, init
from colorama import init as colorama_init
import time
import sys
from termcolor import cprint 
from pyfiglet import figlet_format

colorama.init()
def name1():
	print('\033[32m' + "Alright, here's your album ... ")
	print('\033[33m' + 'Loading... 10%')
	time.sleep(0.2)
	print('Loading... 20%')
	time.sleep(0.2)
	print('Loading... 30%')
	time.sleep(0.2)
	print('Loading... 40%')
	time.sleep(0.2)
	print('Loading... 50%')
	time.sleep(0.2)
	print('Loading... 60%')
	time.sleep(0.2)
	print('Loading... 70%')
	time.sleep(0.2)
	print('Loading... 80%')
	time.sleep(0.2)
	print('Loading... 90%')
	time.sleep(0.2)
	print('Loading... 100%' + Style.RESET_ALL)
	time.sleep(0.2)
	with open("ascii_art.txt") as f:
		content = f.read()
		for line in content.splitlines():
			print(line)
			time.sleep(0.05)
	time.sleep(3)
# ====================================================
	init(strip=not sys.stdout.isatty())
	cprint(figlet_format('Duc Phan', font='doh'),'green')
# ====================================================

	with open("ascii_art1.txt") as f:
		content = f.read()
		for line in content.splitlines():
			print(line)
			time.sleep(0.03)

name = input("Enter your Robotics's Leader's name: ")
if name == 'ton'or name == 'tay gôn':
	name = False
	name1()
else:
	name = True
while name:
	name = input("Type again: ")
	if name == 'ton'or name == 'tay gôn':
		name1()
		break
	else:
		name = True
