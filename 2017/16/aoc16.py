#!/usr/bin/python

import argparse
from string import ascii_lowercase
import gc

parser = argparse.ArgumentParser(description='AdventOfCode 2017 task 16')
parser.add_argument('-i', '--input', help='Indata file, default data.txt', default='data.txt')
parser.add_argument('-r', '--regs', help='Number of registers, default 16', default='16')
args = parser.parse_args()

# Constants
GREEN = '\033[92m'
ENDC = '\033[0m'

CMD_SPIN = 's'
CMD_EXCHANGE = 'x'
CMD_PARTNER = 'p'

# Creating register
register = ''

def main():
  print("--- ADVENT OF CODE 2017 DAY 16 ---")

  f = open(args.input, 'r')
  cmds = f.read().rstrip().split(',')
  run_once = False

#  register = list(create_register(min(16, int(args.regs))))
  register = create_register(min(16, int(args.regs)))
  print register

#  for i in range(1000000000):
  for cmd in cmds:
    if cmd[0] == CMD_SPIN:
      spin(int(cmd[1:]))
    else:
      c = cmd[1:].split('/')
#      if cmd[0] == CMD_EXCHANGE:
#        exchange(int(c[0]), int(c[1]))
#      elif cmd[0] == CMD_PARTNER:
#        partner(c[0], c[1])
    print register

#    if run_once == False:
  print("PART1: The order of the programs after their dance is %s%s%s!" % (GREEN, register, ENDC))
#      run_once = True

#    if i % 10000000:
#      print("%d%" % (10000000/i))

#    gc.collect()

#  print("PART2: The order of the programs after a billion dances is %s%s%s!" % (GREEN, register, ENDC))

def create_register(chars):
  return ascii_lowercase[:chars]

def spin(n):
  global register
  print n
  print register[-n:]
  print register[:-n]
#  register = register[-n:] + register[:-n]
  register = '{0}{1}'.format(register[-n:], register[:-n])

def exchange(p1, p2):
  global register
  rv = list(register)
  rv[p1] = register[p2]
  rv[p2] = register[p1]
  register = ''.join(rv)

def partner(c1, c2):
  global register
  exchange(register.index(c1), register.index(c2))

if __name__ == '__main__':
    main()
