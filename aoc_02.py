#!/usr/bin/env python3

from aoc_util import read_lists_01

def find_total_similarity_score(input_file="data/24-aoc-01.in"):
    """
    >>> find_total_similarity_score("test/24-aoc-01.test")
    31
    """
    left_list, right_list = read_lists_01(input_file)
    total_similarity = sum(left * right_list.count(left) for left in left_list)
    return total_similarity

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    print(f"Total similarity is:\n\t{find_total_similarity_score()}")
