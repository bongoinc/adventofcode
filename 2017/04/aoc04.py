#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser(description='AdventOfCode 2017 task 4')
parser.add_argument('-i', '--input', help='Indata file, default data.txt', default='data.txt')
args = parser.parse_args()

def main():
  print("--- ADVENT OF CODE 2017 DAY 4 ---")

  valid1 = 0
  valid2 = 0

  f = open(args.input, 'r')

  for row in f:
    row = row.rstrip()
    phrase = row.split(" ")
    valid1 += check_for_validity(phrase)
    valid2 += check_for_validity2(phrase)

  print("PART1: There are %d valid passwords!" % valid1)
  print("PART2: There are %d valid passwords!" % valid2)

def check_for_validity(words):
  for word in words:
    if words.count(word) >= 2:
      return 0

  return 1

def check_for_validity2(words):
  wordSet = set()

  for word in words:
    wordSet.add("".join(sorted(list(word))))

  if len(words) != len(wordSet):
    return 0

  return 1

if __name__ == '__main__':
    main()
