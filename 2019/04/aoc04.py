#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser(description='AdventOfCode 2019 task 4')
parser.add_argument('-s', '--start', help='Start value, default 168630', default='168630')
parser.add_argument('-e', '--end', help='End value, default 718098', default='718098')
args = parser.parse_args()


def main():
    print("--- ADVENT OF CODE 2019 DAY 4 ---")

    matches1 = []
    matches2 = []
    for password in range(int(args.start), int(args.end)):
        if is_only_increasing(password):
            if has_adjacent_numbers(password):
                matches1.append(password)

            if has_one_group_of_adjacent_numbers(password):
                #        print('Found a possible password: {}'.format(password))
                matches2.append(password)
    #    if has_adjacent_numbers(password) and is_only_increasing(password):
    #      matches1.append(password)
    #      if has_one_group_of_adjacent_numbers(password):
    #        print('Found a possible password: {}'.format(password))
    #       matches2.append(password)

    #  print('Missing values in second list: ', (set(matches1).difference(matches2)))

    print('PART1: Number of possible passwords: {}'.format(len(matches1)))
    print('PART2: Number of possible passwords: {}'.format(len(matches2)))


def has_adjacent_numbers(num):
    s = str(num)
    for n in range(len(s) - 1):
        if s[n] == s[n + 1]:
            return True
    return False


def is_only_increasing(num):
    s = str(num)
    for n in range(len(s) - 1):
        if int(s[n]) > int(s[n + 1]):
            return False
    return True


def has_one_group_of_adjacent_numbers(num):
    s = str(num)
    for i in range(1, 10):
        #    print(i)
        if s.count(str(i)) == 2:
            return True
    return False


if __name__ == '__main__':
    main()
