#!/usr/bin/env python3

from aoc_util import read_lists_01

def find_total_distance(input_file="data/24-aoc-01.in"):
    """
    >>> find_total_distance("test/24-aoc-01.test")
    11
    """
    left_list, right_list = read_lists_01(input_file)
    total_distance = sum(abs(left - right) for left, right in zip(left_list, right_list))
    return total_distance


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
    print(f"Total distance is:\n\t{find_total_distance()}")
