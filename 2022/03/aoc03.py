#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser(description='AdventOfCode 2022 task 3')
parser.add_argument('-i', '--input', help='Indata file, default data.txt', default='data.txt')
args = parser.parse_args()

def main():
  print("--- ADVENT OF CODE 2022 DAY 3 ---")
  indata = get_indata(args.input)

  print("PART1: The answer is %d." % part_one(indata))
  print("PART2: The answer is %d." % part_two(indata))

def get_indata(filename):
  indata = []
  f = open(filename, 'r')
  for row in f:
    indata.append(row.strip())
  return indata

def part_one(indata):
  data = shared_characters(indata)
  sum = 0
  for c in data:
    sum = sum + get_priority(c)
  return sum

def part_two(data):
  sum = 0
  for idx in range(0, len(data), 3):
    rucksacks = data[idx:idx+3]
    chrs = intersection3(rucksacks[0], rucksacks[1], rucksacks[2])
    sum = sum + get_priority(chrs[0])
  return sum

def get_priority(chr):
  rv = 0
  if ord(chr) > 96:
    rv = ord(chr) - 96
  else:
    rv = ord(chr) - 38
  return rv

def chunkIt(seq, num):
  avg = len(seq) / float(num)
  out = []
  last = 0.0

  while last < len(seq):
    out.append(seq[int(last):int(last + avg)])
    last += avg
  return out

def intersection2(lst1, lst2):
  return list(set(lst1) & set(lst2))

def intersection3(lst1, lst2, lst3):
  return list(set(lst1) & set(lst2) & set(lst3))

def shared_characters(indata):
  chars = []
  for c in indata:
    comps = chunkIt(list(c), 2)
    common = intersection2(comps[0], comps[1])
    chars.append(common[0])
  return chars

if __name__ == '__main__':
    main()
