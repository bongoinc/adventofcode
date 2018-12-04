#!/usr/bin/python

import argparse
from fabric_matrix import FabricMatrix
from claim import Claim

parser = argparse.ArgumentParser(description='AdventOfCode 2018 task 3')
parser.add_argument('-i', '--input', help='Indata file, default data.txt', default='data.txt')
args = parser.parse_args()

def main():
  print("--- ADVENT OF CODE 2018 DAY 3 ---")

  claim_matrix = FabricMatrix(1000, 1000)

  f = open(args.input, 'r')

  for row in f:
    data = Claim(row)
    claim_matrix.claim_area(data)

  print("PART1: There are %d overlapping areas in the fabric!" % claim_matrix.get_amount_of_multiple_claims())

  id = -1
  f.seek(0)
  for row in f:
    data = Claim(row)
    if claim_matrix.check_for_only_claimer(data) == True:
      id = data.get_id()
      break

  if id != -1:
  	print("PART2: The only ID that doesnt overlap is %d!" % int(id))
  else:
    print("PART2: DIDNT FIND ANY ID THAT DONT OVERLAP!!!")

if __name__ == '__main__':
  main()
