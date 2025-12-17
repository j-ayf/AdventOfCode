# https://adventofcode.com/2015/day/4
import hashlib
import re

def get_input():
    with open('input.txt', 'r') as f:
        return f.read().rstrip()

def main():
    puzzle = get_input()

    print(f'Part1: {part1(puzzle)}')
    print(f'Part2: {part2(puzzle)}')

def part1(puzzle):
    return get_advent_coin(puzzle, 5)


def part2(puzzle):
    return get_advent_coin(puzzle, 6)


def get_advent_coin(puzzle, leading_zeroes):
    i = 0
    while True:
        s = f'{puzzle}{i}'
        h = hashlib.md5(s.encode()).hexdigest()
        regex = r'^0{' + re.escape(str(leading_zeroes)) + r'}\w+'
        if re.search(regex, h):
            return i
        i += 1

if __name__ == '__main__':
    main()