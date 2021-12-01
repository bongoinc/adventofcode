#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser(description='AdventOfCode 2021 task 1')
parser.add_argument('-i', '--input', help='Indata file, default data.txt', default='data.txt')
args = parser.parse_args()

def main():
  print("--- ADVENT OF CODE 2021 DAY 1 ---")
  cnt = 0
  previous = -1

  f = open(args.input, 'r')
  for row in f:
    current = int(row)
    if previous != -1:
      if current > previous:
        cnt += 1
    previous = current
    
  print("PART1: %d measurements are bigger than the previous." % cnt)
#  print("PART2: The first reoccuring frequency is {} after {} repeats!".format(second_answer, repeats))

if __name__ == '__main__':
    main()
