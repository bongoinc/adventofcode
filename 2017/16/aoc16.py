#!/usr/bin/python

import argparse
from string import ascii_lowercase

parser = argparse.ArgumentParser(description='AdventOfCode 2017 task 16')
parser.add_argument('-i', '--input', help='Indata file, default data.txt', default='data.txt')
parser.add_argument('-r', '--regs', help='Number of registers, default 16', default='16')
args = parser.parse_args()

# Constants
CMD_SPIN = 's'
CMD_EXCHANGE = 'x'
CMD_PARTNER = 'p'

def main():
  print("--- ADVENT OF CODE 2017 DAY 16 ---")

  # Creating register
  register = create_register(min(16, int(args.regs)))
  print("REGISTER: %s" % register)
  print("REGISTER: %s" % rotate(register, 1))

  f = open(args.input, 'r')
  cmds = f.read().rstrip().split(',')

  print("No of commands: %d!" % len(cmds))
  for cmd in cmds:
    if cmd[0] == CMD_SPIN:
      print("SPIN, VALUES %d" % int(cmd[1:]))
    elif cmd[0] == CMD_EXCHANGE:
      print("EXCHANGE")
    elif cmd[0] == CMD_PARTNER:
      print("PARTNER")



  print("PART1: The solution of this captcha is %d!" % 1)
  print("PART2: The solution of this captcha is %d!" % 2)

def create_register(chars):
  print("CHARS: %d" % chars)
  return ascii_lowercase[:chars]

def rotate(strg, n):
  return strg[n:] + strg[:n]

if __name__ == '__main__':
    main()
