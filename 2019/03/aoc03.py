#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser(description='AdventOfCode 2019 task 1')
parser.add_argument('-i', '--input', help='Indata file, default data.txt', default='data.txt')
args = parser.parse_args()

def main():
  print("--- ADVENT OF CODE 2019 DAY 1 ---")

  f = open(args.input, 'r')

  wires = []

  for row in f:
    wire = []
    x = 1
    y = 1
    w = row.split(',')
#    print(w)
#    print('X: {}, Y: {}'.format(x, y))
    for p in w:
      d = p[0]
      l = int(p[1:])
#      print('DIR: {}, LEN: {}'.format(d, l))
      if d == 'U':
#        t = []
        for dy in range(y, y+l+1):
#          t.append(dy)
          wire.append('{},{}'.format(x,dy))
#        print(t)
        y += l
      elif d == 'D':
#        t = []
        for dy in range(y, y-l-1, -1):
#          t.append(dy)
          wire.append('{},{}'.format(x,dy))
#        print(t)
        y -= l
      elif d == 'R':
#        t = []
        for dx in range(x, x+l+1):
#          t.append(dx)
          wire.append('{},{}'.format(dx,y))
#        print(t)
        x += l
      elif d == 'L':
#        t = []
        for dx in range(x, x-l-1, -1):
#          t.append(dx)
          wire.append('{},{}'.format(dx,y))
#        print(t)
        x -= l
      
#      print('X: {}, Y: {}'.format(x, y))

    wires.append(wire)

#  print('W1:', wires[0])
#  print('W2:', wires[1])

  intersections = set(wires[0]).intersection(wires[1])
  intersections.remove('1,1')
#  print('INTERSECTIONS:', intersections)

  shortest = -1
  for i in intersections:
    p = i.split(',')
    ti = get_distance(int(p[0]), int(p[1]))
    if shortest == -1 or ti < shortest:
      shortest = ti

  print("PART1: The shortest path is %d!" % shortest)

  wires[0].remove('1,1')
  wires[1].remove('1,1')
  distances = []
  for i in intersections:
#    print('D1: {}, D2: {}'.format(wires[0].index(i), wires[1].index(i)))
    distances.append(wires[0].index(i)+wires[1].index(i)+2)

#  print('Distances:', distances)
  print("PART2: Fewest combined steps to an intersection is {}!".format(min(distances)))

def get_distance(x, y):
  return abs((1-x)) + abs((1-y))

if __name__ == '__main__':
    main()
