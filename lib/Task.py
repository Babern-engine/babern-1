class task:
	def __init__(self, name:str, task:list, current_task:list, completed_task:list, ignored_task:list):
		self.name = name
		self.task = task
		self.current_task = current_task
		self.completed_task = completed_task
		self.ignored_task = ignored_task

	def get_task(self):
		return self.task

	def get_current_task(self):
		return self.current_task

	def get_completed_task(self):
		return self.completed_task

	def get_ignored_task(self):
		return self.ignored_task
