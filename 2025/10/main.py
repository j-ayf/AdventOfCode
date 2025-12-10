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
        data = strip_brackets(data)
        lights = []
        for light in data:
            if light == '#':
                lights.append(True)
            else:
                lights.append(False)
        return lights


def strip_brackets(string):
    string = string.lstrip('[({')
    string = string.rstrip('])}')
    return string


def main():
    puzzle_input = get_input()
    print(puzzle_input)  # todo: remove

    print(f'Part1: {part1(puzzle_input)}')
    print(f'Part2: {part2()}')


def part1(puzzle):
    sum_presses = 0
    for machine in puzzle:
        sum_presses += find_fewest_presses(machine)
    return sum_presses


def part2():
    return 0


def find_fewest_presses(machine):
    indicator_lights = machine[0]
    button_schematics = machine[1]
    fewest_presses = 99999999999
    indicator_lights = press_button(indicator_lights, button_schematics[1])

    return fewest_presses


def press_button(indicator_lights, button):
    for index in button:
        indicator_lights = toggle_light(indicator_lights, index)
    return indicator_lights


def toggle_light(indicator_lights, index):
    if indicator_lights[index]:
        indicator_lights[index] = False
    else:
        indicator_lights[index] = True
    return indicator_lights


if __name__ == '__main__':
    main()