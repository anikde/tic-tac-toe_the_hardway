#!/usr/bin/env python3

from enum import Enum, unique
@unique
class EngineReturnCode(Enum):
	WIN = 0
	RUNNING = 1
	TIE = 2
	VALID = 3
	INVALID_INPUT = 4

class TictactoeEngine:

	def __init__(self):
		self.gamestate = [0]*9
		self.list_of_states = []
		self.engine_status = EngineReturnCode.RUNNING
		self.winning_agents_input = 0
		self.check_input = EngineReturnCode.VALID

	def update_state(self,agents_move, agent_value):
		""" updates the state of the board with inputs from the player. Heart of the game.

			Parameters
			----------
			agents_move : agent's move ( numerical value from the set [0, 8] ).
						The choice of agent's move can be found from available states returned by the function get_available_pos().
			
			agent_value : The symbol associated with the agent which is making the move.

		
		"""
		self.agents_move = agents_move
		self.check_player_input_valid(agents_move)
		if (self.check_input == EngineReturnCode.VALID):
			self.gamestate[agents_move] = agent_value
			if( self.check_status() == EngineReturnCode.TIE ):
				self.engine_status = EngineReturnCode.TIE
				self.winning_agents_input = -1
			if(self.check_status() == EngineReturnCode.WIN ): 
				self.engine_status = EngineReturnCode.WIN
				self.winning_agents_input = agent_value
			elif( self.check_status() == EngineReturnCode.RUNNING ):
				self.engine_status =  EngineReturnCode.RUNNING
				self.winning_agents_input = 0
		self.get_gamestate()

	def check_win(self):
		"""
			Winning rules defined
		"""
		if (self.gamestate[0]== self.gamestate[4] ==  self.gamestate[8] != 0 ):return EngineReturnCode.WIN
		elif(self.gamestate[0]== self.gamestate[3] ==  self.gamestate[6] != 0):return EngineReturnCode.WIN
		elif(self.gamestate[0]== self.gamestate[1] ==  self.gamestate[2] != 0):return EngineReturnCode.WIN
		elif(self.gamestate[2]== self.gamestate[5] ==  self.gamestate[8] != 0):return EngineReturnCode.WIN
		elif(self.gamestate[2]== self.gamestate[4] ==  self.gamestate[6] != 0):return EngineReturnCode.WIN
		elif(self.gamestate[6]== self.gamestate[7] ==  self.gamestate[8] != 0):return EngineReturnCode.WIN
		elif(self.gamestate[3]== self.gamestate[4] ==  self.gamestate[5] != 0):return EngineReturnCode.WIN
		elif(self.gamestate[1]== self.gamestate[4] ==  self.gamestate[7] != 0):return EngineReturnCode.WIN
		return EngineReturnCode.RUNNING

	def check_tie(self):
		if all (self.gamestate):
			return EngineReturnCode.TIE
		return EngineReturnCode.RUNNING

	def check_status(self):
		if( self.check_tie() == EngineReturnCode.TIE ): return EngineReturnCode.TIE
		return self.check_win()

	def get_gamestate(self):
		self.list_of_states.append(list(self.gamestate))
		return self.list_of_states

	def check_player_input_valid(self, players_move):
		if (self.gamestate[players_move] != 0): self.check_input = EngineReturnCode.INVALID_INPUT
		else: self.check_input = EngineReturnCode.VALID

	def get_available_pos(self):
		""" The function returns the available moves to be made by looking at the current gamestate.
		"""
		self.vacant_pos =[]
		for x in range(len(self.gamestate)):
			if (self.gamestate[x] == 0): (self.vacant_pos).append(x)
		return self.vacant_pos
