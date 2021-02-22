from enum import Enum

state_list=[]
class Code(Enum):
	SUCCESS = 1
	FAILURE = 2
	WIN = 3
	RUNNING = 4
	TIE = 5	
	VALID = 6

class tictactoeEngine:
	def __init__(self, agent1, agent1moves, agent1value,  agent2, agent2moves, agent2value):
		self.agent1 = agent1
		self.agent2 = agent2
		self.agent1moves = agent1moves
		self.agent2moves = agent2moves
		self.agent1value = agent1value
		self.agent2value = agent2value
		self.gamestate = [0] * 9
		self.index1 = 0
		self.index2 = 0

	def startEngine(self):
		if (self.gamestate == [0] * 9):
			if (self.checkWin() == Code.RUNNING):
				for x in range(0,9):
					if(x%2 == 0 and (self.checkTie() != Code.TIE) and (self.checkWin()== Code.RUNNING) ):
						a = self.agent1moves[self.index1]
						while(self.checkvalid(a-1) != Code.SUCCESS):
							a = self.agent1moves[self.index1]
						self.index1 +=1
						self.gamestate[a-1] = self.agent1value
					elif(x%2==1 and (self.checkTie() != Code.TIE) and (self.checkWin()== Code.RUNNING) ):
						b = self.agent2moves[self.index2]
						while(self.checkvalid(b-1) != Code.SUCCESS):
							b = self.agent2moves[self.index2]
						self.index2 +=1
						self.gamestate[b-1] = self.agent2value

					self.get_gameState()
					if (Code.TIE == self.checkTie()): 
						return Code.TIE, 0, 0
						 
					if (self.checkWin()== Code.WIN and (self.checkTie() != Code.TIE) ):
						if (x%2==0): 
							return Code.SUCCESS , self.get_gameState(), self.agent1value  
						else:
							return Code.SUCCESS, self.get_gameState(), self.agent2value

	def get_gameState(self): 
		state_list.append(list(self.gamestate))
		return state_list
		

	def checkWin(self):
		if(self.gamestate != [0]*9):
			if (self.gamestate[0]== self.gamestate[4] ==  self.gamestate[8] != 0 ):
				return Code.WIN
			elif(self.gamestate[0]== self.gamestate[3] ==  self.gamestate[6] != 0):
				return Code.WIN
			elif(self.gamestate[0]== self.gamestate[1] ==  self.gamestate[2] != 0):
				return Code.WIN
			elif(self.gamestate[2]== self.gamestate[5] ==  self.gamestate[8] != 0):
				return Code.WIN
			elif(self.gamestate[2]== self.gamestate[4] ==  self.gamestate[6] != 0):
				return Code.WIN
			elif(self.gamestate[6]== self.gamestate[7] ==  self.gamestate[8] != 0):
				return Code.WIN
			elif(self.gamestate[3]== self.gamestate[4] ==  self.gamestate[5] != 0):
				return Code.WIN
			elif(self.gamestate[1]== self.gamestate[4] ==  self.gamestate[7] != 0):
				return Code.WIN
			else: return Code.RUNNING
		else: return Code.RUNNING
	

	def checkTie(self):
		count = 0 
		for p in self.gamestate:
			if (p != 0):
				count +=1 
		if (count==9): return Code.TIE
		return Code.RUNNING


	def checkvalid(self, a):
		if (self.gamestate[a] != 0):
			return Code.FAILURE
		else: 
			return Code.SUCCESS