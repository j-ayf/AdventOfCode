# https://adventofcode.com/2025/day/3
import itertools


def get_input():
    with open('puzzleInput.txt', 'r') as f:
        return f.read().rstrip().split('\n')


def main():
    puzzle_input = get_input()

    print(f'Part1: {part1(puzzle_input)}')
    print(f'Part2: {part2()}')


def part1(puzzle_input):
    max_joltage = 0
    for bank in puzzle_input:
        t = itertools.combinations(bank, 2)
        l = list(t)
        l.sort(reverse=True)
        num_str = ''
        for num in l[0]:
            num_str += num
        max_joltage += int(num_str)
    return max_joltage


def part2():
    return 0


if __name__ == '__main__':
    main()