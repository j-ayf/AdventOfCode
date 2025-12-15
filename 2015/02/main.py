# https://adventofcode.com/2015/day/2

def get_input():
    with open('input.txt', 'r') as f:
        return f.read().rstrip().split('\n')

def main():
    puzzle = get_input()

    print(f'Part1: {part1(puzzle)}')
    print(f'Part2: {part2(puzzle)}')

def part1(puzzle):
    total = 0
    for present in puzzle:
        l, w, h = get_dimensions(present)
        total += get_total_area(l, w, h)
        total += get_smallest_area(l, w, h)
    return total


def part2(puzzle):
    total = 0
    for present in puzzle:
        l, w, h = get_dimensions(present)
        total += get_base_ribbon_length(l, w, h)
        total += l*w*h
    return total


def get_dimensions(dimensions):
    dims = dimensions.split('x')
    return int(dims[0]), int(dims[1]), int(dims[2])


def get_total_area(l, w, h):
    return 2*l*w + 2*w*h + 2*h*l


def get_smallest_area(l, w, h):
    areas = [l*w, w*h, h*l]
    return min(areas)


def get_base_ribbon_length(l, w, h):
    dims = [l, w, h]
    longest_i = dims.index(max(dims))
    if longest_i == 0:
        small_i = [1, 2]
    elif longest_i == 1:
        small_i = [0, 2]
    else:
        small_i = [0, 1]

    return 2*dims[small_i[0]] + 2*dims[small_i[1]]


if __name__ == '__main__':
    main()