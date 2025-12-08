# https://adventofcode.com/2025/day/7
import re

def get_input():
    with open('puzzleInput.txt', 'r') as f:
        return f.read().rstrip().split('\n')


def main():
    puzzle_input = get_input()

    print(f'Part1: {part1(puzzle_input)}')
    print(f'Part2: {part2()}')


def part1(puzzle):
    total_splits = 0
    beam_indexes = []
    for i in range(len(puzzle)):
        if i == 0:
            beam_indexes.append(puzzle[i].find('S'))
            continue
        splitter_indices = get_splitter_indices(puzzle[i])
        if splitter_indices:
            for splitter_i in splitter_indices:
                if splitter_i in beam_indexes:
                    beam_indexes.remove(splitter_i)
                    total_splits += 1
                    if splitter_i-1 not in beam_indexes:
                        beam_indexes.append(splitter_i-1)
                        beam_indexes.sort()
                    if splitter_i+1 not in beam_indexes:
                        beam_indexes.append(splitter_i+1)
                        beam_indexes.sort()

    return total_splits


def part2():
    return 0


def get_splitter_indices(line):
    indices = []
    for splitter in re.finditer(r'\^', line):
        indices.append(splitter.start())
    return indices

if __name__ == '__main__':
    main()