#!/usr/bin/env python3

from aoc_util import read_wordsearch

offsets = {
    "left":       [ (0, -i)  for i in range(1, 4) ],
    "up":         [ (-i, 0)  for i in range(1, 4) ],
    "right":      [ (0, i)   for i in range(1, 4) ],
    "down":       [ (i, 0)   for i in range(1, 4) ],
    "left_up":    [ (-i, -i) for i in range(1, 4) ],
    "left_down":  [ (i, -i)  for i in range(1, 4) ],
    "right_up":   [ (-i, i)  for i in range(1, 4) ],
    "right_down": [ (i, i)   for i in range(1, 4) ],
}

target_word = "XMAS"

def borders_safe(position, width, height):
    p_height, p_width = position
    return 0 <= p_width < width and 0 <= p_height < height

def find_char(line, target_char):
    return [ idx for idx, value in enumerate(line) if value == target_char ]

def count_valid_from(start_position, lines, width, height):
    row, col = start_position
    count = 0

    for values in offsets.values():
        positions = [ start_position ] + [ (row + i, col + j) for i, j in values ]
        if all(borders_safe(position, width, height) for position in positions):
            word = ''.join(lines[row][col] for row, col in positions)
            if word == target_word:
                count += 1
        
    return count

def find_word_count(input_file="data/24-aoc-07.in"):
    """
    >>> find_word_count("test/24-aoc-07.test")
    18
    """
    lines = read_wordsearch(input_file)

    height, width = len(lines), (0 if len(lines) <= 0 else len(lines[0]))
    positions = [ (line_idx, x_position) for line_idx, line in enumerate(lines) for x_position in find_char(line, 'X') ]
    result = sum(count_valid_from(position, lines, width, height) for position in positions)

    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    print(f"Total XMAS count:\n\t{find_word_count()}")
