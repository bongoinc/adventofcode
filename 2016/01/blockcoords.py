class BlockCoords:
	def __init__(self):
		self.__posx = 0
		self.__posy = 0
		self.__direction = 'N'

	def set_direction(self, dir):
		if dir == "R":
			if self.__direction == 'N':
				self.__direction = 'E'
			elif self.__direction == 'E':
				self.__direction = 'S'
			elif self.__direction == 'S':
				self.__direction = 'W'
			elif self.__direction == 'W':
				self.__direction = 'N'
		elif dir == 'L':
			if self.__direction == 'N':
				self.__direction = 'W'
			elif self.__direction == 'W':
				self.__direction = 'S'
			elif self.__direction == 'S':
				self.__direction = 'E'
			elif self.__direction == 'E':
				self.__direction = 'N'

	def move_blocks(self, blocks):
		if self.__direction == 'N':
			self.__posy += blocks
		elif self.__direction == 'W':
			self.__posx -= blocks
		elif self.__direction == 'S':
			self.__posy -= blocks
		elif self.__direction == 'E':
			self.__posx += blocks

	def block_x(self):
		return self.__posx

	def block_y(self):
		return self.__posy

	def get_blocks(self):
		return abs(self.__posx) + abs(self.__posy)
