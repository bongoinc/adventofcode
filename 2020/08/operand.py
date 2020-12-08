import re

class Operand:
    REGEX_OPERAND = r"^(nop|acc|jmp) (\+|-)([0-9]{1,3})$"
    def __init__(self):
        self.__action = ""
        self.__steps = 0

    def get_action(self):
      return self.__action

    def get_steps(self):
      return self.__steps

    def decode(self, str):
        m = re.findall(self.REGEX_OPERAND, str)
        if m:
          o, s, n = m[0]
          self.__action = o
          self.__steps = int(s+n)

    def __repr__(self):
      return 'ACTION: {}, STEPS: {}'.format(self.__action, self.__steps)