# https://adventofcode.com/2015/day/1

def get_input():
    with open('input.txt', 'r') as f:
        return f.read().rstrip()

def main():
    puzzle = get_input()

    print(f'Part1: {part1(puzzle)}')
    print(f'Part2: {part2()}')

def part1(puzzle):
    floor = 0
    floor += puzzle.count('(')
    floor -= puzzle.count(')')
    return floor


def part2():
    return 0


if __name__ == '__main__':
    main()