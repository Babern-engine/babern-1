class Entity():
	def __init__(self, name, shape, types, parent, child):
		self.name = name
		self.shape = shape
		self.types = types
		self.parent = parent
		self.child = child

	def get_name(self):
		return self.name

	def get_shape(self):
		return self.shape

	def get_type(self):
		return self.type

	def get_parent(self):
		return self.parent

	def get_child(self):
		return self.child
