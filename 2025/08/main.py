# https://adventofcode.com/2025/day/8
import math


class JunctionBox:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f'X:{self.x},Y:{self.y},Z:{self.z}'

def get_input():
    with open('puzzleInput.txt', 'r') as f:
        lines = f.read().rstrip().split('\n')
        boxes = []
        for line in lines:
            coords = line.split(',')
            boxes.append(JunctionBox(int(coords[0]), int(coords[1]), int(coords[2])))
        return boxes


def main():
    puzzle_input = get_input()
    print(puzzle_input)  # todo
    print(get_distance(puzzle_input[0], puzzle_input[0]))  # todo

    print(f'Part1: {part1(puzzle_input)}')
    print(f'Part2: {part2()}')


def part1(boxes):
    for box in boxes:
        lowest_distance = 9999999999999999999999999999999999999999999.0
        for box2 in boxes:
            distance = get_distance(box, box2)
            if distance == 0:
                continue
            elif distance < lowest_distance:
                lowest_distance = distance
        print(lowest_distance)  # todo
    return 0


def part2():
    return 0


def get_distance(box1, box2):
    """https://en.wikipedia.org/wiki/Euclidean_distance"""
    return math.sqrt((box1.x - box2.x)**2 + (box1.y - box2.y)**2 + (box1.z - box2.z)**2)


if __name__ == '__main__':
    main()