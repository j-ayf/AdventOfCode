# https://adventofcode.com/2015/day/6


class Light:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_on = False
        self.brightness = 0

    def on(self):
        self.is_on = True

    def off(self):
        self.is_on = False

    def toggle(self):
        if self.is_on:
            self.is_on = False
        else:
            self.is_on = True

    def increase_brightness(self, amount=1):
        self.brightness += amount

    def decrease_brightness(self):
        if self.brightness > 0:
            self.brightness -= 1

    def __repr__(self):
        return f'{self.x}, {self.y}, {self.is_on}'


def make_lights():
    lights = []
    for i in range(1000):
        row = []
        for j in range(1000):
            row.append(Light(j, i))
        lights.append(row)
    return lights


def get_input():
    with open('input.txt', 'r') as f:
        lines = f.read().rstrip().split('\n')
    instructions = []
    for line in lines:
        l = line.split(' through ')
        end = get_int_coords(l[-1])
        l = l[0].split()
        start = get_int_coords(l[-1])
        if len(l) == 3:
            instruction = l[1]
        else:
            instruction = l[0]

        instructions.append([instruction, start, end])
    return instructions


def get_int_coords(str_coords):
    str_coords = str_coords.split(',')
    return [int(str_coords[0]), int(str_coords[1])]


def main():
    puzzle = get_input()
    lights = make_lights()

    print(f'Part1: {part1(puzzle, lights)}')
    print(f'Part2: {part2(puzzle, lights)}')


def part1(puzzle, lights):
    for instruction in puzzle:
        start = instruction[1]
        end = instruction[2]
        for i in range(start[0], end[0]+1):
            for j in range(start[1], end[1]+1):
                light = lights[i][j]
                if instruction[0] == 'on':
                    light.on()
                if instruction[0] == 'off':
                    light.off()
                if instruction[0] == 'toggle':
                    light.toggle()

    total = 0
    for row in lights:
        for light in row:
            if light.is_on:
                total += 1
    return total


def part2(puzzle, lights):
    for instruction in puzzle:
        start = instruction[1]
        end = instruction[2]
        for i in range(start[0], end[0]+1):
            for j in range(start[1], end[1]+1):
                light = lights[i][j]
                if instruction[0] == 'on':
                    light.increase_brightness()
                if instruction[0] == 'off':
                    light.decrease_brightness()
                if instruction[0] == 'toggle':
                    light.increase_brightness(2)

    total_brightness = 0
    for row in lights:
        for light in row:
            total_brightness += light.brightness
    return total_brightness


if __name__ == '__main__':
    main()