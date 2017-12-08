class Memory:
  def __init__(self, banks):
    self.__banks = list(banks)

  def size(self):
    return len(self.__banks)

  def state(self):
    pattern = ""
    for c in self.__banks:
      pattern += str(c) + " "

    return pattern.strip()

  def get_highest_value(self):
    mv = max(self.__banks)
    return self.__banks.index(mv), mv

  def __increase_value_at(self, pos):
    self.__banks[pos] += 1

  def increment_starting_at(self, start, inc):
    current_pos = start
    self.__banks[start] = 0
    for i in range(1, inc+1):
      if(current_pos == self.size()-1):
        current_pos = 0
      else:
        current_pos += 1
      self.__increase_value_at(current_pos)
#    print(self.state())
