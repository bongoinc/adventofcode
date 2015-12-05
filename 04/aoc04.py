import argparse
import hashlib

parser = argparse.ArgumentParser(description='AdventOfCode task 4')
parser.add_argument('-k', '--key', help='Secret key, default iwrupvqb', default='iwrupvqb')
args = parser.parse_args()

def main():
	print("--- ADVENT OF CODE 2015 DAY 4 ---")
	key = args.key
	final_num1 = 0
	final_num2 = 0
	part1_done = False
	part2_done = False

	for num in range(1, 999999999):
		m = hashlib.md5()
		str2hash = key + str(num)
		m.update(str2hash.encode('utf-8'))
		md5 = m.hexdigest()

		if part1_done == False and md5[0:5] == '00000':
			print("- Found a match for part1, MD5 = %s" % md5[0:16])
			final_num1 = num
			part1_done = True

		if part2_done == False and md5[0:6] == '000000':
			print("- Found a match for part2, MD5 = %s" % md5[0:16])
			final_num2 = num
			part2_done = True

		if part1_done == True and part2_done == True:
			print("Found both, quitting...")
			break

	print("PART1: The lowest number that produces a hash that starts with 5 zeros for the key %s is %d!" % (key, final_num1))
	print("PART2: The lowest number that produces a hash that starts with 6 zeros for the key %s is %d!" % (key, final_num2))


if __name__ == '__main__':
    main()
