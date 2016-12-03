#!/usr/bin/python

import argparse
from blockcoords import BlockCoords

parser = argparse.ArgumentParser(description='AdventOfCode 2016 task 1')
parser.add_argument('-i', '--input', help='Indata file, default data.txt', default='data.txt')
args = parser.parse_args()

def main():
	print("--- ADVENT OF CODE 2016 DAY 1 ---")

	bc = BlockCoords()

	f = open(args.input, 'r')
	data = f.read()

	cmds = data.split(", ")

	for cmd in cmds:
		bc.set_direction(cmd[0])
		bc.move_blocks(int(''.join(cmd[1:])))

	print("PART1: Easter Bunnys HQ is %d blocks away!" % bc.get_blocks())

if __name__ == '__main__':
    main()
