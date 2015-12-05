import argparse

parser = argparse.ArgumentParser(description='AdventOfCode task 1')
parser.add_argument('-i', '--input', help='Indata file, default data.txt', default='data.txt')
args = parser.parse_args()

def main():
	print("--- ADVENT OF CODE 2015 DAY 1 ---")

	floor = 0
	first_basement = -1
	pos = 0

	f = open(args.input, 'r')
	data = f.read()

	for c in data:
		pos += 1
		if c == '(':
			floor += 1
		elif c == ')':
			floor -= 1

		if first_basement == -1 and floor == -1 :
			first_basement = pos

	print("PART1: Santa will end up on floor %d!" % floor)
	print("PART2: The character position that first takes Santa to the basement is %d!" % first_basement)

if __name__ == '__main__':
    main()
