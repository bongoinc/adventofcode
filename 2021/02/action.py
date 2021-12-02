import re

class Action:
    REGEX_OPERAND = r"^(forward|down|up) ([0-9]{1})$"
    def __init__(self, str):
        self.__do = ""
        self.__steps = 0
        self.decode(str)

    def get_do(self):
      return self.__do

    def get_steps(self):
      return self.__steps

    def decode(self, str):
        m = re.findall(self.REGEX_OPERAND, str)
        if m:
          a, s = m[0]
          self.__do = a
          self.__steps = int(s)

    def __repr__(self):
      return 'DO: {}, STEPS: {}'.format(self.__do, self.__steps)