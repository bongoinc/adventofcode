#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser(description='AdventOfCode 2020 task 9')


parser.add_argument('-i', '--input', help='Indata file, default data.txt', default='testdata.txt')
parser.add_argument('-p', '--preamble', help='Preamble, amount of numbers, default 25', default=5, type=int)
args = parser.parse_args()

def main():
    print('--- ADVENT OF CODE 2020 DAY 9 ---')
    numbers = []

    f = open(args.input, 'r')
    for row in f:
        numbers.append(int(row.strip()))

#    print(numbers)

    first_answer = part1(numbers)
    second_answer = -1

    print('PART1: The value in the accumulator is %d!' % first_answer)
    print('PART2: The sum of these counts are %d!' % second_answer)

def part1(nums):
    p = args.preamble
    for i in range(p, len(nums)-p):
        r = calc_sums(nums[i-p:i], nums[i])
        if r == None:
            return nums[i]
    
def calc_sums(sl, s):
#    print('sublist: {}, sum: {}'.format(sl, s))
    for i, n in enumerate(sl):
        #print('sl[{}]  n[{}]'.format(sl[i], n))
        if s-n in sl:
            return n
    return None

if __name__ == '__main__':
    main()
