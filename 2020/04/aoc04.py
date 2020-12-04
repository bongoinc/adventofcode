#!/usr/bin/python

import argparse
import re

parser = argparse.ArgumentParser(description='AdventOfCode 2020 task 4')
parser.add_argument('-i', '--input', help='Indata file, default data.txt', default='data.txt')
args = parser.parse_args()

REGEXP_HEIGHT = r"^(\d+)(cm|in)$"
REGEXP_PID = r'^[0-9]{9}$'
REGEXP_COLOR = r'^#[0-9a-f]{6}$'
VALID_COLORS = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def main():
    print('--- ADVENT OF CODE 2020 DAY 4 ---')
    passports = []
    pp = {}

    f = open(args.input, 'r')
    for row in f:
        r = row.strip()
        if len(r) == 0:
            passports.append(pp)
            pp = {}
        pp.update(parse_info(r))
    passports.append(pp)

    first_answer = 0
    second_answer = 0
    for ps in passports:
        print(ps)
        if (len(ps) == 8 and 'cid' in ps) or (len(ps) == 7 and 'cid' not in ps):
            first_answer += 1
            if check_int_value(ps['byr'], 1920, 2002) and \
                check_int_value(ps['iyr'], 2010, 2020) and \
                check_int_value(ps['eyr'], 2020, 2030) and \
                check_height(ps['hgt']) and \
                re.search(REGEXP_COLOR, ps['hcl']) and \
                ps['ecl'] in VALID_COLORS and \
                re.search(REGEXP_PID, ps['pid']):
                second_answer += 1

    print('PART1: The number of valid passports is %d!' % first_answer)
    print('PART2: The number of valid passports is %d!' % second_answer)

def check_int_value(val, l, u):
    try:
        v = int(val)
        if l <= v <= u:
            return True;
    except ValueError:
        pass
    return False

def check_height(val):
    m = re.findall(REGEXP_HEIGHT, val)
    if not m:
        return False
    v, u = m[0]
    if u == 'cm':
        return check_int_value(v, 150, 193)
    elif u == 'in':
        return check_int_value(v, 59, 76)
    return False

def parse_info(info):
    t = {}
    for i in info.split():
        kv = i.split(":")
        t[kv[0]] = kv[1]

    return t

if __name__ == '__main__':
    main()

