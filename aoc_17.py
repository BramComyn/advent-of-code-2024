#!/usr/bin/env python3

from aoc_util import read_dense_disk_map

def convert_dense_to_full_disk_map(dense_disk_map):
    full_disk_map = []

    idx = 0
    free = False
    while idx < len(dense_disk_map):
        full_disk_map += int(dense_disk_map[idx]) * ([ str(idx // 2) ] if not free else [ "." ])
        idx += 1
        free = not free

    return full_disk_map


def reorganize_disk_map(disk_map):
    """
    >>> reorganize_disk_map("00...111...2...333.44.5555.6666.777.888899")
    ['0', '0', '9', '9', '8', '1', '1', '1', '8', '8', '8', '2', '7', '7', '7', '3', '3', '3', '6', '4', '4', '6', '5', '5', '5', '5', '6', '6', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
    """
    disk_map = list(disk_map)
    left = 0
    right = len(disk_map) - 1

    while left < right:
        while disk_map[left] != '.':
            left += 1
        while disk_map[right] == '.':
            right -= 1

        if left >= right:
            break

        disk_map[left], disk_map[right] = disk_map[right], disk_map[left]

    return disk_map


def checksum(reorganized_disk_map):
    idx, factor, result = 0, 0, 0
    while idx < len(reorganized_disk_map):
        result += idx * (int(reorganized_disk_map[idx]) if reorganized_disk_map[idx] != '.' else 0)
        factor += reorganized_disk_map[idx] != '.'
        idx += 1

    return result


def find_checksum(input_file="data/24-aoc-17.in"):
    """
    >>> find_checksum("test/24-aoc-17.test")
    1928
    """
    dense_disk_map = read_dense_disk_map(input_file)
    full_disk_map = convert_dense_to_full_disk_map(dense_disk_map)
    reorganized_disk_map = reorganize_disk_map(full_disk_map)
    return checksum(reorganized_disk_map)
    

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    print(f"Total file checksum:\n\t{find_checksum()}")
