#!/usr/bin/python

import argparse
import hashlib

parser = argparse.ArgumentParser(description='AdventOfCode 2016 task 5')
parser.add_argument('-k', '--key', help='Secret key, default ojvtpuvg', default='ojvtpuvg')
parser.add_argument('-p', '--part', help='Part, default both parts', default='0')
args = parser.parse_args()

def main():
	print("--- ADVENT OF CODE 2016 DAY 5 ---")
	key = args.key
	part = args.part
	password1 = ''
	password2 = ['-', '-', '-', '-', '-', '-', '-', '-']

	if part == "1" or part == "0":
		print("Running PART1")
		for num in range(1, 999999999):
			m = hashlib.md5()
			str2hash = key + str(num)
			m.update(str2hash.encode('utf-8'))
			md5 = m.hexdigest()

			if md5[0:5] == '00000':
				print("- Found a match for part1, MD5 = %s, adding the char %s to the password." % (md5[0:16], md5[5]))
				password1 += md5[5]

				if len(password1) == 8:
					break;

		print("PART1: The password for the key %s is %s!" % (key, password1))

	if part == "2" or part == "0":
		print("Running PART2")
		for num in range(1, 999999999):
			m = hashlib.md5()
			str2hash = key + str(num)
			m.update(str2hash.encode('utf-8'))
			md5 = m.hexdigest()

			if md5[0:5] == '00000':
				print("- Found a match for part2, MD5 = %s, adding the char %s to the password on position %s. [%s]" % (md5[0:16], md5[6], md5[5], "".join(password2)))
				if md5[5].isdigit():
					pos = int(md5[5])
					if 0 <= pos < 8 and password2[pos] == '-':
						password2[pos] = md5[6]

				if "-" not in password2:
					break;

		print("PART2: The password for the key %s is %s!" % (key, "".join(password2)))

if __name__ == '__main__':
    main()
