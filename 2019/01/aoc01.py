#!/usr/bin/python

import argparse
import math

parser = argparse.ArgumentParser(description='AdventOfCode 2019 task 1')
parser.add_argument('-i', '--input', help='Indata file, default data.txt', default='data.txt')
args = parser.parse_args()

def main():
  print("--- ADVENT OF CODE 2019 DAY 1 ---")

  sum1 = 0
  sum2 = 0

  f = open(args.input, 'r')

  for mass in f:
    sum1 += calculate_fuel(int(mass))
    sum2 += calculate_fuel2(int(mass))

  print("PART1: The sum of required fuel is %d!" % sum1)
  print("PART2: The sum of required fuel is %d!" % sum2)

def calculate_fuel(mass):
  return math.floor(mass / 3) - 2

def calculate_fuel2(mass):
  fuel = math.floor(mass / 3) - 2
  if fuel <= 0:
    return 0
  else:
    return fuel + calculate_fuel2(fuel)

if __name__ == '__main__':
    main()
