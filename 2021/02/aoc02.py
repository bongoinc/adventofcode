#!/usr/bin/python

import argparse
from action import Action

parser = argparse.ArgumentParser(description='AdventOfCode 2021 task 2')
parser.add_argument('-i', '--input', help='Indata file, default data.txt', default='data.txt')
args = parser.parse_args()

def main():
  print("--- ADVENT OF CODE 2021 DAY 2 ---")
  indata = get_indata(args.input)
  
  print("PART1: The answer is %d." % part_one(indata))
  print("PART2: The answer is %d." % part_two(indata))

def get_indata(filename):
  indata = []
  f = open(filename, 'r')
  for row in f:
    o = Action(row.strip())
    indata.append(o)
  return indata

def part_one(actions):
  pos = 0
  depth = 0
  
  for a in actions:
    if a.get_do() == "forward":
      pos = pos + a.get_steps()
    elif a.get_do() == "down":
      depth = depth + a.get_steps()
    elif a.get_do() == "up":
      depth = depth - a.get_steps()
  return pos * depth

def part_two(actions):
  return 0

if __name__ == '__main__':
    main()
