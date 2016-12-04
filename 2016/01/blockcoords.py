class BlockCoords:
	def __init__(self):
		self.__posx = 0
		self.__posy = 0
		self.__direction = 'N'
		self.__foundclosest = False
		self.__coords = []
		self.__closestcoordx = 0
		self.__closestcoordy = 0
		self.__coords.append("%d,%d" % (self.__posx, self.__posy))

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
		startx = self.__posx
		starty = self.__posy
		if self.__direction == 'N':
			self.__posy += blocks
		elif self.__direction == 'W':
			self.__posx -= blocks
		elif self.__direction == 'S':
			self.__posy -= blocks
		elif self.__direction == 'E':
			self.__posx += blocks

#		print(self.__coords)

		if self.__foundclosest == False:
			self.__check_path(startx, starty, blocks)

	def __check_path(self, startx, starty, blocks):
		posx = startx
		posy = starty
		for i in range(blocks):
			if self.__direction == 'N':
				posy += 1
			elif self.__direction == 'W':
				posx -= 1
			elif self.__direction == 'S':
				posy -= 1
			elif self.__direction == 'E':
				posx += 1

			new_coord = "%d,%d" % (posx, posy)
			if self.__coords.count(new_coord) > 0:
#				print("Found a matching coord at %s!" % new_coord)
				self.__closestcoordx = posx
				self.__closestcoordy = posy
				self.__foundclosest = True
				return
			else:
				self.__coords.append(new_coord)


	def block_x(self):
		return self.__posx

	def block_y(self):
		return self.__posy

	def get_blocks(self):
		return abs(self.__posx) + abs(self.__posy)

	def block_closest_x(self):
		return self.__closestcoordx

	def block_closest_y(self):
		return self.__closestcoordy

	def get_closest_blocks(self):
		return abs(self.__closestcoordx) + abs(self.__closestcoordy)
