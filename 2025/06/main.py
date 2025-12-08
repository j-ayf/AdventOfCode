# https://adventofcode.com/2025/day/6
import math

def get_input():
    with open('puzzleInput.txt', 'r') as f:
        return f.read().rstrip().split('\n')


def split_part1(puzzle_input):
    lines = []
    for line in puzzle_input:
        lines.append(line.split())
    return lines


def main():
    print(f'Part1: {part1()}')
    print(f'Part2: {part2()}')


def part1():
    puzzle = split_part1(get_input())
    total = 0
    for i in range(len(puzzle[0])):
        nums = get_nums(puzzle, i)
        total += solve_problem(nums, puzzle[-1][i])

    return total


def part2():
    return 0


def get_nums(puzzle, index):
    nums = []
    for i in range(len(puzzle)-1):
        nums.append(int(puzzle[i][index]))
    return nums


def solve_problem(nums, operator):
    if operator == '+':
        return sum(nums)
    elif operator == '*':
        return math.prod(nums)
    else:
        raise Exception(f'Unknown operator {operator}')


if __name__ == '__main__':
    main()