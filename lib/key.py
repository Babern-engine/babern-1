class Keyboard(object):
	def __init__(self, name:str, key:str, method:function):
		self.name = name
		self.key = key
		self.method = method
