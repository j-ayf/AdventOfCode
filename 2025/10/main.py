# https://adventofcode.com/2025/day/10


def get_input():
    with open('puzzleInput.txt', 'r') as f:
        lines = f.read().rstrip().split('\n')
        machines = []
        for line in lines:
            button_schematics = line.split()
            indicator_lights = sanitize_input(button_schematics[0])
            joltage = sanitize_input(button_schematics[-1])
            button_schematics.pop(0)
            button_schematics.pop(-1)
            button_schematics = sanitize_input(button_schematics)
            machines.append([indicator_lights, button_schematics, joltage])
        return machines


def sanitize_input(data):
    if isinstance(data, list):
        button_schem = []
        for schematic in data:
            schematic = strip_brackets(schematic)
            schematic = schematic.split(',')
            temp = []
            for num in schematic:
                temp.append(int(num))
            button_schem.append(temp)
        return button_schem
    elif ',' in data:
        data = strip_brackets(data)
        joltage = []
        data = data.split(',')
        for button in data:
            joltage.append(int(button))
        return joltage
    else:
        return strip_brackets(data)


def strip_brackets(string):
    string = string.lstrip('[({')
    string = string.rstrip('])}')
    return string


def main():
    puzzle_input = get_input()
    print(puzzle_input)  # todo: remove

    print(f'Part1: {part1()}')
    print(f'Part2: {part2()}')


def part1():
    return 0


def part2():
    return 0


if __name__ == '__main__':
    main()