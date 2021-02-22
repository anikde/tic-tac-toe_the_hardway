from agent_class import agent
from tictactoe_engine import tictactoeEngine
import json
from tictactoe_engine import Code


# def test1():
moves1 = [1, 2, 6, 4, 9]
moves2 = [7, 5, 3, 8]
agent1 = agent("anik", moves1, 1)
agent1_ready = agent1.agent_instance()
agent2 = agent("arka", moves2, -1)
agent2_ready = agent2.agent_instance()
engine_input = tictactoeEngine(agent1_ready[0], agent1_ready[1], agent1_ready[2], agent2_ready[0], agent2_ready[1], agent2_ready[2] ) 
returnn = engine_input.startEngine()
if (returnn[0] == Code.SUCCESS):
	with open("gamelog.txt", 'a') as json_file:
		json.dump(returnn[2], json_file, indent="\t")
		json_file.write("\t")
		json.dump(list(returnn[1]), json_file)
		json_file.write("\n")
