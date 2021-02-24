#!/usr/bin/env python3

from agent_random import agent
from tictactoe_engine import tictactoeEngine
import json

def game(times):
	
	agent1 = agent("anik", 1)
	agent2 = agent("arka", 5)
	engine = tictactoeEngine(agent1, agent2)
	returnn = engine.startEngine()
	game_dictionary = {
		"times" : times,
		"winner_moves" : returnn[1],
		"winning_agent_value" : returnn[2]
	}
	if (returnn[2] != 0):
		json_file = open("gamelog.json", "a")
		json.dump(game_dictionary, json_file, indent=4)

if __name__ == "__main__" :
	for x in range(11):
		game(x)