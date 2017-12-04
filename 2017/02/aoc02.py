#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser(description='AdventOfCode 2017 task 2')
parser.add_argument('-i', '--input', help='Indata file, default data.txt', default='data.txt')
args = parser.parse_args()

def main():
  print("--- ADVENT OF CODE 2017 DAY 2 ---")

  checksum1 = 0
  checksum2 = 0

  f = open(args.input, 'r')

  for row in f:
    rowlist = map(int, row.split(" "))
    checksum1 += (int(max(rowlist)) - int(min(rowlist)))
    checksum2 += get_checksum_from_list(rowlist)

  print("PART1: The first checksum is %d!" % checksum1)
  print("PART2: The second checksum is %d!" % checksum2)

def get_checksum_from_list(numbers):
  for num1 in numbers:
    for num2 in numbers:
      if num1 == num2: # Ignore same numbers
        continue

      high = max(num1, num2) # Get the highest number
      low = min(num1, num2)  # Get the lowest number

      if high % low == 0:
        return high/low

if __name__ == '__main__':
    main()
