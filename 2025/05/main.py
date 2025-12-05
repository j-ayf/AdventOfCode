# https://adventofcode.com/2025/day/5

def get_input():
    with open('puzzleInput.txt', 'r') as f:
        whole = f.read().rstrip().split('\n\n')
        first = whole[0].split('\n')
        second = whole[1].split('\n')
        return [first, second]


def main():
    puzzle_input = get_input()
    ranges = puzzle_input[0]
    item_ids = puzzle_input[1]

    print(f'Part1: {part1(ranges, item_ids)}')
    print(f'Part2: {part2()}')


def part1(ranges, item_ids):
    sum_spoiled = 0

    for item in item_ids:
        for str_range in ranges:
            int_range = get_range_ints(str_range)
            if is_in_range(int_range[0], int_range[1], item):
                sum_spoiled += 1
                break

    return sum_spoiled


def part2():
    return 0


def get_range_ints(str_range):
    """TODO: Comment function get_range_int"""
    nums = str_range.split('-')
    return [int(nums[0]), int(nums[1])]


def is_in_range(range_start, range_end, item_id):
    """TODO: Comment function is_in_range"""
    range_list = range(range_start, range_end + 1)
    if int(item_id) in range_list:
        return True
    return False



if __name__ == '__main__':
    main()