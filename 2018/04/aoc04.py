#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser(description='AdventOfCode 2018 task 4')
parser.add_argument('-i', '--input', help='Indata file, default data.txt', default='data.txt')
args = parser.parse_args()


def main():
    print("--- ADVENT OF CODE 2018 DAY 4 ---")

    times = []

    f = open(args.input, 'r')

    for row in f:
        times.append(row.strip())

    times.sort()

    for item in times:
        print(item)
    #  print("PART1: There are %d overlapping areas in the fabric!" % claim_matrix.get_amount_of_multiple_claims())


#  print("PART2: The only ID that doesnt overlap is %d!" % int(id))

if __name__ == '__main__':
    main()
