#!/usr/bin/python

import argparse
import node

parser = argparse.ArgumentParser(description='AdventOfCode 2018 task 8')
parser.add_argument('-i', '--input', help='Indata file, default data.txt', default='data.txt')
args = parser.parse_args()

def main():
  print("--- ADVENT OF CODE 2018 DAY 8 ---")

  f = open(args.input, 'r')
  data = f.read().split(' ')
  lendata = len(data)

  print('Read {} numbers!'.format(lendata))

  root = Node()
  children = data[0]
  metadata = data[1]
  i = 2
  while i < lendata:
    for x in range(0, children):
      i, node = get_next_node(i+1, metadata)
      root.add_child(node)

def get_next_node(startpos, metadata):
  node = Node()
  children = data[0]
  metadata = data[1]
  return pos, 
#  print("PART1: %d units remain after fully reacting to the scanned polymer!" % calculate_remaining_units(data))
#  print("PART2: The shortest polymer produced is {} by removing all {}!".format(results[shortest], shortest))

if __name__ == '__main__':
  main()
