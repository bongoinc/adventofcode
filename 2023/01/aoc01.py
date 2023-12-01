#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser(description='AdventOfCode 2023 task 1')
parser.add_argument('-i', '--input', help='Indata file, default data.txt', default='data.txt')
args = parser.parse_args()

def main():
  print("--- ADVENT OF CODE 2023 DAY 1 ---")
  indata = get_indata(args.input)

  print("PART1: The answer is %d." % part_one(indata))
  # print("PART2: The answer is %d." % part_two(all_calories))

def get_indata(filename):
  indata = []
  f = open(filename, 'r')
  for row in f:
    indata.append(row.strip())

#  print(indata)
  return indata

def get_value_from_string(string):
  digits = [d for d in string if d.isdigit()]
  if digits:
    first_digit = digits[0]
    last_digit = digits[-1]
    return int(first_digit + last_digit)
  else:
    return None

def part_one(data):
  total = 0
  for d in data:
    total = total + get_value_from_string(d)
  return total

# def part_two(data):
#   data.sort(reverse=True)
#   return sum(data[0:3])


if __name__ == '__main__':
    main()
