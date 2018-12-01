#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser(description='AdventOfCode 2018 task 1')
parser.add_argument('-i', '--input', help='Indata file, default data.txt', default='data.txt')
args = parser.parse_args()

def main():
  print("--- ADVENT OF CODE 2018 DAY 1 ---")

  frequency = 0
  changes = []
  frequencies = [] 
  first_repeat_found = False

  f = open(args.input, 'r')
  frequencies.append(frequency)

  for diff in f:
    changes.append(diff)
    frequency = eval('frequency' + diff)
    if not first_repeat_found:
      if frequency in frequencies:
        print('IN LIST!!! {}'.format(frequency))
        first_repeat_found = True
    frequencies.append(frequency)
  
  first_answer = frequency
  second_answer = -99999999999
  repeats = 1

  while first_repeat_found == False:
    repeats = repeats+1
    for diff in changes:
      frequency = eval('frequency' + diff)
      if frequency in frequencies:
        first_repeat_found = True
        second_answer = frequency
        break

  print("PART1: The resulting frequency is %d!" % first_answer)
  print("PART2: The first reoccuring frequency is {} after {} repeats!".format(second_answer, repeats))

if __name__ == '__main__':
    main()
