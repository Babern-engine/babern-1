class Keyboard(object):
	def __init__(self, name:str, key:str, method:function):
		self.name = name
		self.key = key
		self.method = method

	def get_name(self):
		return self.name

	def get_key(self):
		return self.key

	def get_method(self):
		return self.method
