# https://adventofcode.com/2025/day/2

def get_input():
    with open('puzzleInput.txt', 'r') as f:
        return f.read().rstrip().split(',')


def main():
    puzzle_input = get_nums(get_input())

    print(f'Part1: {part1(puzzle_input)}')
    print(f'Part2: {part2()}')


def get_nums(ranges):
    new_ranges = []
    for num_range in ranges:
        temp = num_range.split('-')
        temp[0] = int(temp[0])
        temp[1] = int(temp[1])
        new_ranges.append(temp)

    return new_ranges


def part1(ranges):
    sum_ids = 0
    for num_range in ranges:
        for i in range(num_range[0], num_range[1]+1):
            j = str(i)
            if len(j) % 2 != 0:
                continue
            half_len = int(len(j)/2)
            first = j[:half_len]
            second = j[half_len:]
            if first == second:
                sum_ids += i

    return sum_ids


def part2():
    return 0


if __name__ == '__main__':
    main()