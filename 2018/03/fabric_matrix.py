from claim import Claim

class FabricMatrix:
  def __init__(self, width, height):
    self._width = width
    self._height = height
    self._matrix = []

    for x in range(0, self._width):
      row = []
      for y in range(0,self._height):
        row.append(list())

      self._matrix.append(row)

  def claim_area(self, claim):
#    print('CLAIM[{}]'.format(claim))
    for x in range(claim.get_x(), claim.get_x()+claim.get_width()):
      row = self._matrix[x]
      for y in range(claim.get_y(), claim.get_y()+claim.get_height()):
        row[y].append(claim.get_id())
#    print('Claimming area for elf #{}.'.format(claim.get_id()))

  def check_for_only_claimer(self, claim):
    for x in range(claim.get_x(), claim.get_x()+claim.get_width()):
      row = self._matrix[x]
      for y in range(claim.get_y(), claim.get_y()+claim.get_height()):
        if len(row[y]) != 1 or row[y][0] != claim.get_id():
          return False

    return True

  def get_amount_of_multiple_claims(self):
    multiple_claims = 0
    for x in range(0, self._width):
      row = self._matrix[x]
      for y in range(0, self._height):
        claims_list = row[y]
        if len(claims_list) > 1:
          multiple_claims += 1

    return multiple_claims
