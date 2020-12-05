#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser(description='AdventOfCode 2020 task 5')
parser.add_argument('-i', '--input', help='Indata file, default data.txt', default='data.txt')
args = parser.parse_args()

UPPER = []
LOWER = []

def main():
    print('--- ADVENT OF CODE 2020 DAY 5 ---')
    bps = []

    f = open(args.input, 'r')
    for row in f:
        bps.append(row.strip())

    first_answer = -1
    second_answer = -1

    for bp in bps:
        row, column = get_seat_from_boarding_pass(bp)
        first_answer = max(first_answer, get_seat_id(row, column))

    print('PART1: The number of valid passports is %d!' % first_answer)
    print('PART2: The number of valid passports is %d!' % second_answer)

def get_position(str, l, u):
    print("STR: {}, LOW: {}, HI: {}".format(str, l, u))
    lo = l
    hi = u
    for c in str:
        if c in UPPER:
            lo = lo + (hi-lo+1)/2
        elif c in LOWER:
            hi = hi - (hi-lo+1)/2
    return hi

def get_seat_from_boarding_pass(bp):
    r = get_position(bp[0,8], 0, 127)
    c = get_position(bp[-3:], 0, 7)
    return r, c

def get_seat_id(r, c):
    return r*8+c

if __name__ == '__main__':
    main()

