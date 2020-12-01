#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser(description='AdventOfCode 2019 task 2')
parser.add_argument('-i', '--input', help='Indata file, default data.txt', default='data.txt')
args = parser.parse_args()

f = open(args.input, 'r')
data = f.read().split(',')
data = list(map(int, data))


def main():
    print('--- ADVENT OF CODE 2019 DAY 2 ---')

    global data

    #  f = open(args.input, 'r')
    #  data = f.read().split(',')
    #  data = list(map(int, data))

    data[1] = 12
    data[2] = 2

    pos = 0
    while True:
        cmd = get_value_at_position(pos)
        a = get_value_at_position(pos + 1)
        b = get_value_at_position(pos + 2)
        store = get_value_at_position(pos + 3)
        #    print('READING: {} {} {} {}'.format(cmd, a, b, store))
        if cmd == 1:
            #      print('---> ADD: {} + {} => {}, store in {}'.format(get_value_at_position(a), get_value_at_position(b), get_value_at_position(a) + get_value_at_position(b), store))
            set_value_at_position(store, get_value_at_position(a) + get_value_at_position(b))
        elif cmd == 2:
            print('---> MULTIPLY: {} * {} => {}, store in {}'.format(get_value_at_position(a), get_value_at_position(b),
                                                                     get_value_at_position(a) * get_value_at_position(
                                                                         b), store))
            set_value_at_position(store, get_value_at_position(a) * get_value_at_position(b))
        elif cmd == 99:
            #      print('---> QUIT')
            break
        else:
            print('###### ERROR: %s' % cmd)
            break

        #    print('--------------------------------------------------------------------------')
        #    print(data)
        pos += 4

    print("PART1: Value left at position 0 is %d!" % get_value_at_position(0))


#  print("PART2: The first reoccuring frequency is {} after {} repeats!".format(second_answer, repeats))

def get_value_at_position(pos):
    global data
    return data[pos]


def set_value_at_position(i, val):
    global data
    print('Saving value {} at pos {}'.format(val, i))
    data[i] = val


if __name__ == '__main__':
    main()
