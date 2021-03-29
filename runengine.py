#!/usr/bin/env python3
# writing test using unittest https://realpython.com/python-testing/#writing-your-first-test

from tictactoe_engine import EngineReturnCode
from agent_random import Agent
from tictactoe_engine import TictactoeEngine
import json

agent1 = Agent("anik", 1)
agent2 = Agent("arka", 5)
engine_instance = TictactoeEngine()
count = 1

while(engine_instance.engine_status == EngineReturnCode.RUNNING):
	state = engine_instance.gamestate
	if (count % 2 == 1):
		move = agent1.move(engine_instance.get_available_pos())
		engine_instance.update_state(move, agent1.value)
		print("count-->%d, move--->%d "%(count ,move))
		# if(engine_instance.check_input == EngineReturnCode.INVALID_INPUT):
		# 	move = agent1.move(state)
		# 	returnn = engine_instance.updateState(move, agent1.value)
	if(count %2 == 0):
		move = agent2.move(engine_instance.get_available_pos())
		engine_instance.update_state(move, agent2.value)
		print("count-->%d, move--->%d "%(count ,move))
		# if(engine_instance.check_input == EngineReturnCode.INVALID_INPUT):
		# 	move = agent2.move(state)
		# 	returnn = engine_instance.updateState(move, agent2.value)
	count += 1
print(engine_instance.engine_status)

if (engine_instance.engine_status == EngineReturnCode.WIN):
	game_dictionary = {
		#"times" : times,
		"winner_moves" : engine_instance.list_of_states,
		"winning_agent_value" : engine_instance.winning_agents_input
	}
	json_file = open("gamelog.json", "a")
	json.dump(game_dictionary, json_file, indent=4)
