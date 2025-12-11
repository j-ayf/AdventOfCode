# https://adventofcode.com/2025/day/11

def get_input():
    with open('puzzleInput.txt', 'r') as f:
        lines = f.read().rstrip().split('\n')
        devices = []
        for line in lines:
            temp = line.split(': ')
            device = [temp[0], temp[1].split()]
            devices.append(device)
    return devices


def main():
    puzzle_input = get_input()

    # print(f'Part1: {part1(puzzle_input)}')
    print(f'Part2: {part2(puzzle_input)}')


def part1(devices):
    start_i = get_device_index(devices, 'you')
    find_paths_to_out1(devices, start_i)
    global paths1
    return paths1


def part2(devices):
    start_i = get_device_index(devices, 'svr')
    find_paths_to_out2(devices, start_i, False, False)
    global paths2
    return paths2


def get_device_index(devices, device_name):
    for device in devices:
        if device[0] == device_name:
            return devices.index(device)


def find_paths_to_out1(devices, current_index):
    device = devices[current_index]
    for output in device[1]:
        if output == 'out':
            global paths1
            paths1 += 1
            return
        new_index = get_device_index(devices, output)
        find_paths_to_out1(devices, new_index)


def find_paths_to_out2(devices, current_index, dac, fft):
    device = devices[current_index]
    for output in device[1]:
        if output == 'out' and dac and fft:
            global paths2
            paths2 += 1
            return
        elif output == 'out':
            return
        elif output == 'dac':
            dac = True
        elif output == 'fft':
            fft = True
        new_index = get_device_index(devices, output)
        find_paths_to_out2(devices, new_index, dac, fft)


if __name__ == '__main__':
    paths1 = 0
    paths2 = 0
    main()