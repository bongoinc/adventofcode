#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser(description='AdventOfCode 2019 task 8')
parser.add_argument('-i', '--input', help='Indata file, default data.txt', default='data.txt')
parser.add_argument('-w', '--width', help='Image width', default=25)
parser.add_argument('-t', '--height', help='Image height', default=6)
args = parser.parse_args()


def main():
    print("--- ADVENT OF CODE 2019 DAY 8 ---")

    f = open(args.input, 'r')
    data = f.read()

    steps = int(args.height) * int(args.width)
    layers = [data[x:x + steps] for x in range(0, len(data), steps)]

    fewest = 1000000
    fewest_index = -1
    i = 0
    for l in layers:
        cnt = l.count('0')
        if cnt < fewest:
            fewest_index = i
            fewest = cnt
        i += 1
    first_answer = layers[fewest_index].count('2') * layers[fewest_index].count('1')

    pixels = []
    for i in range(0, steps):
        pixels.append(get_pixel_from_all_layers(layers, i))

    #  print('Pixels:', pixels)

    img = []
    for pixel in pixels:
        img.append(get_actual_pixel(pixel))

    print("PART1: The answer is %d!" % first_answer)
    print("PART2: The answer is...")
    print_image(img, int(args.width), int(args.height))


def print_image(i, w, h):
    for y in range(0, h):
        for x in range(0, w):
            print(i[h * y + x], end='')
        print('\n', end='')


def get_actual_pixel(pixel):
    for l in pixel:
        if l == '1':
            return ' '
        elif l == '0':
            return '#'
    return '#'


def get_pixel_from_all_layers(lyrs, pos):
    pixel = []
    for l in lyrs:
        pixel.append(l[pos])
    return pixel


if __name__ == '__main__':
    main()
