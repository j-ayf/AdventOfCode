# https://adventofcode.com/2025/day/8
import math


class JunctionBox:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f'X:{self.x},Y:{self.y},Z:{self.z}'


class Network:
    def __init__(self, box1, box2):
        self.boxes = [box1, box2]

    def __repr__(self):
        return f'{self.boxes}'


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

    print(f'Part1: {part1(puzzle_input)}')
    print(f'Part2: {part2()}')


def part1(boxes):
    networks = []
    for i in range(10):
        nearest_boxes = find_lowest_distance_boxes(boxes, networks)
        box1 = nearest_boxes[0]
        box2 = nearest_boxes[1]
        is_box1_in_network = is_in_any_network(box1, networks)
        is_box2_in_network = is_in_any_network(box2, networks)
        # check if they're already in any network
        if is_box1_in_network or is_box2_in_network:
            # if both are in a different network, move all boxes from second network to first and remove second network
            if is_box1_in_network and is_box2_in_network:
                box1_network_index = get_box_network(box1, networks)
                box2_network_index = get_box_network(box2, networks)
                combined_network = combine_networks(networks[box1_network_index], networks[box2_network_index])
                networks[box1_network_index] = combined_network
                networks.pop(box2_network_index)
            # if only one is in a network, add them to the existing network
            elif is_box1_in_network:
                box_network_index = get_box_network(box1, networks)
                networks[box_network_index].boxes.append(box2)
            elif is_box2_in_network:
                box_network_index = get_box_network(box2, networks)
                networks[box_network_index].boxes.append(box1)
        # if no, create new network
        else:
            networks.append(Network(box1, box2))
        i += 1

    for network in networks:
        print(len(network.boxes))  # todo
    return 0


def part2():
    return 0


def get_distance(box1, box2):
    """https://en.wikipedia.org/wiki/Euclidean_distance"""
    return math.sqrt((box1.x - box2.x)**2 + (box1.y - box2.y)**2 + (box1.z - box2.z)**2)


def find_lowest_distance_boxes(boxes, networks):
    lowest_distance = 9999999999999999999999999999999999999999999.0
    nearest_boxes = []
    for box1 in boxes:
        for box2 in boxes:
            distance = get_distance(box1, box2)
            if distance == 0 or is_in_same_network(box1, box2, networks):
                continue
            elif distance < lowest_distance:
                lowest_distance = distance
                nearest_boxes = [box1, box2]

    return nearest_boxes


def is_in_same_network(box1, box2, networks):
    for network in networks:
        if box1 in network.boxes and box2 in network.boxes:
            return True
    return False


def is_in_any_network(box, networks):
    for network in networks:
        if box in network.boxes:
            return True
    return False


def get_box_network(box, networks):
    for i in range(len(networks)):
        if box in networks[i].boxes:
            return i


def combine_networks(network1, network2):
    for box in network2.boxes:
        network1.boxes.append(box)
    return network1


if __name__ == '__main__':
    main()