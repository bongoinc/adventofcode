#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser(description='AdventOfCode 2021 task 3')
parser.add_argument('-i', '--input', help='Indata file, default data.txt', default='data.txt')
args = parser.parse_args()

def main():
  print("--- ADVENT OF CODE 2021 DAY 3 ---")
  indata = get_indata(args.input)
  
  print("PART1: The answer is %d." % part_one(indata))
  print("PART2: The answer is %d." % part_two(indata))

def get_indata(filename):
  indata = []
  f = open(filename, 'r')
  for row in f:
    indata.append(row.strip())
  return indata

def get_most_and_least_common(indata):
  m = l = ''
  for i in range(len(indata[0])):
    posbit = []
    for row in indata:
      posbit.append(row[i])
    zeros = posbit.count('0')
    ones = posbit.count('1')
    if zeros > ones:
      m += '0'
      l += '1'
    else:
      m += '1'
      l += '0'

  return m, l

def part_one(indata):
  gamma, epsilon = get_most_and_least_common(indata)
  print("GAMMA: %s, EPSILON: %s" % (gamma, epsilon))
  return int(gamma, 2) * int(epsilon, 2)

def part_two(indata):
  return 0


if __name__ == '__main__':
    main()
