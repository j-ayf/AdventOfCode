# https://adventofcode.com/2015/day/5
import re


def get_input():
    with open('input.txt', 'r') as f:
        return f.read().rstrip().split('\n')

def main():
    puzzle = get_input()

    print(f'Part1: {part1(puzzle)}')
    print(f'Part2: {part2(puzzle)}')

def part1(puzzle):
    nice_strings = 0
    for s in puzzle:
        vowels = re.findall(r'[aeiou]', s)
        double = re.search(r'(?P<double>\w)(?P=double)', s)
        bad = re.search(r'ab|cd|pq|xy', s)
        if bad:
            continue
        if double and len(vowels) >= 3:
            nice_strings += 1

    return nice_strings


def part2(puzzle):
    nice_strings = 0
    for s in puzzle:
        pairs = re.search(r'(?P<pair>\w{2}).*(?P=pair)', s)
        repeat = re.search(r'(?P<repeat>\w)\w(?P=repeat)', s)
        if pairs and repeat:
            nice_strings += 1
    return nice_strings


if __name__ == '__main__':
    main()