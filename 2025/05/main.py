# https://adventofcode.com/2025/day/5

def get_input():
    with open('puzzleInput.txt', 'r') as f:
        whole = f.read().rstrip().split('\n\n')
        first = whole[0].split('\n')
        second = whole[1].split('\n')
        return [first, second]


def main():
    ranges, item_ids = get_input()

    print(f'Part1: {part1(ranges, item_ids)}')
    print(f'Part2: {part2(ranges)}')


def part1(ranges, item_ids):
    sum_spoiled = 0

    for item in item_ids:
        for str_range in ranges:
            int_range = get_range_ints(str_range)
            if is_in_range(int_range[0], int_range[1], item):
                sum_spoiled += 1
                break

    return sum_spoiled


def part2(ranges):
    long_list = []
    for id_range in ranges:
        int_start, int_end = get_range_ints(id_range)
        int_end += 1
        if int_start in long_list and int_end in long_list:
            continue
        elif int_start not in long_list and int_end not in long_list:
            long_list.extend(range(int_start, int_end))
        elif int_start in long_list and int_end not in long_list:
            for num in range(int_start, int_end):
                if num not in long_list:
                    long_list.extend(range(num, int_end))
        elif int_start not in long_list and int_end in long_list:
            for num in range(int_start, int_end):
                if num not in long_list:
                    long_list.extend(range(num, int_end))
        else:
            raise Exception(f'wtf {id_range}')
    return len(long_list)


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


def from_internet(filename):
    from bisect import bisect
    with open(filename) as f:
        lines = f.readlines()
    ranges = []
    ingredients_ids = []
    step = 0
    for line in lines:
        line = line[:-1]
        if not line:
            step += 1
            continue
        if step == 0:
            start, end = map(int, line.split('-'))
            end += 1
            ix0 = bisect(ranges, start)
            ix1 = bisect(ranges, end)
            adding = []
            if ix0 % 2 == 0:
                adding.append(start)
            if ix1 % 2 == 0:
                adding.append(end)
            ranges = ranges[:ix0] + adding + ranges[ix1:]
        if step == 1:
            ingredients_ids.append(int(line))
    ans0 = 0
    for ingredient_id in ingredients_ids:
        ix = bisect(ranges, ingredient_id)
        if ix % 2:
            ans0 += 1
    ans1 = 0
    for ix in range(len(ranges)//2):
        ans1 += ranges[2 * ix + 1] - ranges[2 * ix]
    return (ans0, ans1)


if __name__ == '__main__':
    # main()
    print(from_internet('puzzleInput.txt'))