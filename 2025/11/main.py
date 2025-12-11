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

    print(f'Part1: {part1(puzzle_input)}')
    print(f'Part2: {part2()}')


def part1(devices):
    start_i = get_device_index(devices, 'you')
    find_paths_to_out(devices, start_i)
    global paths
    return paths


def part2():
    return 0


def get_device_index(devices, device_name):
    for device in devices:
        if device[0] == device_name:
            return devices.index(device)


def find_paths_to_out(devices, current_index):
    device = devices[current_index]
    for output in device[1]:
        if output == 'out':
            global paths
            paths += 1
            return
        new_index = get_device_index(devices, output)
        find_paths_to_out(devices, new_index)


if __name__ == '__main__':
    paths = 0
    main()