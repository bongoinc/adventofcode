#!/usr/bin/python

import argparse
from memory import Memory

parser = argparse.ArgumentParser(description='AdventOfCode 2017 task 6')
parser.add_argument('-i', '--input', help='Indata file, default data.txt', default='data.txt')
args = parser.parse_args()

def main():
  print("--- ADVENT OF CODE 2017 DAY 6 ---")
  cycles = 0
  first_occurence = -1
  patterns = []

  f = open(args.input, 'r')
  data = f.read()
  data = map(int, data.split("\t"))

  mem = Memory(data)

  patterns.append(mem.state())
  while True:
    idx, high = mem.get_highest_value()
    mem.increment_starting_at(idx, high)
    cycles += 1
    try:
      first_occurence = patterns.index(mem.state())
      break
    except ValueError:
      patterns.append(mem.state())

  print("PART1: It takes %d redistribution cycles before a pattern is reproduced!" % cycles)

if __name__ == '__main__':
    main()
