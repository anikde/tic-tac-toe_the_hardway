#!/usr/bin/env python3

import random
class Agent:
	def __init__(self, name, value):
		self.name = name
		self.value = value

	def move(self, gamestate):
		self.gamestate = gamestate
		vacant_pos =[]
		if(self.gamestate == [0]*9): return random.randint(0, 8)
		for x in range(len(self.gamestate)):
			if (self.gamestate[x] == 0): (vacant_pos).append(x)
		return random.choice(vacant_pos)

