class CameraController:
	def __init__(self, name:str, scene:str, camera_list:list, active_camera:list, inactive_camera:list, method:list):
		self.name = name
		self.scene = scene
		self.camera_list = camera_list
		self.active_camera = active_camera
		self.inactive_camera = inactive_camera
		self.method = method
