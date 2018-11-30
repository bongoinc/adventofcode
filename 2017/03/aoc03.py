#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser(description='AdventOfCode 2017 task 3')
parser.add_argument('-e', '--end', help='Secret key, default 368078', default='368078')
args = parser.parse_args()

def main():
    print("--- ADVENT OF CODE 2017 DAY 3 ---")
    end = int(args.end)
    distance = 0
    l, r, t, b = 0
    directions = ['r', 'u', 'l', 'd']
    cd = directions[0]

    for num in range(1, end):

    print("PART1: The distance is %s!" % distance)


if __name__ == '__main__':
    main()
