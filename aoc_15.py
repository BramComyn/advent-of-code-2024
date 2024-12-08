#!/usr/bin/env python3

from aoc_util import read_antenna_map, borders_safe
from collections import defaultdict
from itertools import combinations
import re

target_regex = r"\d|[A-Z]|[a-z]"

def find_antennas(joined_grid, width):
    antennas = defaultdict(list)
    for match in re.finditer(target_regex, joined_grid):
        y, x = match.start() // width, match.start() % width
        antennas[match.group()].append((y, x))
    return antennas

def count_antinode_positions(input_file="data/24-aoc-15.in"):
    """
    >>> count_antinode_positions("test/24-aoc-15.test")
    14
    """    
    grid = read_antenna_map(input_file)
    height, width = len(grid), (0 if len(grid) <= 0 else len(grid[0]))
    joined_grid = ''.join(grid)

    antennas = find_antennas(joined_grid, width)

    anti_nodes = set()
    for positions in antennas.values():
        for position_pair in combinations(positions, 2):
            first_position, second_position = position_pair
            dy, dx = second_position[0] - first_position[0], second_position[1] - first_position[1]

            first_antinode_position = (first_position[0] - dy, first_position[1] - dx)
            if borders_safe(first_antinode_position, width, height):
                anti_nodes.add(first_antinode_position)

            second_antinode_position = (second_position[0] + dy, second_position[1] + dx)
            if borders_safe(second_antinode_position, width, height):
                anti_nodes.add(second_antinode_position)

    return len(anti_nodes)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    print(f"Total number of unique antinode positions:\n\t{count_antinode_positions()}")
