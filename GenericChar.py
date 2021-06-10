# File: GenericChar.py

import random
import threading

class Char(object):
	def __init__(self, name, type, health, power, specpower, speed):
		self.name = name
		self.type = type
		self.health = health
		self.power = power
		self.specpower = specpower
		self.speed = speed
		
	# Generating name for creature
	def NameGen(self):
		syl_list = ["en", "el", "kar", "ku", "kun", "das", "du", "fa", "fu", "xi", "xun", "xan"]
		temp_name = ""
		for i in range(3):
			temp_name = temp_name+syl_list[random.randint(0, (len(syl_list) - 1))]
			if temp_name.count("-") < 2:
				temp_name = temp_name+"-"
			self.name = temp_name


# Initialising class
my_char = Char("", "E", 100, 100, 100, 100)
my_char.NameGen()
print(my_char.name)

