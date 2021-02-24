#!/usr/bin/env python3

import random
class agent:
	def __init__(self, name, value):
		self.name = name
		self.value = value

	def move(self, gamestate):
		self.gamestate = gamestate
		list =[]
		if(self.gamestate == [0]*9): return random.randint(0, 8)
		for x in range(len(self.gamestate)):
			if (self.gamestate[x] == 0): (list).append(x)
		random_move = random.choice(list)
		return random_move

