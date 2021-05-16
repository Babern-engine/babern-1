"""virtual class allow a variable to embed to another variable with virtual value
"""
class virtual:
	virtual = None;
	def __init__(self, name, linker, config=None):
		self.name = name
		self.linker = linker
		self.config = config
		self.virtual = self.linker
