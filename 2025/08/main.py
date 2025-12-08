# https://adventofcode.com/2025/day/8

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
    print(puzzle_input)

    print(f'Part1: {part1()}')
    print(f'Part2: {part2()}')


def part1():
    return 0


def part2():
    return 0


class JunctionBox:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f'X:{self.x},Y:{self.y},Z:{self.z}'


if __name__ == '__main__':
    main()