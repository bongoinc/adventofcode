#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser(description='AdventOfCode 2017 task 1')
parser.add_argument('-i', '--input', help='Indata file, default data.txt', default='data.txt')
args = parser.parse_args()

def main():
  print("--- ADVENT OF CODE 2017 DAY 1 ---")

  captcha = 0

  f = open(args.input, 'r')
  data = f.read()

  nums = list(data)

  length = len(nums)

#  print("LENGTH: %d" % length)

  for pos in range(0, length):
    if pos == length-1:
      captcha = calc_captcha(captcha, int(nums[pos]), int(nums[0]))
    else:
      captcha = calc_captcha(captcha, int(nums[pos]), int(nums[pos + 1]))

  print("PART1: The solution of the captcha is %d!" % captcha)

def calc_captcha(summary, val1, val2):
  if val1 == val2:
      return summary + val1

  return summary

if __name__ == '__main__':
    main()
