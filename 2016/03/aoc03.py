#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser(description='AdventOfCode 2016 task 3')
parser.add_argument('-i', '--input', help='Indata file, default data.txt', default='data.txt')
args = parser.parse_args()

def main():
  print("--- ADVENT OF CODE 2016 DAY 3 ---")

  correct_triangles = 0

  f = open(args.input, 'r')

  for triangle in f:
    s1 = triangle[:5].strip()
    s2 = triangle[5:10].strip()
    s3 = triangle[10:].strip()

    if is_a_working_triangle(int(s1), int(s2), int(s3)) == True:
      correct_triangles += 1

  print("PART1: The are %d possible triangles in the input!" % correct_triangles)

def is_a_working_triangle(s1, s2, s3):

  if s1 + s2 <= s3 or s1 + s3 <= s2 or s2 + s3 <= s1:
    return False

  return True

if __name__ == '__main__':
    main()
