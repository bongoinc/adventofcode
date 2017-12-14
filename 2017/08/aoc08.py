#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser(description='AdventOfCode 2017 task 8')
parser.add_argument('-i', '--input', help='Indata file, default data.txt', default='data.txt')
args = parser.parse_args()

registers = {}
highest = list()

def main():
  print("--- ADVENT OF CODE 2017 DAY 8 ---")

  f = open(args.input, 'r')

  for instruction in f:
    cmd = instruction.rstrip().split(" ")

    if check_condition(cmd[4], cmd[5], cmd[6]) == True:
      if cmd[1] == 'inc':
        add_to_register(cmd[0], int(cmd[2]))
      else:
        subtract_from_register(cmd[0], int(cmd[2]))

    highest.append(max(registers.values()))

  print("PART1: There largest value in any register is %d!" % max(registers.values()))
  print("PART2: There largest value at any time in any register is %d!" % max(highest))

def check_condition(reg, cond, val):
  tmp = get_value_of_register(reg)
  return eval('tmp ' + cond + ' ' + val)

def add_to_register(reg, val):
  tmp = get_value_of_register(reg)
  set_value_in_register(reg, tmp+val)

def subtract_from_register(reg, val):
  tmp = get_value_of_register(reg)
  set_value_in_register(reg, tmp-val)

def get_value_of_register(reg):
  if registers.has_key(reg) == False:
    registers[reg] = 0
  return registers.get(reg)

def set_value_in_register(reg, val):
  registers[reg] = val

if __name__ == '__main__':
    main()