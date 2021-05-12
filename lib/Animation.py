"""
animation class
parameter: name:str step:dict data:any
"""
class Animation:
	def __init__(self, name, step, data):
		self.name = name
		self.step = step
		self.data = data
