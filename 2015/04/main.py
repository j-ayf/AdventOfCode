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
    i = 0
    while True:
        s = f'{puzzle}{i}'
        h = hashlib.md5(s.encode()).hexdigest()
        if re.search(r"^0{5}\w+", h):
            return i
        i += 1


def part2(puzzle):
    return 0


if __name__ == '__main__':
    main()