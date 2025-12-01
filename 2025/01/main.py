# https://adventofcode.com/2025/day/1

def get_input():
    with open('puzzleInput.txt', 'r') as f:
        return f.read().rstrip().split('\n')

def main():
    puzzle_input = get_input()
    dial = list(range(100))
    current_position = 50

    print(f'Zeros: {part1(puzzle_input, dial, current_position)}')
    print(f'Zeros: {part2()}')

def part1(puzzle_input, dial, current_position):
    zero_counter = 0
    for turn in puzzle_input:
        current_position += get_direction(turn)
        while current_position >= len(dial):
            current_position -= len(dial)
        while current_position < 0:
            current_position += len(dial)

        # print(current_position, get_direction(turn))
        if dial[current_position] == 0:
            zero_counter += 1

    return zero_counter


def part2():
    from itertools import accumulate as acc

    a, b = [50], [50]

    for line in open('puzzleInput.txt'):
        dir = {'L': -1, 'R': +1}[line[0]]
        dist = int(line[1:])
        a += [dir * dist]
        b += [dir] * dist

    for x in a, b:
        print(sum(x % 100 == 0 for x in acc(x)))


def get_direction(turn):
    num = int(turn.lstrip('LR'))
    if turn[0] == 'R':
        return num
    elif turn[0] == 'L':
        return -num
    else:
        print('error')
        exit(1)


if __name__ == '__main__':
    main()