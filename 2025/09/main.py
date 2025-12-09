# https://adventofcode.com/2025/day/9

def get_input():
    with open('puzzleInput.txt', 'r') as f:
        lines = f.read().rstrip().split('\n')
        coords = []
        for line in lines:
            coords.append([int(x) for x in line.split(',')])
        return coords


def main():
    puzzle_input = get_input()

    print(f'Part1: {part1(puzzle_input)}')
    print(f'Part2: {part2()}')


def part1(coords):
    largest_area = 0
    for corner1 in coords:
        for corner2 in coords:
            area = calc_area(corner1, corner2)
            if area > largest_area:
                largest_area = area

    return largest_area


def part2():
    return 0


def calc_area(corner1, corner2):
    x_coords = [corner1[0], corner2[0]]
    y_coords = [corner1[1], corner2[1]]
    side1 = max(x_coords) - min(x_coords) + 1
    side2 = max(y_coords) - min(y_coords) + 1
    return side1 * side2


if __name__ == '__main__':
    main()