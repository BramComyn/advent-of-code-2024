#!/usr/bin/env python3

from aoc_util import read_guard_path, borders_safe
from aoc_11 import start_indicators, directions, obstacle_indicator, update_direction

def find_guard_path(grid, width, height, position, direction_idx):
    """
    Same function as in aoc_11.py, but returns the visited positions instead of the number of unique positions
    """
    visited = set()

    while borders_safe(position, width, height):
        if position not in visited:
            visited.add(position)

        y, x = position
        dy, dx = directions[direction_idx]
        next_position = (y + dy, x + dx)

        while borders_safe(next_position, width, height) and grid[y + dy][x + dx] == obstacle_indicator:
            direction_idx = update_direction(direction_idx)
            dy, dx = directions[direction_idx]
            next_position = (y + dy, x + dx)

        position = next_position

    return visited


def find_loop(grid, width, height, position, direction_idx):
    visited = set()

    while borders_safe(position, width, height) and (position, direction_idx) not in visited:
        visited.add((position, direction_idx))

        y, x = position
        dy, dx = directions[direction_idx]
        next_position = (y + dy, x + dx)

        while borders_safe(next_position, width, height) and grid[y + dy][x + dx] == obstacle_indicator:
            direction_idx = update_direction(direction_idx)
            dy, dx = directions[direction_idx]
            next_position = (y + dy, x + dx)

        position = next_position

    return borders_safe(position, width, height)


def find_number_of_infinite_blockades(input_file="data/24-aoc-11.in"):
    """
    >>> find_number_of_infinite_blockades("test/24-aoc-11.test")
    6
    """
    grid = read_guard_path(input_file)
    height, width = len(grid), (0 if len(grid) <= 0 else len(grid[0]))

    joined_grid = "".join(grid) # used for finding the start_position
    start_position_idx = -1

    direction_idx = 0
    start_indicators_idx = 0
    while start_indicators_idx < len(start_indicators) and start_position_idx < 0:
        start_position_idx = joined_grid.find(start_indicators[start_indicators_idx])
        direction_idx = start_indicators_idx
        start_indicators_idx += 1

    start_position = start_position_idx // width, start_position_idx % width
    visited_positions = find_guard_path(grid, width, height, start_position, direction_idx)

    result = 0
    for position in visited_positions - { start_position }:
        y, x = position
        grid[y] = grid[y][:x] + obstacle_indicator + grid[y][x + 1:]

        result += find_loop(grid, width, height, start_position, direction_idx)
        grid[y] = grid[y][:x] + '.' + grid[y][x + 1:]

    return result

    
if __name__ == "__main__":
    import doctest
    doctest.testmod()

    print(f"Total number of looping blockades:\n\t{find_number_of_infinite_blockades()}")
