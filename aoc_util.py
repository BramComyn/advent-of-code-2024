#!/usr/bin/env python3

def read_lists_01(input_file="data/24-aoc-01.in"):
    left_list = []
    right_list = []

    with open(input_file) as file:
        for line in file:
            values = line.split(' ')

            left_list.append(int(values[0]))
            right_list.append(int(values[-1]))

    left_list.sort()
    right_list.sort()

    return left_list, right_list


if __name__ == "__main__":
    import doctest
    doctest.testmod()
