# https://adventofcode.com/2015/day/3

def get_input():
    with open('input.txt', 'r') as f:
        return f.read().rstrip()

def main():
    puzzle = get_input()

    print(f'Part1: {part1(puzzle)}')
    print(f'Part2: {part2(puzzle)}')

def part1(puzzle):
    current_coords = [0,0]
    delivered_presents = {str(current_coords): 1}
    for direction in puzzle:
        delivered_presents, current_coords = deliver_presents(current_coords, direction, delivered_presents)

    return len(delivered_presents)


def part2(puzzle):
    santa_coords = [0, 0]
    robot_coords = [0, 0]
    delivered_presents = {str(santa_coords): 2}
    for i in range(len(puzzle)):
        if i % 2 == 0:
            # santa
            delivered_presents, santa_coords = deliver_presents(santa_coords, puzzle[i], delivered_presents)
        else:
            # robot
            delivered_presents, robot_coords = deliver_presents(robot_coords, puzzle[i], delivered_presents)

    return len(delivered_presents)


def get_new_coords(current_coords, direction):
    if direction == '^':
        return [current_coords[0], current_coords[1]+1]
    elif direction == '>':
        return [current_coords[0]+1, current_coords[1]]
    elif direction == 'v':
        return [current_coords[0], current_coords[1]-1]
    elif direction == '<':
        return [current_coords[0]-1, current_coords[1]]
    else:
        raise Exception(f'Invalid direction "{direction}"')


def deliver_presents(current_coords, direction, delivered_presents):
    current_coords = get_new_coords(current_coords, direction)
    if str(current_coords) in delivered_presents:
        delivered_presents[str(current_coords)] += 1
    else:
        delivered_presents[str(current_coords)] = 1

    return delivered_presents, current_coords



if __name__ == '__main__':
    main()