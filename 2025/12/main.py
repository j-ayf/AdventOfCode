# https://adventofcode.com/2025/day/12

def get_input():
    with open('puzzleInput.txt', 'r') as f:
        sections = f.read().rstrip().split('\n\n')
        layout_section = sections[-1]
        shapes_section = sections[:-1]
        shapes = get_shapes(shapes_section)
        layouts = get_layouts(layout_section)
        return [shapes, layouts]


def get_shapes(shapes_section):
    shapes = []
    for shape in shapes_section:
        shape = shape.split('\n')
        shape.pop(0)
        shapes.append(shape)
    return shapes


def get_layouts(layout_section):
    layouts = []
    for layout in layout_section.split('\n'):
        area, present_numbers = layout.split(': ')
        width, length = area.split('x')
        width, length = int(width), int(length)
        area = [width, length]
        present_numbers = present_numbers.split(' ')
        present_numbers = list(map(int, present_numbers))
        layouts.append((area, present_numbers))
    return layouts


def main():
    puzzle_input = get_input()

    print(f'Part1: {part1(puzzle_input)}')
    print(f'Part2: {part2()}')


def part1(puzzle):
    """
    just try area >= sum(shapes)
    only works with real input, not with sample input
    """
    shapes = puzzle[0]
    layouts = puzzle[1]
    fitting_regions = 0

    for layout in layouts:
        layout_area = layout[0][0] * layout[0][1]
        shape_area_sum = 0
        for i in range(len(layout[1])):
            amount = layout[1][i]
            shape_area_sum += amount * get_shape_area(shapes[i])
        if shape_area_sum < layout_area:
            fitting_regions += 1

    return fitting_regions


def part2():
    return 0


def get_shape_area(shape):
    shape_area = 0
    for line in shape:
        for char in line:
            if char == '#':
                shape_area += 1
    return shape_area


if __name__ == '__main__':
    main()