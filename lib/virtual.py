class virtual:
	def __init__(self, name, linker, config=None):
		self.name = name
		self.linker = linker
		self.config = config

	def get_object(self):
		return self.object
