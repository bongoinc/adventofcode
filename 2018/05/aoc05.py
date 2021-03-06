#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser(description='AdventOfCode 2018 task 5')
parser.add_argument('-i', '--input', help='Indata file, default data.txt', default='data.txt')
args = parser.parse_args()

def main():
  print("--- ADVENT OF CODE 2018 DAY 5 ---")

  f = open(args.input, 'r')
  data = list(f.read())

  print("PART1: %d units remain after fully reacting to the scanned polymer!" % calculate_remaining_units(data))

  chars = sorted(get_list_of_characters(data))
  print('CHARS: {}'.format(chars))
  results = {}

  for c in chars:
    idata = remove_chars_from_list(data, c)
    l = calculate_remaining_units(idata)
    print('CHAR: {}, LENGTH: {}'.format(c, l))
    results[c] = l

    shortest = get_shortest(results)

  print("PART2: The shortest polymer produced is {} by removing all {}!".format(results[shortest], shortest))

def get_shortest(d):
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(min(v))]

def remove_chars_from_list(data, char):
  tempdata = data.copy()
  tempdata = list(filter(lambda a: a != char.lower(), tempdata))
  tempdata = list(filter(lambda a: a != char.upper(), tempdata))

  return tempdata

def get_list_of_characters(data):
  tempset = set(data)
  rv = set()
  for c in tempset:
    rv.add(c.lower())

  return list(rv)

def calculate_remaining_units(data):
  done = False
  while not done:
    for i in range(0, len(data)-1):
      if i == len(data)-2:
        done = True

      if data[i].lower() == data[i+1].lower() and ((data[i].islower() and data[i+1].isupper()) or (data[i].isupper() and data[i+1].islower())):
         del data[i+1]
         del data[i]
         break

  return len(data)

if __name__ == '__main__':
  main()
