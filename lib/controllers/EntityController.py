class EntityController:
	def __init__(self, name:str, scene:str, entity_list:list, active_entity:list, inactive_entity:list, method:list):
		self.name = name
		self.scene = scene
		self.entity_list = entity_list
		self.active_entity = active_entity
		self.inactive_entity = inactive_entity
		self.method = method
