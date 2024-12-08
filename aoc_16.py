#!/usr/bin/env python3

from aoc_util import read_antenna_map, borders_safe
from aoc_15 import target_regex, find_antennas
from collections import defaultdict
from itertools import combinations
import re

def count_harmonic_antinode_positions(input_file="data/24-aoc-15.in"):
    """
    >>> count_harmonic_antinode_positions("test/24-aoc-15.test")
    34
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

            first_antinode_position = first_position
            while borders_safe(first_antinode_position, width, height):
                anti_nodes.add(first_antinode_position)
                first_antinode_position = (first_antinode_position[0] - dy, first_antinode_position[1] - dx)

            second_antinode_position = second_position
            while borders_safe(second_antinode_position, width, height):
                anti_nodes.add(second_antinode_position)
                second_antinode_position = (second_antinode_position[0] + dy, second_antinode_position[1] + dx)

    return len(anti_nodes)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    print(f"Total number of unique harmonic antinode positions:\n\t{count_harmonic_antinode_positions()}")
