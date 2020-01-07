#!/usr/bin/python

import argparse
from body import Body

parser = argparse.ArgumentParser(description='AdventOfCode 2019 task 6')
parser.add_argument('-i', '--input', help='Indata file, default data.txt', default='data.txt')
args = parser.parse_args()

total = 0

def main():
  global total
  print("--- ADVENT OF CODE 2019 DAY 6 ---")

  f = open(args.input, 'r')
  input = f.read()
  orbitList = input.split('\n')

  bodies = {}
  bodies["COM"] = Body()
  for orbit in orbitList:
    name = orbit.split(')')[1]
    bodies[name] = Body()

  for orbit in orbitList:
    o = orbit.split(')')
    outer = o[1]
    inner = o[0]
    bodies[outer].parent = bodies[inner]
    bodies[inner].addChild(bodies[outer])

  #Start counting the orbits from the COM, then output the reults
  countOrbits(bodies["COM"], 1)

  print("PART1: Total number of direct and indirect orbits is %d!" % total)

  #Part 2

  start = bodies["YOU"].parent
  end = bodies["SAN"].parent

  #Find the bodies between santa and the COM
  santaPath = [end]
  current = end
  while current != bodies["COM"]:
    current = current.parent
    santaPath.append(current)

  #Find the first body in santa's path to the COM, climbing up from YOU
  currentLength = 0
  current = start
  while not current in santaPath:
    current = current.parent
    currentLength += 1

  #Print the distance
  total = currentLength + santaPath.index(current)
  print("PART2: Minimal required orbital transfers to get from YOU to SAN is {}!".format(total))

#Count the number of direct and indirect orbits
def countOrbits(b, i):
	global total
	#Add to the total the number of children the current body has multiplied by how far it is from the centre of mass (to account for the indirect orbits)
	total += b.numChildren * i
	#Recursively count the number of orbits for the children
	for c in b.children:
		countOrbits(c, i+1)

if __name__ == '__main__':
    main()
