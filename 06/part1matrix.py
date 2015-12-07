class Part1Matrix:
	def __init__(self, width, height):
		self.__width = width
		self.__height = height
		self.__matrix = []

		for x in range(0,self.__width):
			row = []
			for y in range(0,self.__height):
				row.append(False)

			self.__matrix.append(row)

	def __set_lamp_state(self, from_x, from_y, to_x, to_y, lamp_state):
		for x in range(from_x,to_x+1):
			row = self.__matrix[x]
			for y in range(from_y,to_y+1):
				row[y] = lamp_state

	def turn_on(self, from_x, from_y, to_x, to_y):
		self.__set_lamp_state(from_x, from_y, to_x, to_y, True)

	def turn_off(self, from_x, from_y, to_x, to_y):
		self.__set_lamp_state(from_x, from_y, to_x, to_y, False)

	def toggle(self, from_x, from_y, to_x, to_y):
		for x in range(from_x,to_x+1):
			row = self.__matrix[x]
			for y in range(from_y,to_y+1):
				row[y] = not row[y]

	def lit(self):
		lit_lamps = 0
		for x in range(0,self.__width):
			lit_lamps += self.__matrix[x].count(True)

		return lit_lamps
    
	def printM(self):
		print("---------------------------")
		for x in range(0, self.__width):
			row = self.__matrix[x]
			out = ""
			for y in range(0, self.__height):
				if row[y] == True:
					out += "1"
				else:
					out += "0"
             
			print(out)
		print("---------------------------")

