#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser(description='AdventOfCode 2020 task 6')
parser.add_argument('-i', '--input', help='Indata file, default data.txt', default='data.txt')
args = parser.parse_args()

def main():
    print('--- ADVENT OF CODE 2020 DAY 6 ---')
    group_answers = []
    i_group_answers = []
    answers = ""
    i_answers = []

    f = open(args.input, 'r')
    for row in f:
        r = row.strip()
        if len(r) == 0:
            group_answers.append(answers)
            i_group_answers.append(i_answers)
            answers = ""
            i_answers = []
        else:
            answers += r
            i_answers.append(r)
    group_answers.append(answers)
    i_group_answers.append(i_answers)

    first_answer = sum(get_list_of_unique_group_answer(group_answers))
    second_answer = sum(get_list_of_common_answers_for_all(i_group_answers))

    print('PART1: The sum of these counts are %d!' % first_answer)
    print('PART2: The sum of these counts are %d!' % second_answer)

def get_list_of_unique_group_answer(l):
    ul = []
    for a in l:
        ua = set()
        for c in a:
            ua.add(c)
        ul.append(len(list(ua)))
    return ul

def get_list_of_common_answers_for_all(l):
    cl = []
    for a in l:
        ca = set.intersection(*[set(list) for list in a])
        cl.append(len(list(ca)))
    return cl

if __name__ == '__main__':
    main()

