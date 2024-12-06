#!/usr/bin/env python3

from aoc_util import read_guard_path
from aoc_07 import borders_safe

directions = [ (-1, 0), (0, 1), (1, 0), (0, -1) ]
start_indicators = [ '^', '>', 'v', '<' ]
obstacle_indicator = '#'


def update_direction(direction):
    return (direction + 1) % len(directions)


def find_guard_path(input_file="data/24-aoc-11.in"):
    """
    >>> find_guard_path("test/24-aoc-11.test")
    41
    """
    grid = read_guard_path(input_file)
    height, width = len(grid), (0 if len(grid) <= 0 else len(grid[0]))

    joined_grid = "".join(grid) # used for finding the start_position
    start_position_idx = -1
    visited = set()

    direction_idx = 0
    start_indicators_idx = 0
    while start_indicators_idx < len(start_indicators) and start_position_idx < 0:
        start_position_idx = joined_grid.find(start_indicators[start_indicators_idx])
        direction_idx = start_indicators_idx
        start_indicators_idx += 1

    position = start_position_idx // width, start_position_idx % width

    result = 0
    while borders_safe(position, width, height):
        if position not in visited:
            visited.add(position)
            result += 1

        y, x = position
        dy, dx = directions[direction_idx]
        next_position = (y + dy, x + dx)

        while borders_safe(next_position, width, height) and grid[y + dy][x + dx] == obstacle_indicator:
            direction_idx = update_direction(direction_idx)
            dy, dx = directions[direction_idx]
            next_position = (y + dy, x + dx)

        position = next_position

    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    print(f"Total number of independent positions visited:\n\t{find_guard_path()}")
