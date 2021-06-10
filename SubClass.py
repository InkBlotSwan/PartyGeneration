# File SubClass.py

import random
import pickle
import sys

# Generic class for creatures
class Char(object):
	def __init__(self, name, health, power, specpower, speed):
		self.name = name
		self.health = health
		self.power = power
		self.specpower = specpower
		self.speed = speed

	# Assigning attributes
	def att_rate(self):
		syl_list = ["en", "el", "kar", "ku", "kun", "das", "du", "fa", "fu", "xi", "xun", "xan"]
		temp_name = ""
		for i in range(3):
			temp_name = temp_name+syl_list[random.randint(0, (len(syl_list) - 1))]
			if temp_name.count("-") < 2:
				temp_name = temp_name+"-"
			self.name = temp_name
		if self.type == "Barbarian":
			self.health = 100
			self.power = 70
			self.specpower = 20
			self.speed = 50
		elif self.type == "Elf":
			self.health = 100
			self.power = 30
			self.specpower = 60
			self.speed = 10
		elif self.type == "Wizard":
			self.health = 100
			self.power = 50
			self.specpower = 70
			self.speed = 30
		elif self.type == "Dragon":
			self.health = 100
			self.power = 90
			self.specpower = 40
			self.speed = 50
		elif self.type == "Knight":
			self.health = 100
			self.power = 60
			self.specpower = 10
			self.speed = 60
		else:
			pass

	def print_stat(self):
		if self.type == "Elf":
			print("\n|||This is %s\n|||An %s\n|||Health: %s\n|||Power: %s\n|||Special Attack Power: %s\n|||Speed: %s" % (self.name, self.type, self.health, self.power, self.specpower, self.speed))
		else:
			print("\n|||This is %s\n|||A %s\n|||Health: %s\n|||Power: %s\n|||Special Attack Power: %s\n|||Speed: %s" % (self.name, self.type, self.health, self.power, self.specpower, self.speed))
	
	def change_stat(self):
		self.health = input("New Health equals: ")
		self.power = input("New Power equals: ")
		self.specpower = input("New Special Attack Power equals: ")
		self.speed = input("New Speed equals: ")
			


# Classes for individual creatures
class B(Char):
	type = "Barbarian"
	def __init__(self, name, health, power, specpower, speed):
		self.name = name
		self.health = health
		self.power = power
		self.specpower = specpower
		self.speed = speed

class E(Char):
	type = "Elf"
	def __init__(self, name, health, power, specpower, speed):
		self.name = name
		self.health = health
		self.power = power
		self.specpower = specpower
		self.speed = speed

class W(Char):
	type = "Wizard"
	def __init__(self, name, health, power, specpower, speed):
		self.name = name
		self.health = health
		self.power = power
		self.specpower = specpower
		self.speed = speed

class D(Char):
	type = "Dragon"
	def __init__(self, name, health, power, specpower, speed):
		self.name = name
		self.health = health
		self.power = power
		self.specpower = specpower
		self.speed = speed

class K(Char):
	type = "Knight"
	def __init__(self, name, health, power, specpower, speed):
		self.name = name
		self.health = health
		self.power = power
		self.specpower = specpower
		self.speed = speed

"""
 Menu functions
 -rand_gen randomly generate characters and add to party
 -print_party prints the stats of all party members
"""
type_list = [B, E, W, D, K]
party = []
amou = 10
party_num = 0
def rand_gen():
	for i in range(amou):
		ran_char = type_list[random.randint(0, (len(type_list) - 1))](0,0,0,0,0)
		ran_char.att_rate()
		party.append(ran_char)
def print_party():
	for i in party:
		i.print_stat()
		print("\n")

# Menu loop
print("\n|||Hello, and welcome to the amazing character menu!\n|||To exit the program type, quit, at any menu.\n|||To return to the previous menu type, back, at any menu.")
choice2 = ""
while True:
	if len(party) != 1:
		print("\n|||You have %d members in your party" % (len(party)))
	else:
		print("\n|||You have %d member in your party" % (len(party)))
	print("\nWhat would you like to do?\n1: Generate a full party\n2: View current party\n3: Load or save")
	choice = input("1/2/3 : ")
	# Automatically fill the party
	if choice == "1":
		party = []
		amou = 10
		rand_gen()
	# Viewing Party
	elif choice == "2":
		# Listing current party
		add_rem = ""
		while True:
			party_num = 1
			for i in party:
				print(party_num, i.name, ":", i.type)
				party_num += 1
			add_rem = input("\nWhat would you like to do?\n1: Add member\n2: Remove member\n3: View members stats\n1/2/3 : ")
			# Adding party member
			if add_rem == "1":
				amou = int(input("How many characters should be added? Enter amount: "))
				rand_gen()
			# Removing Party member
			elif add_rem == "2":
				try:
					choice2 = (input("\nWho would you like to remove? Enter their number: "))
					del party[(int(choice2)) - 1]
				except ValueError:
					pass
			# Viewing stats
			elif add_rem == "3":
				choice3 = int(input("Whos stat should be viewed? Enter their number: "))
				choice3 -= 1
				party[choice3].print_stat()
				stat_ch = input("Should these stats be changed?\n1: Yes\n2: No")
				if stat_ch == "1":
					party[choice3].change_stat()
			# Quitting
			elif "quit" in add_rem or "QUIT" in add_rem or "Quit" in add_rem:
				print("Quitting...")
				sys.exit()
			elif "back" in add_rem or "Back" in add_rem or "BACK" in add_rem:
				break
			else:
				print("|||Please enter a valid response")
	# Saving/Loading via pickle
	elif choice == "3":
		choice3 = input("\nWould you like to save your current party or load a previous party?\n1: Save\n2: Load\n1/2 : ")
		if choice3 == "1":
			# Saving
			with open("save.txt", "wb") as fp:
				pickle.dump(party, fp)
		elif choice3 == "2":
			# Loading
			with open("save.txt", "rb") as fp:
				party = pickle.load(fp)
		# Quitting
		elif "quit" in choice3 or "QUIT" in choice3 or "Quit" in choice3:
			print("Quitting...")
			sys.exit()
	# Exit break
	elif "quit" in choice or "QUIT" in choice or "Quit" in choice:
		print("Quitting...")
		sys.exit()
	else:
		print("\nPlease enter a valid response")