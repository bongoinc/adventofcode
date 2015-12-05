import argparse

parser = argparse.ArgumentParser(description='AdventOfCode task 3')
parser.add_argument('-i', '--input', help='Indata file, default data.txt', default='data.txt')
args = parser.parse_args()

def main():
	print("--- ADVENT OF CODE 2015 DAY 3 ---")

	STARTING_POINT = "0,0"
	coordinates = [STARTING_POINT]
	x = 0
	y = 0

	f = open(args.input, 'r')
	data = f.read()

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
#		print("Pos: %s" % pos)

		if pos not in coordinates:
			coordinates.append(pos)

#	print(coordinates)
	print("PART1: %d houses will receive at least one gift!" % len(coordinates))
#	print("PART2: The character position that first takes Santa to the basement is %d!" % first_basement)


if __name__ == '__main__':
    main()
