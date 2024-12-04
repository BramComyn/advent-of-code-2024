#!/usr/bin/env python3

from aoc_util import read_wordsearch
from aoc_07 import find_char, offsets, borders_safe

pattern_offsets = {
    "left_up": offsets["left_up"][0],
    "left_down": offsets["left_down"][0],
    "right_up": offsets["right_up"][0], 
    "right_down": offsets["right_down"][0]
}

directions = ["left_up", "right_down", "right_up", "left_down"]

valid_patterns = [
    "MSMS", "SMMS", "MSSM", "SMSM"
]

def count_valid_from(start_position, lines, width, height):
    row, col = start_position
    count = 0

    positions = { "start": start_position }
    for key, value in pattern_offsets.items():
        i, j = value
        positions[key] = (row + i, col + j)

    if all(borders_safe(position, width, height) for position in positions.values()):
        pattern = ''.join(lines[positions[offset][0]][positions[offset][1]] for offset in directions)
        if pattern in valid_patterns:
            count += 1

    return count


def find_pattern_count(input_file="data/24-aoc-07.in"):
    """
    >>> find_pattern_count("test/24-aoc-07.test")
    9
    """
    lines = read_wordsearch(input_file)

    height, width = len(lines), (0 if len(lines) <= 0 else len(lines[0]))
    positions = [ (line_idx, a_position) for line_idx, line in enumerate(lines) for a_position in find_char(line, 'A') ]
    result = sum(count_valid_from(position, lines, width, height) for position in positions)

    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    print(f"Total X-MAS pattern count:\n\t{find_pattern_count()}")
