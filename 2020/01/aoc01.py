#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser(description='AdventOfCode 2020 task 1')
parser.add_argument('-i', '--input', help='Indata file, default data.txt', default='data.txt')
args = parser.parse_args()

def main():
    print("--- ADVENT OF CODE 2020 DAY 1 ---")

    numbers = []

    f = open(args.input, 'r')

    for row in f:
        numbers.append(int(row.strip()))

    num1, num2 = get_two_matching_values(numbers)
    print("[{}][{}]".format(num1, num2))

    first_answer = -1
    if num1 == -1 and num2 == -1:
        print("Did not find any values that together summarizes to 2020!")
        exit(-1)
    else:
        first_answer = num1 * num2

    no1, no2, no3 = get_three_matching_values(numbers)
    print("[{}][{}][{}]".format(no1, no2, no3))

    second_answer = -1
    if no1 == -1 and no2 == -1 and no3 == -1:
        print("Did not find any values that together summarizes to 2020!")
        exit(-1)
    else:
        second_answer = no1 * no2 * no3

    print("PART1: The first answer is %d!" % first_answer)
    print("PART2: The second answer is %d!" % second_answer)

def get_two_matching_values(nos):
    for n1 in range(len(nos)-1):
        for n2 in range(n1+1, len(nos)):
            # print("n1: {}, n2: {}".format(nos[n1], nos[n2]))
            if nos[n1] + nos[n2] == 2020:
                return nos[n1], nos[n2]

    return -1, -1

def get_three_matching_values(nos):
    for n1 in range(len(nos)-2):
        for n2 in range(n1+1, len(nos)-1):
            for n3 in range(n2+1, len(nos)):
                #print("n1: {}, n2: {}, n3: {}".format(nos[n1], nos[n2], nos[n3]))
                if nos[n1] + nos[n2] + nos[n3] == 2020:
                    return nos[n1], nos[n2], nos[n3]

    return -1, -1, -1

if __name__ == '__main__':
    main()

