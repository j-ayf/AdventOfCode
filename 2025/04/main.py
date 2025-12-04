# https://adventofcode.com/2025/day/4

def get_input():
    with open('puzzleInput.txt', 'r') as f:
        return f.read().rstrip().split('\n')


def main():
    puzzle_input = get_input()

    print(f'Part1: {part1(puzzle_input)}')
    print(f'Part2: {part2()}')


def part1(puzzle_input):
    sum_rolls = 0
    for i in range(len(puzzle_input)):
        if i-1 < 0:
            above = None
        else:
            above = puzzle_input[i-1]

        if i+1 >= len(puzzle_input):
            below = None
        else:
            below = puzzle_input[i+1]

        for j in range(len(puzzle_input[i])):
            if puzzle_input[i][j] == '.':
                continue

            adjacent_count = check_row(puzzle_input[i], above, below, j, len(puzzle_input[i]))
            if adjacent_count >= 4:
                continue
            else:
                sum_rolls += 1

    return sum_rolls


def part2():
    return 0


def check_row(row, above, below, roll_index, row_length):
    if roll_index == 0:
        left_index = None
    else:
        left_index = roll_index-1
    if roll_index >= row_length-1:
        right_index = None
    else:
        right_index = roll_index+1
    adjacent_count = 0
    if above:
        if left_index or left_index == 0:
            adjacent_count += check_spot(above[left_index])
        adjacent_count += check_spot(above[roll_index])
        if right_index:
            adjacent_count += check_spot(above[right_index])
    if left_index or left_index == 0:
        adjacent_count += check_spot(row[left_index])
    if right_index:
        adjacent_count += check_spot(row[right_index])
    if below:
        if left_index or left_index == 0:
            adjacent_count += check_spot(below[left_index])
        adjacent_count += check_spot(below[roll_index])
        if right_index:
            adjacent_count += check_spot(below[right_index])
    return adjacent_count

def check_spot(spot):
    if spot == '@':
        return 1
    return 0

if __name__ == '__main__':
    main()