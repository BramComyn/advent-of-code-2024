#!/usr/bin/env python3

from aoc_17 import convert_dense_to_full_disk_map, checksum
from aoc_util import read_dense_disk_map

def reorganize_disk_map_whole_files(disk_map):
    """
    >>> reorganize_disk_map_whole_files("00...111...2...333.44.5555.6666.777.888899")
    ['0', '0', '9', '9', '2', '1', '1', '1', '7', '7', '7', '.', '4', '4', '.', '3', '3', '3', '.', '.', '.', '.', '5', '5', '5', '5', '.', '6', '6', '6', '6', '.', '.', '.', '.', '.', '8', '8', '8', '8', '.', '.']
    """
    disk_map = list(disk_map)
    right = len(disk_map) - 1

    left = 0
    while left < right:
        file_size = 0
        while right >= 0 and disk_map[right] == '.':
            right -= 1

        if right >= 0:
            file_id = disk_map[right]
            while right >= 0 and disk_map[right] == file_id:
                file_size += 1
                right -= 1

        free_size = 0
        enough_space = False
        while not enough_space and left < right:
            while left < right and disk_map[left] != '.':
                left += 1

            if disk_map[left] == '.' and left < right:
                while left < right and disk_map[left] == '.' and free_size < file_size:
                    free_size += 1
                    left += 1

                if free_size == file_size:
                    enough_space = True
                elif left < right and disk_map[left] != '.':
                    free_size = 0

        if enough_space:
            disk_map = disk_map[:left - file_size] + disk_map[right + 1:right + file_size + 1] + disk_map[left:right + 1] + disk_map[left - file_size:left] + disk_map[right + file_size + 1:]
        left = 0

    return disk_map


def find_whole_file_checksum(input_file="data/24-aoc-17.in"):
    """
    >>> find_whole_file_checksum("test/24-aoc-17.test")
    2858
    """
    dense_disk_map = read_dense_disk_map(input_file)
    full_disk_map = convert_dense_to_full_disk_map(dense_disk_map)
    reorganized_disk_map = reorganize_disk_map_whole_files(full_disk_map)
    return checksum(reorganized_disk_map)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    print(f"Total whole file-swapping checksum:\n\t{find_whole_file_checksum()}")
