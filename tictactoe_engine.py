#!/usr/bin/env python3
from enum import Enum, unique

@unique
class engineReturnCode(Enum):
	WIN = 0
	RUNNING = 1
	TIE = 2
	VALID = 3
	INVALID_INPUT = 4

class tictactoeEngine:

	def __init__(self):
		self.gamestate = [0]*9
		self.list_of_states = []
		self.engine_status = engineReturnCode.RUNNING
		self.winning_agents_input = 0
		self.checkInput = engineReturnCode.VALID



	def updateState(self,move, agentValue):
		self.move = move
		self.checkvalid(move)
		if (self.checkInput == engineReturnCode.VALID):
			self.gamestate[move] = agentValue
			if( self.checkstatus() == engineReturnCode.TIE ):
				self.engine_status = engineReturnCode.TIE
				self.winning_agents_input = -1
			if(self.checkstatus() == engineReturnCode.WIN ): 
				self.engine_status = engineReturnCode.WIN
				self.winning_agents_input = agentValue
			elif( self.checkstatus() == engineReturnCode.RUNNING ):
				self.engine_status =  engineReturnCode.RUNNING
				self.winning_agents_input = 0
		self.get_gameState()

	def checkWin(self):
		if (self.gamestate[0]== self.gamestate[4] ==  self.gamestate[8] != 0 ):return engineReturnCode.WIN
		elif(self.gamestate[0]== self.gamestate[3] ==  self.gamestate[6] != 0):return engineReturnCode.WIN
		elif(self.gamestate[0]== self.gamestate[1] ==  self.gamestate[2] != 0):return engineReturnCode.WIN
		elif(self.gamestate[2]== self.gamestate[5] ==  self.gamestate[8] != 0):return engineReturnCode.WIN
		elif(self.gamestate[2]== self.gamestate[4] ==  self.gamestate[6] != 0):return engineReturnCode.WIN
		elif(self.gamestate[6]== self.gamestate[7] ==  self.gamestate[8] != 0):return engineReturnCode.WIN
		elif(self.gamestate[3]== self.gamestate[4] ==  self.gamestate[5] != 0):return engineReturnCode.WIN
		elif(self.gamestate[1]== self.gamestate[4] ==  self.gamestate[7] != 0):return engineReturnCode.WIN
		else: return engineReturnCode.RUNNING

	def checkTie(self):
		if all (self.gamestate):
			return engineReturnCode.TIE
		else: return engineReturnCode.RUNNING

	def checkstatus(self):
		if( self.checkTie() == engineReturnCode.TIE ): return engineReturnCode.TIE
		if( self.checkWin() == engineReturnCode.WIN ): return engineReturnCode.WIN
		elif( self.checkWin() == engineReturnCode.RUNNING ): return engineReturnCode.RUNNING

	def get_gameState(self):
		self.list_of_states.append(list(self.gamestate))
		return self.list_of_states

	def checkvalid(self, a):
		if (self.gamestate[a] != 0): self.checkInput = engineReturnCode.INVALID_INPUT
		else: self.checkInput = engineReturnCode.VALID
