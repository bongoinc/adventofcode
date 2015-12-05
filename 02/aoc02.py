import argparse

parser = argparse.ArgumentParser(description='AdventOfCode task 2')
parser.add_argument('-i', '--input', help='Indata file, default data.txt', default='data.txt')
args = parser.parse_args()

def main():
	print("--- ADVENT OF CODE 2015 DAY 2 ---")

	wrapping = 0
	ribbons = 0

	f = open(args.input, 'r')

	for gift in f:
		sides = gift.split('x')

		length = float(sides[0])
		width  = float(sides[1])
		height = float(sides[2])

		wrapping += get_wrapping(length, width, height)
		ribbons += get_ribbons(length, width, height)

	print("PART1: The elves need to order %d square feet of wrapping paper!" % wrapping)
	print("PART2: The elves need to order %d feet of ribbons!" % ribbons)

def get_wrapping(l, w, h):

	t = l*w
	f = w*h
	s = h*l

	slack = min(t, f, s)

	return 2*t + 2*f + 2*s + slack

def get_ribbons(l, w, h):

	bow = l*w*h

	deletable = max(l, w, h)
	lowest = [l, w, h]
	lowest.remove(deletable)

	return 2*lowest[0] + 2*lowest[1] + bow

if __name__ == '__main__':
    main()
