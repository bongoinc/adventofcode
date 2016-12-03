class LampMatrix:
	def __init__(self, width, height):
		self.__width = width
		self.__height = height
		self.__matrix = []

		for x in range(0,self.__width):
			row = []
			for y in range(0,self.__height):
				row.append(0)

			self.__matrix.append(row)

	def __set_brightness(self, from_x, from_y, to_x, to_y, diff):
		for x in range(from_x,to_x+1):
			row = self.__matrix[x]
			for y in range(from_y,to_y+1):
				row[y] += diff
				if row[y] < 0:
					row[y] = 0

	def brighten(self, from_x, from_y, to_x, to_y):
		self.__set_brightness(from_x, from_y, to_x, to_y, 1)

	def darken(self, from_x, from_y, to_x, to_y):
		self.__set_brightness(from_x, from_y, to_x, to_y, -1)

	def super_brighten(self, from_x, from_y, to_x, to_y):
		self.__set_brightness(from_x, from_y, to_x, to_y, 2)

	def brightness(self):
		total_brightness = 0
		for x in range(0,self.__width):
			row = self.__matrix[x]
			for y in range(0, self.__height):
				total_brightness += row[y]

		return total_brightness

	def __set_lamp_state(self, from_x, from_y, to_x, to_y, lamp_state):
		for x in range(from_x,to_x+1):
			row = self.__matrix[x]
			for y in range(from_y,to_y+1):
				row[y] = lamp_state

	def turn_on(self, from_x, from_y, to_x, to_y):
		self.__set_lamp_state(from_x, from_y, to_x, to_y, 1)

	def turn_off(self, from_x, from_y, to_x, to_y):
		self.__set_lamp_state(from_x, from_y, to_x, to_y, 0)

	def toggle(self, from_x, from_y, to_x, to_y):
		for x in range(from_x,to_x+1):
			row = self.__matrix[x]
			for y in range(from_y,to_y+1):
				if row[y] == 0:
					row[y] = 1
				else:
					row[y] = 0

	def lit(self):
		lit_lamps = 0
		for x in range(0,self.__width):
			lit_lamps += self.__matrix[x].count(1)

		return lit_lamps
    