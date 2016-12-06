#!/usr/bin/python

import argparse
from keypad import KeyPad

parser = argparse.ArgumentParser(description='AdventOfCode 2016 task 2')
parser.add_argument('-i', '--input', help='Indata file, default data.txt', default='data.txt')
args = parser.parse_args()

def main():
	print("--- ADVENT OF CODE 2016 DAY 2 ---")

	kp = KeyPad()
	bathroom_code = ''

	f = open(args.input, 'r')

	for instructions in f:
		bathroom_code += kp.parse_instructions(instructions)

	print("PART1: The bathroom code is %s!" % bathroom_code)
#	print("PART2: The elves need to order %d feet of ribbons!" % ribbons)

if __name__ == '__main__':
    main()
