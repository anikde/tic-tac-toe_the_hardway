class agent:
	def __init__(self, name, value, moves):
		self.name = name
		self.moves = moves
		self.value = value

	def agent_instance(self):
		return [self.name, self.value, self.moves]

