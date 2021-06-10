#File: NameGen.py

import random

#Varibles
name = ""
syl_list = ["en", "el", "kar", "ku", "kun", "das", "du", "fa", "fu", "xi", "xun", "xan"]

for i in range(3):
	name = name+syl_list[random.randint(0, (len(syl_list) - 1))]
	if name.count("-") < 2:
		name = name+"-"
print (name)