#!/usr/bin/env python3

from tictactoe_engine import engineReturnCode
from agent_random import agent
from tictactoe_engine import tictactoeEngine
import json

agent1 = agent("anik", 1)
agent2 = agent("arka", 5)
engine1 = tictactoeEngine()
count = 1
while(engine1.engine_status == engineReturnCode.RUNNING):
	state = engine1.gamestate
	if (count % 2 == 1):
		move = agent1.move(state)
		engine1.updateState(move, agent1.value)
		print("count-->%d, move--->%d "%(count ,move))
		# if(engine1.checkInput == engineReturnCode.INVALID_INPUT):
		# 	move = agent1.move(state)
		# 	returnn = engine1.updateState(move, agent1.value)
	if(count %2 == 0):
		move = agent2.move(state)
		engine1.updateState(move, agent2.value)
		print("count-->%d, move--->%d "%(count ,move))
		# if(engine1.checkInput == engineReturnCode.INVALID_INPUT):
		# 	move = agent2.move(state)
		# 	returnn = engine1.updateState(move, agent2.value)
	count += 1
print(engine1.engine_status)	 
if (engine1.engine_status == engineReturnCode.WIN):
	game_dictionary = {
		#"times" : times,
		"winner_moves" : engine1.list_of_states,
		"winning_agent_value" : engine1.winning_agents_input
	}
	json_file = open("gamelog.json", "a")
	json.dump(game_dictionary, json_file, indent=4)

