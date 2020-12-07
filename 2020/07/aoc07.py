#!/usr/bin/python

import argparse
from bag import Bag

parser = argparse.ArgumentParser(description='AdventOfCode 2020 task 7')
parser.add_argument('-i', '--input', help='Indata file, default data.txt', default='testdata.txt')
args = parser.parse_args()

BAGS_CONTAINED = 'bags contain'

def main():
    print('--- ADVENT OF CODE 2020 DAY 7 ---')
    rules = []
    bags = []

    f = open(args.input, 'r')
    for row in f:
        rules.append(row.strip())
    print(rules)

    for r in rules:
        bags.append(decode_rule(r))
    print(bags)

    first_answer = count_bags_that_might_contain_shiny_gold(bags)
    second_answer = -1

    print('PART1: The sum of these counts are %d!' % first_answer)
    print('PART2: The sum of these counts are %d!' % second_answer)

def count_bags_that_might_contain_shiny_gold(all_bags):
    cnt = 0
    for b in all_bags:
        if b.has_shiny_gold_bag():
            cnt += 1
#        elif b.contain_other_bags():
    return cnt

def decode_rule(rule):
    idx = rule.index(BAGS_CONTAINED)
    color = rule[0:idx].strip()
    b = Bag(color)
    if rule.endswith('no other bags.') == False:
        contains = rule[idx + len(BAGS_CONTAINED):].strip().split(',')
        for contain in contains:
            c, n = decode_sub_colors(contain.strip())
            b.add_contained_bag(c, n)
    return b

def decode_sub_colors(sc):
    n = int(sc[0:1].strip())
    c = sc[2:sc.index('bag')].strip()
    return c, n

if __name__ == '__main__':
    main()
