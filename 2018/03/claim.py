class Claim:
  def __init__(self, data):
    parts = data.split(' ')
    self._id = parts[0][1:]
    coords = parts[2][:-1].split(',')
    self._x = int(coords[0])
    self._y = int(coords[1])
    area = parts[3].split('x')
    self._width = int(area[0])
    self._height = int(area[1])

  def get_id(self):
    return self._id

  def get_x(self):
    return self._x

  def get_y(self):
    return self._y

  def get_width(self):
    return self._width

  def get_height(self):
    return self._height

  def __str__(self):
    return 'ID: {}, X: {}, Y: {}, W: {}, H: {}'.format(self._id, self._x, self._y, self._width, self._height)