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

def main():
  print("--- ADVENT OF CODE 2017 DAY 16 ---")

  # Creating register
  register = create_register(min(16, int(args.regs)))

  f = open(args.input, 'r')
  cmds = f.read().rstrip().split(',')
  run_once = False

#  print("No of commands: %d!" % len(cmds))
#  print("REGISTER: %s" % register)
  for i in range(1000000000):
    for cmd in cmds:
      if cmd[0] == CMD_SPIN:
  #      print("SPIN, VALUES %d" % int(cmd[1:]))
        register = spin(register, int(cmd[1:]))
      elif cmd[0] == CMD_EXCHANGE:
  #      print("EXCHANGE")
        pos = cmd[1:].split('/')
        register = exchange(register, int(pos[0]), int(pos[1]))
      elif cmd[0] == CMD_PARTNER:
  #      print("PARTNER")
        chars = cmd[1:].split('/')
        register = partner(register, chars[0], chars[1])

    if run_once == False:
      print("PART1: The order of the programs after their dance is %s%s%s!" % (GREEN, register, ENDC))
      run_once = True

    if i % 10000000:
      print("%d%" % (10000000/i))

    gc.collect()

  print("PART2: The order of the programs after a billion dances is %s%s%s!" % (GREEN, register, ENDC))

def create_register(chars):
#  print("CHARS: %d" % chars)
  return ascii_lowercase[:chars]

def spin(strg, n):
#  print("strg[:-n]: %s" % strg[:-n])
#  print("strg[-n:]: %s" % strg[-n:])
  return strg[-n:] + strg[:-n]

def exchange(strg, p1, p2):
#  print("pos1: %d, pos2: %d" % (p1, p2))
  rv = list(strg)
  rv[p1] = strg[p2]
  rv[p2] = strg[p1]
  return "".join(rv)

def partner(strg, c1, c2):
#  print("char1: %s, char2: %s" % (c1, c2))
  p1 = strg.index(c1)
  p2 = strg.index(c2)
  return exchange(strg, p1, p2)

if __name__ == '__main__':
    main()
