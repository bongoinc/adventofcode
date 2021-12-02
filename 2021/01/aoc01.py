#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser(description='AdventOfCode 2021 task 1')
parser.add_argument('-i', '--input', help='Indata file, default data.txt', default='data.txt')
args = parser.parse_args()

def main():
  print("--- ADVENT OF CODE 2021 DAY 1 ---")
  indata = get_indata(args.input)
  
  print("PART1: %d measurements are bigger than the previous." % part_one(indata))
  print("PART2: %d measurements are bigger than the previous." % part_two(indata))

def get_indata(filename):
  indata = []
  f = open(filename, 'r')
  for row in f:
    indata.append(int(row.strip()))
  return indata

def part_one(indata):
  cnt = 0
  previous = -1
  
  for current in indata:
    if previous != -1:
      if current > previous:
        cnt += 1
    previous = current
  return cnt

def part_two(indata):
  cnt = 0
  previous = -1
  
  for i in range(len(indata)-2):
    current = indata[i] + indata[i+1] + indata[i+2]
#    print("INDATA[%d,%d,%d]: %d" % (indata[i], indata[i+1], indata[i+2], current))
    if previous != -1:
      if current > previous:
        cnt += 1
    previous = current
  return cnt

if __name__ == '__main__':
    main()
