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
    print(f'Part2: {part2(puzzle_input)}')


def part1(coords):
    largest_area = 0
    for corner1 in coords:
        for corner2 in coords:
            area = calc_area(corner1, corner2)
            if area > largest_area:
                largest_area = area

    return largest_area


def part2(coords):
    largest_area = 0
    for corner1 in coords:
        for corner2 in coords:
            if corner1 == corner2:
                continue
            is_valid = False
            # add validation
            if is_valid:
                area = calc_area(corner1, corner2)
                if area > largest_area:
                    largest_area = area
    return largest_area


def calc_area(corner1, corner2):
    x_coords = [corner1[0], corner2[0]]
    y_coords = [corner1[1], corner2[1]]
    side1 = max(x_coords) - min(x_coords) + 1
    side2 = max(y_coords) - min(y_coords) + 1
    return side1 * side2


def is_point_in_rectangle(corner1, corner2, point):
    if point == corner1 or point == corner2:
        return False
    x_coords = [min([corner1[0], corner2[0]]), max([corner1[0], corner2[0]])]
    y_coords = [min([corner1[1], corner2[1]]), max([corner1[1], corner2[1]])]
    return x_coords[0] < point[0] < x_coords[1] and y_coords[0] < point[1] < y_coords[1]


if __name__ == '__main__':
    main()