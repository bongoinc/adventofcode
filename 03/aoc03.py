#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser(description='AdventOfCode task 3')
parser.add_argument('-i', '--input', help='Indata file, default data.txt', default='data.txt')
args = parser.parse_args()

def main():
	print("--- ADVENT OF CODE 2015 DAY 3 ---")

	f = open(args.input, 'r')
	data = f.read()

	part1_answer = part1(data)
	part2_answer = part2(data)

	print("PART1: %d houses will receive at least one gift!" % part1_answer)
	print("PART1: %d houses will receive at least one gift!" % part2_answer)

def part1(data):
	STARTING_POINT = "0,0"
	coordinates = [STARTING_POINT]
	x = 0
	y = 0

	for c in data:
		if c == '^':
			y += 1
		elif c == 'v':
			y -= 1
		elif c == '>':
			x += 1
		elif c == '<':
			x -= 1

		pos = str(x) + ',' + str(y)

		if pos not in coordinates:
			coordinates.append(pos)

	return len(coordinates)

def part2(data):
	STARTING_POINT = "0,0"
	coordinates = [STARTING_POINT]
	santa_x = 0
	santa_y = 0
	robot_x = 0
	robot_y = 0
	santas_turn = True

	for c in data:

		if santas_turn:
			if c == '^':
				santa_y += 1
			elif c == 'v':
				santa_y -= 1
			elif c == '>':
				santa_x += 1
			elif c == '<':
				santa_x -= 1

			pos = str(santa_x) + ',' + str(santa_y)
		else:
			if c == '^':
				robot_y += 1
			elif c == 'v':
				robot_y -= 1
			elif c == '>':
				robot_x += 1
			elif c == '<':
				robot_x -= 1

			pos = str(robot_x) + ',' + str(robot_y)

		if pos not in coordinates:
			coordinates.append(pos)

		santas_turn = not santas_turn

	return len(coordinates)

if __name__ == '__main__':
    main()
