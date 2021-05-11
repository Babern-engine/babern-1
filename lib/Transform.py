class Transform(object):
	def __init__(self,x, y, width, height, scale_x, scale_y):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.scale_x = scale_x
		self.scale_y = scale_y

	@property
	def center(self):
		y = self.x + (self.width / 2)
		x = self.y + (self.height / 2)
		return x,y

	def change_position(self, x, y):
		self.x = x or self.x
		self.y = y or self.y

	def change_dimension(self, width, height):
		self.width = width or self.width
		self.height = height or self.height

	def change_dimension(self, sx, sy):
		self.scale_x = sx + self.scale_x
		self.scale_y = sy + self.scale_y

def transformtype(): ...
