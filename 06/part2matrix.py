class Part2Matrix:
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

	def turn_on(self, from_x, from_y, to_x, to_y):
		self.__set_brightness(from_x, from_y, to_x, to_y, 1)

	def turn_off(self, from_x, from_y, to_x, to_y):
		self.__set_brightness(from_x, from_y, to_x, to_y, -1)

	def toggle(self, from_x, from_y, to_x, to_y):
		self.__set_brightness(from_x, from_y, to_x, to_y, 2)

	def sum(self):
		total_brightness = 0
		for x in range(0,self.__width):
			row = self.__matrix[x]
			for y in range(0, self.__height):
				total_brightness += row[y]

		return total_brightness
    