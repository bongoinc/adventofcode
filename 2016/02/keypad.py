class KeyPad:
	def __init__(self):
		self.__current_key = 5

	def parse_instructions(self, instructions):
		for c in instructions:
			if c == 'U' and self.__current_key - 3 > 0:
				self.__current_key -= 3
			elif c == 'D' and self.__current_key + 3 < 10:
				self.__current_key += 3
			elif c == 'L' and self.__current_key not in (1, 4, 7):
				self.__current_key -= 1
			elif c == 'R' and self.__current_key not in (3, 6, 9):
				self.__current_key += 1

		return str(self.__current_key)