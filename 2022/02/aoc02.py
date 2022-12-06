#!/usr/bin/python

import argparse
from rockpaperscissor import RPS

parser = argparse.ArgumentParser(description='AdventOfCode 2022 task 2')
parser.add_argument('-i', '--input', help='Indata file, default data.txt', default='data.txt')
args = parser.parse_args()

def main():
    print("--- ADVENT OF CODE 2022 DAY 2 ---")
    indata = get_indata(args.input)

    print("PART1: The answer is %d." % part_one(indata))
    print("PART2: The answer is %d." % part_two(indata))

def part_one(indata):
    sum = 0
    for rps in indata:
        sum = sum + rps.score_one()
    return sum

def part_two(indata):
    sum = 0
    for rps in indata:
        sum = sum + rps.score_two()
    return sum

def get_indata(filename):
    indata = []
    f = open(filename, 'r')
    for row in f:
        r = row.strip().split(" ")
        indata.append(RPS(r[0], r[1]))
    return indata

if __name__ == '__main__':
    main()
