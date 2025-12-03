# https://adventofcode.com/2025/day/3

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
        reversed_bank = list(bank).copy()
        reversed_bank.reverse()
        index_1 = 0
        index_2 = 0
        max_num = 0
        for i in range(len(reversed_bank)):
            if i == 0: continue
            current_num = int(reversed_bank[i])
            if current_num >= max_num:
                max_num = current_num
                index_1 = i
        max_num = 0
        i = len(bank)-index_1
        while i < len(bank):
            current_num = int(bank[i])
            if current_num > max_num:
                max_num = current_num
                index_2 = i
            i += 1

        max_joltage += int(reversed_bank[index_1] + bank[index_2])

    return max_joltage


def part2():
    return 0


if __name__ == '__main__':
    main()