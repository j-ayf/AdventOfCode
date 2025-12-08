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


def get_operator_indices(puzzle_input):
    indices = []
    operator_line = puzzle_input[-1]
    for i in range(len(operator_line)):
        if operator_line[i] == ' ':
            continue
        indices.append(i)
    return indices


def main():
    print(f'Part1: {part1()}')
    print(f'Part2: {part2()}')


def part1():
    puzzle = split_part1(get_input())
    total = 0
    for i in range(len(puzzle[0])):
        nums = get_nums_part1(puzzle, i)
        total += solve_problem(nums, puzzle[-1][i])

    return total


def part2():
    puzzle = get_input()
    operator_indices = get_operator_indices(puzzle)
    total = 0
    for i in range(len(operator_indices)):
        try:
            problem_nums = get_nums_part2(puzzle, operator_indices[i], operator_indices[i+1])
        except IndexError:
            problem_nums = get_nums_part2(puzzle, operator_indices[i], None)

        total += solve_problem(problem_nums, puzzle[-1][operator_indices[i]])

    return total


def get_nums_part1(puzzle, index):
    nums = []
    for i in range(len(puzzle)-1):
        nums.append(int(puzzle[i][index]))
    return nums


def get_nums_part2(puzzle, current_index, next_index):
    if next_index:
        end_index = next_index-1
    else:
        end_index = len(puzzle[0])
    nums = []
    for i in range(current_index, end_index):
        num = ''
        for j in range(len(puzzle)-1):
            if puzzle[j][i] != ' ':
                num += puzzle[j][i]

        nums.append(int(num))

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