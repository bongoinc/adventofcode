#!/usr/bin/python

import argparse
import re

parser = argparse.ArgumentParser(description='AdventOfCode 2018 task 2')
parser.add_argument('-i', '--input', help='Indata file, default data.txt', default='data.txt')
args = parser.parse_args()

def main():
  print('--- ADVENT OF CODE 2018 DAY  ---')

  twos = 0
  threes = 0
  ids = []

  f = open(args.input, 'r')

  for box_id in f:
    ids.append(box_id.strip())
    tw, th = check_box_id(box_id.strip())
#    print("ID: {}, 2: {}, 3: {}".format(box_id.strip(), tw, th))
    twos += tw
    threes += th

  task_two_solution = task_two(ids)

  print("PART1: The checksum is %d!" % (twos*threes))
  print("PART2: The common characters between the correct box ids are {}!".format(task_two_solution))

def compare_ids(id_one, id_two):
  diffs = 0
  for i in range(len(id_one)):
#    print('{}:{}'.format(id_one[i], id_two[i]))
    if id_one[i] != id_two[i]:
      diffs += 1

  if diffs == 1:
    print('[{}|{}]: {}'.format(id_one, id_two, diffs))
  
  return diffs

def task_two(id_list):
  l = len(id_list)-1
  for i in range(l):
    for j in range(l):
      if compare_ids(id_list[i], id_list[j+1]) == 1:
        return get_common_chars(id_list[i], id_list[j+1])
  return 'Nada'

def get_common_chars(str1, str2):
  rv = ''
  for i in range(len(str1)):
    if str1[i] == str2[i]:
      rv = rv + str1[i]

  return rv

def check_box_id(id):
  uniq_chars = set(list(id))
  two = 0
  three = 0
#  print('UniqChars: {}'.format(uniq_chars))

  for c in uniq_chars:
    n = id.count(c)
    if n == 2:
      two = 1
    if n == 3:
      three = 1

    if two != 0 and three != 0:
      break

  return two,three

if __name__ == '__main__':
    main()
