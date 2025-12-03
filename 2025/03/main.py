# https://adventofcode.com/2025/day/3
import itertools


def get_input():
    with open('puzzleInput.txt', 'r') as f:
        return f.read().rstrip().split('\n')


def main():
    puzzle_input = get_input()

    print(f'Part1: {part1(puzzle_input)}')
    print(f'Part2: {part2(puzzle_input)}')


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


def part2(puzzle_input):
    max_joltage = 0

    for bank in puzzle_input:
        joltage = ''
        bank_list = list(bank)
        remaining_digits = 12
        start_index = 0
        for i in range(len(bank)):
            if remaining_digits == 0:
                break
            if i < start_index:
                continue

            nums_to_check = []
            high_ind = len(bank_list)-remaining_digits+1 if len(bank_list)-remaining_digits+1 <= len(bank_list) else len(bank_list)
            for j in range(start_index, high_ind):
                nums_to_check.append(bank_list[j])
            high_num = max(nums_to_check)
            ind_num = nums_to_check.index(high_num) + start_index
            joltage += bank_list[ind_num]

            start_index = ind_num + 1
            remaining_digits -= 1
        max_joltage += int(joltage)

    return max_joltage


if __name__ == '__main__':
    main()