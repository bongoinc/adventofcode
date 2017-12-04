#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser(description='AdventOfCode 2017 task 2')
parser.add_argument('-i', '--input', help='Indata file, default data.txt', default='data.txt')
args = parser.parse_args()

def main():
  print("--- ADVENT OF CODE 2017 DAY 2 ---")

  checksum = 0

  f = open(args.input, 'r')

  for row in f:
    rowlist = map(int, row.split(" "))
#    print(rowlist)
#    print("MAX: %d, MIN: %d, DIFF: %d" % (int(max(rowlist)), int(min(rowlist)), int(max(rowlist)) - int(min(rowlist))))
    checksum += (int(max(rowlist)) - int(min(rowlist)))

  print("PART1: The checksum is %d!" % checksum)

if __name__ == '__main__':
    main()
