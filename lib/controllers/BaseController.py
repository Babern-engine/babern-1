class BaseController:
	def __init__(self, name:str, controller_list:list, data:dict, method:list):
		self.name = name
		self.controller_list = controller_list
		self.data = data
		self.method = method
