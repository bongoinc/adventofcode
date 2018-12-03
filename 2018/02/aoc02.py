#!/usr/bin/python

import argparse
import re

parser = argparse.ArgumentParser(description='AdventOfCode 2018 task 2')
parser.add_argument('-i', '--input', help='Indata file, default data.txt', default='data.txt')
args = parser.parse_args()

def main():
  print('--- ADVENT OF CODE 2018 DAY  ---')

  twos = 0
  threes = 0

  f = open(args.input, 'r')

  for box_id in f:
    tw, th = check_box_id(box_id.strip())
#    print("ID: {}, 2: {}, 3: {}".format(box_id.strip(), tw, th))
    twos += tw
    threes += th

  print("PART1: The checksum is %d!" % (twos*threes))
#  print("PART2: The first reoccuring frequency is {} after {} repeats!".format(second_answer, repeats))

def check_box_id(id):
  uniq_chars = set(list(id))
  two = 0
  three = 0
#  print('UniqChars: {}'.format(uniq_chars))

  for c in uniq_chars:
    n = id.count(c)
    if n == 2:
      two = 1
    if n == 3:
      three = 1

    if two != 0 and three != 0:
      break

  return two,three

if __name__ == '__main__':
    main()
