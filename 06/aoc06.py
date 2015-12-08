import argparse
import hashlib
from lampmatrix import LampMatrix

parser = argparse.ArgumentParser(description='AdventOfCode task 6')
parser.add_argument('-i', '--input', help='Indata file, default data.txt', default='data.txt')
args = parser.parse_args()

def main():
	print("--- ADVENT OF CODE 2015 DAY 6 ---")

	part1matrix = LampMatrix(1000, 1000)
	part2matrix = LampMatrix(1000, 1000)

	f = open(args.input, 'r')

	for instruction in f:
		cmd = instruction.split(" ")

		if cmd[0] == 'turn':
			f = get_coord(cmd[2])
			t = get_coord(cmd[4])

			if cmd[1] == 'on':
				part1matrix.turn_on(f[0], f[1], t[0], t[1])
				part2matrix.brighten(f[0], f[1], t[0], t[1])
			elif cmd[1] == 'off':
				part1matrix.turn_off(f[0], f[1], t[0], t[1])
				part2matrix.darken(f[0], f[1], t[0], t[1])

		elif cmd[0] == 'toggle':
			f = get_coord(cmd[1])
			t = get_coord(cmd[3])
			part1matrix.toggle(f[0], f[1], t[0], t[1])
			part2matrix.super_brighten(f[0], f[1], t[0], t[1])

	print("PART1: There are %d light bulbs lit!" % part1matrix.lit())
	print("PART2: Total amount of brightness is %d!" % part2matrix.brightness())

def get_coord(s):
	return list(map(int, s.split(',')))

if __name__ == '__main__':
    main()
