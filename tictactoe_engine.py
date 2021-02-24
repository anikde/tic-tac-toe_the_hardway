#!/usr/bin/env python3
from enum import Enum, unique

@unique
class engineReturnCode(Enum):
	SUCCESS = 1
	FAILURE = 2
	WIN = 3
	RUNNING = 4
	TIE = 5	
	VALID = 6

class tictactoeEngine:
	def __init__(self, agent1, agent2):
		self.agent1 = agent1
		self.agent2 = agent2
		self.gamestate = [0] * 9
		self.state_list= []

	
	def startEngine(self):
		if (self.gamestate == [0] * 9):
			if (self.checkWin() == engineReturnCode.RUNNING):
				for x in range(0,9):
					if(x%2 == 0 and (self.checkTie() != engineReturnCode.TIE) and (self.checkWin()== engineReturnCode.RUNNING) ):
						a = self.agent1.move(self.gamestate)
						while(self.checkvalid(a) != engineReturnCode.SUCCESS):
							a = self.agent1.move(self.gamestate)
						self.gamestate[a] = self.agent1.value
					elif(x%2==1 and (self.checkTie() != engineReturnCode.TIE) and (self.checkWin()== engineReturnCode.RUNNING) ):
						b = self.agent2.move(self.gamestate)
						while(self.checkvalid(b) != engineReturnCode.SUCCESS):
							b = (self.agent2).move(self.gamestate)
						self.gamestate[b] = self.agent2.value

					self.get_gameState()
					if (engineReturnCode.TIE == self.checkTie()): 
						return engineReturnCode.TIE, 0, 0
						 
					if (self.checkWin()== engineReturnCode.WIN and (self.checkTie() != engineReturnCode.TIE) ):
						if (x%2==0): 
							return engineReturnCode.SUCCESS , self.get_gameState(), self.agent1.value  
						else:
							return engineReturnCode.SUCCESS, self.get_gameState(), self.agent2.value

	def get_gameState(self): 
		self.state_list.append(list(self.gamestate))
		return self.state_list
		

	def checkWin(self):
		if(self.gamestate != [0]*9):
			if (self.gamestate[0]== self.gamestate[4] ==  self.gamestate[8] != 0 ):
				return engineReturnCode.WIN
			elif(self.gamestate[0]== self.gamestate[3] ==  self.gamestate[6] != 0):
				return engineReturnCode.WIN
			elif(self.gamestate[0]== self.gamestate[1] ==  self.gamestate[2] != 0):
				return engineReturnCode.WIN
			elif(self.gamestate[2]== self.gamestate[5] ==  self.gamestate[8] != 0):
				return engineReturnCode.WIN
			elif(self.gamestate[2]== self.gamestate[4] ==  self.gamestate[6] != 0):
				return engineReturnCode.WIN
			elif(self.gamestate[6]== self.gamestate[7] ==  self.gamestate[8] != 0):
				return engineReturnCode.WIN
			elif(self.gamestate[3]== self.gamestate[4] ==  self.gamestate[5] != 0):
				return engineReturnCode.WIN
			elif(self.gamestate[1]== self.gamestate[4] ==  self.gamestate[7] != 0):
				return engineReturnCode.WIN
			else: return engineReturnCode.RUNNING
		else: return engineReturnCode.RUNNING
	

	def checkTie(self):
		count = 0 
		for p in self.gamestate:
			if (p != 0):
				count +=1 
		if (count==9): return engineReturnCode.TIE
		return engineReturnCode.RUNNING


	def checkvalid(self, a):
		self.a = a
		if (self.gamestate[self.a] != 0):
			return engineReturnCode.FAILURE
		else: 
			return engineReturnCode.SUCCESS
