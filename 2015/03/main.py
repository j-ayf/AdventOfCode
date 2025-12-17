# https://adventofcode.com/2015/day/2

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
        current_coords =  get_new_coords(current_coords, direction)
        if str(current_coords) in delivered_presents:
            delivered_presents[str(current_coords)] += 1
        else:
            delivered_presents[str(current_coords)] = 1

    return len(delivered_presents)


def part2(puzzle):
    return 0


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



if __name__ == '__main__':
    main()