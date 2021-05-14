from lib.babern import base

class Entity(base):
	def __init__(self, name, parent, child, shape, types):
		super().__init__(name, parent=parent, child=child)
		self.shape = shape
		self.types = types
