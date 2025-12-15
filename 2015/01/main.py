# https://adventofcode.com/2015/day/1

def get_input():
    with open('input.txt', 'r') as f:
        return f.read().rstrip()

def main():
    puzzle = get_input()

    print(f'Part1: {part1(puzzle)}')
    print(f'Part2: {part2(puzzle)}')

def part1(puzzle):
    floor = 0
    floor += puzzle.count('(')
    floor -= puzzle.count(')')
    return floor


def part2(puzzle):
    floor = 0
    for i in range(len(puzzle)):
        if puzzle[i] == '(':
            floor += 1
        else:
            floor -= 1
        if floor < 0:
            return i+1


if __name__ == '__main__':
    main()