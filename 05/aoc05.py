import argparse
import hashlib

parser = argparse.ArgumentParser(description='AdventOfCode task 5')
parser.add_argument('-i', '--input', help='Indata file, default data.txt', default='data.txt')
args = parser.parse_args()

VOWELS = ['a', 'e', 'i', 'o', 'u']
FORBIDDEN = ['ab', 'cd', 'pq', 'xy']

def main():
	print("--- ADVENT OF CODE 2015 DAY 5 ---")

	nice_words = 0
	f = open(args.input, 'r')

	for row in f:
		word = row.rstrip('\n')
#		print("%s: %d vowels, Doubles?: %s, Forbidden?: %s" % (word, count_vowels(word), check_for_double_chars(word), has_forbidden_string(word)))
		if count_vowels(word) >= 3 and check_for_double_chars(word) == True and not has_forbidden_string(word):
			nice_words += 1

	print("PART1: There are %d nice words in the list!" % nice_words)
	print("PART2: ???")

def count_vowels(word):
	cnt = 0
	for vowel in VOWELS:
		cnt += word.count(vowel)

	return cnt

def check_for_double_chars(word):
	for i in range(0, len(word)-1):
		if word[i] == word[i+1]:
			return True

	return False

def has_forbidden_string(word):
	for string in FORBIDDEN:
		if string in word:
			return True

	return False

if __name__ == '__main__':
    main()
