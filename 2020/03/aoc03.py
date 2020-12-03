#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser(description='AdventOfCode 2020 task 3')
parser.add_argument('-i', '--input', help='Indata file, default data.txt', default='data.txt')
args = parser.parse_args()

def main():
    print("--- ADVENT OF CODE 2020 DAY 3 ---")

    f = open(args.input, 'r')

    slopes = []
    for row in f:
        slopes.append(row.strip())

    part1 = [(3,1)]
    part2 = [(1,1), (3,1), (5,1), (7,1), (1,2)]

    first_answer = hit_the_slopes(slopes, part1[0][0], part1[0][1])

    second_answers = []
    for p in part2:
        second_answers.append(hit_the_slopes(slopes, p[0], p[1]))
    second_answer = multiply_list(second_answers)

    print("PART1: The number of trees encountered is %d!" % first_answer)
    print("PART2: The multiplicated number of encountered trees is %d!" % second_answer)

def hit_the_slopes(slope, r, d):
    p = t = rn = 0
    for h in slope:
        if rn % d == 0:
            if h[p % len(h)] == '#':
                t += 1
            p += r

        rn +=1

    return t

def multiply_list(l):
    r = 1
    for i in l:
        r = r * i
    return r

if __name__ == '__main__':
    main()

