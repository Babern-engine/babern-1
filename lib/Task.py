class task:
	def __init__(self, name:str, task:list, current_task:list, completed_task:list, ignored_task:list):
		self.name = name
		self.task = task
		self.current_task = current_task
		self.completed_task = completed_task
		self.ignored_task = ignored_task

	def complete(self, task_list, index):
		del task_list[index]

	def empty(self, emptied_list):
		if emptied_list == "self.current_task": self.completed_task = [];return
		if emptied_list == "self.completed_task": self.completed_task = [];return
		if emptied_list == "self.ignored_task": self.completed_task = [];return
		return "invalid task list type"

