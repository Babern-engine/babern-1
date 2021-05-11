from typing import List, OrderedDict

class Vector2D:
	def __init__(self, name, width, height, parent, child, types:str, data:dict, method:List):
		self.name = name
		self.width = width
		self.height = height
		self.parent = parent
		self.child = child
		self.types = types
		self.data = data
		self.method = method
