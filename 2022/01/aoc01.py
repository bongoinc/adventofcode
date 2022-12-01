#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser(description='AdventOfCode 2022 task 1')
parser.add_argument('-i', '--input', help='Indata file, default data.txt', default='data.txt')
args = parser.parse_args()

def main():
  print("--- ADVENT OF CODE 2022 DAY 1 ---")
  indata = get_indata(args.input)
  all_calories = count_all_calories(indata)

  print("PART1: The answer is %d." % part_one(all_calories))
  print("PART2: The answer is %d." % part_two(all_calories))

def get_indata(filename):
  indata = []
  f = open(filename, 'r')
  for row in f:
    indata.append(row.strip())

#  print(indata)
  return indata

def count_all_calories(calories):
  data = []
  sum = 0;

  for c in calories:
    if len(c) == 0:
      data.append(sum)
      sum = 0
    else:
      sum = sum + int(c)
  data.append(sum)

  return data

def part_one(data):
  return max(data)

def part_two(data):
  data.sort(reverse=True)
  return sum(data[0:3])


if __name__ == '__main__':
    main()
