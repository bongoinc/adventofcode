#!/usr/bin/python

import argparse
from operand import Operand

parser = argparse.ArgumentParser(description='AdventOfCode 2020 task 8')
parser.add_argument('-i', '--input', help='Indata file, default data.txt', default='testdata.txt')
args = parser.parse_args()

def main():
    print('--- ADVENT OF CODE 2020 DAY 8 ---')
    operands = []

    f = open(args.input, 'r')
    for row in f:
        o = Operand()
        o.decode(row.strip())
        operands.append(o)

#    print(operands)

    first_answer = part1(operands)
    second_answer = -1

    print('PART1: The value in the accumulator is %d!' % first_answer)
    print('PART2: The sum of these counts are %d!' % second_answer)

def part1(ops):
    positions = []
    pos = 0
    accumulator = 0
    while pos not in positions:
        positions.append(pos)
        op = ops[pos]
        if op.get_action() == 'acc':
            accumulator += op.get_steps()
            pos += 1
        elif op.get_action() == 'jmp':
            pos += op.get_steps()
        elif op.get_action() == 'nop':
            pos += 1

    return accumulator


if __name__ == '__main__':
    main()
