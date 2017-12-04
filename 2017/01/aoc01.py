#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser(description='AdventOfCode 2017 task 1')
parser.add_argument('-i', '--input', help='Indata file, default data.txt', default='data.txt')
args = parser.parse_args()

def main():
  print("--- ADVENT OF CODE 2017 DAY 1 ---")

  captcha1 = 0
  captcha2 = 0

  f = open(args.input, 'r')
  data = f.read()
  nums = list(data)

  for i, val in enumerate(nums):
    if i == len(nums)-1:
      captcha1 = calc_captcha(captcha1, nums[i], nums[0])
    else:
      captcha1 = calc_captcha(captcha1, nums[i], nums[i + 1])

  for pos in range(0, len(nums)/2):
    captcha2 = calc_captcha(captcha2, nums[pos], nums[pos + (len(nums)/2)])

  captcha2 = 2*captcha2

  print("PART1: The solution of this captcha is %d!" % captcha1)
  print("PART2: The solution of this captcha is %d!" % captcha2)

def calc_captcha(summary, val1, val2):
  if val1 == val2:
      return summary + int(val1)

  return summary

if __name__ == '__main__':
    main()
