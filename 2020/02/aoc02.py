#!/usr/bin/python

import argparse
import re

parser = argparse.ArgumentParser(description='AdventOfCode 2020 task 2')
parser.add_argument('-i', '--input', help='Indata file, default data.txt', default='data.txt')
args = parser.parse_args()

def main():
    print("--- ADVENT OF CODE 2020 DAY 2 ---")

    cnt1 = 0
    cnt2 = 0

    f = open(args.input, 'r')

    for row in f:
        l, h, c, p = parse_input_string(row.strip())
        if l <= p.count(c) <= h:
            cnt1 += 1
        if bool(p[l-1] == c) ^ bool(p[h-1] == c):
            cnt2 += 1

    print("PART1: The number of valid passwords are %d!" % cnt1)
    print("PART2: The number of valid passwords are %d!" % cnt2)


def parse_input_string(s):
    r = re.findall(r"[\w']+", s)
#    print(r)
    return int(r[0]), int(r[1]), r[2], r[3]


if __name__ == '__main__':
    main()

