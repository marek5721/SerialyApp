from serialy_database import *
import time
import os


os.system('cls') and os.system('clear') #works with both win and linux
print('Welcome to SeralyApp by Marek! \n\ntype "h" for help')
print()
while True:
	print()
	search=input()
	if search=='help' or search=='h' or search=='H':
		print()
		print(shelp)
	if search=='list' or search=='l' or search=='ls':
		print()
		for item in newlist:
			print(item)
		print()

	if search=='silicon valley' or search=='sil' or search=='Silicon valley':
		print()
		for item in sil_val:
			print(item)
		print()
	if search=='twd' or search=='TWD' or search=='the walking dead':
		print()
		for item in twd:
			print(item)
		print()

	if search=='Office' or search=='office':
		print()
		for item in Office:
			print(item)
		print()
	if search=='Black mirror' or search=='black mirror':
		print()
		for item in black_mirror:
			print(item)
		print()
	if search=='bojack' or search=='Bojack' or search=='Bojack Horseman' or search=='bojack horseman':
		print()
		for item in Bojack:
			print(item)
		print()
	if search=='westworld' or search=='ww':
		print()
		for item in westworld:
			print(item)
		print()
	if search=='game of thrones' or search=='got':
		print()
		for item in got:
			print(item)
		print()
	if search=='breaking bad' or search=='bb':
		print()
		for item in breakingbad:
			print(item)
		print()
		
	
	if len(search)==0:
		os.system('cls') and os.system('clear')
		print()
		print('enter text')
		print()
	if search=='exit':
		exit()
