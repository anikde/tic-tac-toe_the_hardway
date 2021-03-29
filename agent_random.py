#!/usr/bin/env python3

import random
class Agent:
	def __init__(self, name, value):
		self.name = name
		self.value = value

	def move(self, available_pos):
		""" Returns a random choice from the available moves of the board
		"""
		return random.choice(available_pos)
