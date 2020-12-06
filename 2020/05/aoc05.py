#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser(description='AdventOfCode 2020 task 5')
parser.add_argument('-i', '--input', help='Indata file, default data.txt', default='data.txt')
args = parser.parse_args()

UPPER = 'BR'
LOWER = 'FL'

def main():
    print('--- ADVENT OF CODE 2020 DAY 5 ---')
    bps = []

    f = open(args.input, 'r')
    for row in f:
        bps.append(row.strip())

    seatids = get_seat_ids(bps)

    first_answer = max(seatids)
    second_answer = get_my_seat(sorted(seatids))

    print('PART1: The highest seatid is %d!' % first_answer)
    print('PART2: My seatid is %d!' % second_answer)

def get_my_seat(s):
    for i, id in enumerate(s):
        if s[i+1] == id+2:
            return id+1

def get_seat_ids(bps):
    ids = []
    for bp in bps:
        row, column = get_seat_from_boarding_pass(bp)
        ids.append(get_seat_id(row, column))
    return ids


def get_position(str, l, u):
    lo = l
    hi = u
    for c in str:
        if c in UPPER:
            lo = int(lo + (hi-lo+1)/2)
        elif c in LOWER:
            hi = int(hi - (hi-lo+1)/2)
    return hi

def get_seat_from_boarding_pass(bp):
    r = get_position(bp[:7], 0, 127)
    c = get_position(bp[-3:], 0, 7)
    return r, c

def get_seat_id(r, c):
    return r*8+c

if __name__ == '__main__':
    main()

