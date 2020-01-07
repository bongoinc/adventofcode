#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser(description='AdventOfCode 2019 task 2, part 2')
parser.add_argument('-i', '--input', help='Indata file, default data.txt', default='data.txt')
parser.add_argument('-g', '--goal', help='Goal', default='19690720')
args = parser.parse_args()

f = open(args.input, 'r')
data = f.read().split(',')
data = list(map(int, data))
origdata = data.copy()

def main():
  print('--- ADVENT OF CODE 2019 DAY 2, part 2 ---')
  global data

  for noun in range(100):
    for verb in range(100):
#      print('Noun: {}, Verb: {}'.format(noun, verb))
      data = list(origdata)
      data[1] = noun
      data[2] = verb
      pos = 0

      while True:
        cmd = get_value_at_position(pos)
        a = get_value_at_position(pos+1)
        b = get_value_at_position(pos+2)
        store = get_value_at_position(pos+3)
#        print('READING: {} {} {} {}'.format(cmd, a, b, store))
        if cmd == 1:
#          print('---> ADD: {} + {} => {}, store in {}'.format(get_value_at_position(a), get_value_at_position(b), get_value_at_position(a) + get_value_at_position(b), store))
          set_value_at_position(store, get_value_at_position(a) + get_value_at_position(b))
        elif cmd == 2:
#          print('---> MULTIPLY: {} * {} => {}, store in {}'.format(get_value_at_position(a), get_value_at_position(b), get_value_at_position(a) * get_value_at_position(b), store))
          set_value_at_position(store, get_value_at_position(a) * get_value_at_position(b))
        elif cmd == 99:
#          print('---> QUIT')
          break
        else:
#          print('###### ERROR: %s' % cmd)
          break
        pos += 4

      first_position = get_value_at_position(0)
      print('Noun: {}, Verb: {}, RESULT: {}'.format(noun, verb, first_position))
      if first_position == int(args.goal):
        print('PART2: Input needed to get the output {} is {}!'.format(args.goal, 100*noun+verb))
        exit(0)

#  print('PART2: Input needed to get the output {} is {}!'.format(args.goal, 100*noun+verb))

def reset_program():
  global data
  print('RESETTING')
  data = origdata.copy()

def int_code(noun, verb):
  global data

  data[1] = noun
  data[2] = verb
  pos = 0

  while True:
    cmd = get_value_at_position(pos)
    a = get_value_at_position(pos+1)
    b = get_value_at_position(pos+2)
    store = get_value_at_position(pos+3)
    print('READING: {} {} {} {}'.format(cmd, a, b, store))
    if cmd == 1:
      print('---> ADD: {} + {} => {}, store in {}'.format(get_value_at_position(a), get_value_at_position(b), get_value_at_position(a) + get_value_at_position(b), store))
      set_value_at_position(store, get_value_at_position(a) + get_value_at_position(b))
    elif cmd == 2:
      print('---> MULTIPLY: {} * {} => {}, store in {}'.format(get_value_at_position(a), get_value_at_position(b), get_value_at_position(a) * get_value_at_position(b), store))
      set_value_at_position(store, get_value_at_position(a) * get_value_at_position(b))
    elif cmd == 99:
      print('---> QUIT')
      break
    else:
      print('###### ERROR: %s' % cmd)
      break
    pos += 4

    print('RV: {}'.format(get_value_at_position(0)))
    return get_value_at_position(0)

def get_value_at_position(pos):
  global data
  return data[pos]

def set_value_at_position(i, val):
  global data
#  print('Saving value {} at pos {}'.format(val, i))
  data[i] = val

if __name__ == '__main__':
    main()
