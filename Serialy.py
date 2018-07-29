from serialy_database import *
import time
import os


print('Welcome to SeralyApp by Marek! \n\ntype "h" for help')
print()
intro=input()
if intro=='help' or intro=='h':
	print()
	print(shelp)
else:
	if intro=='list' or intro=='l':
		print()
		for item in newlist:
			print(item)
		print()

	if intro=='search' or intro=='s':
		os.system('clear')
		search=input()

		if search=='silicon valley' or search=='sil' or search=='Silicon valley':
			print()
			for item in sil_val:
				print(item)
			print()
			time.sleep(3)
			exit()
		if search=='twd' or search=='TWD' or search=='the walking dead':
			print()
			for item in twd:
				print(item)
			print()
			time.sleep(3)
			exit()
		if search=='Office' or search=='office':
			print()
			for item in Office:
				print(item)
			print()
			exit()
		if search=='Bojack' or search=='bojack':
			print()
			for item in Bojack:
				print(item)
			print()
			time.sleep(3)
			exit()
		if search=='Black mirror' or search=='black mirror' or search=='bm':
			print()
			for item in black_mirror:
				print(item)
			print()
			exit()


		else:
			print()
			print('error')
			print('invalid input')
			print()
			exit()
