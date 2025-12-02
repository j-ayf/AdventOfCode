# https://adventofcode.com/2025/day/2
import re

def get_input():
    with open('puzzleInput.txt', 'r') as f:
        return f.read().rstrip().split(',')


def main():
    puzzle_input = get_nums(get_input())

    print(f'Part1: {part1(puzzle_input)}')
    print(f'Part2: {part2(puzzle_input)}')


def get_nums(ranges):
    new_ranges = []
    for num_range in ranges:
        temp = num_range.split('-')
        temp[0] = int(temp[0])
        temp[1] = int(temp[1])
        new_ranges.append(temp)

    return new_ranges


def part1(ranges):
    return run_regex(ranges, r'^(?P<number>\d+)(?P=number)$')


def part2(ranges):
    return run_regex(ranges, r'^(?P<number>\d+)(?P=number)+$')


def run_regex(ranges, regex):
    sum_ids = 0
    regex = regex
    for num_range in ranges:
        for i in range(num_range[0], num_range[1] + 1):
            if re.search(regex, str(i)):
                sum_ids += i

    return sum_ids


if __name__ == '__main__':
    main()