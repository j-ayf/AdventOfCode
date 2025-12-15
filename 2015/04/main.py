# https://adventofcode.com/2015/day/2

def get_input():
    with open('input.txt', 'r') as f:
        return f.read().rstrip().split('\n')

def main():
    puzzle = get_input()
    print(puzzle)

    print(f'Part1: {part1(puzzle)}')
    print(f'Part2: {part2(puzzle)}')

def part1(puzzle):
    return 0


def part2(puzzle):
    return 0


if __name__ == '__main__':
    main()