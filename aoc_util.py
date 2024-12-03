#!/usr/bin/env python3

def read_lists_01(input_file="data/24-aoc-01.in"):
    left_list = []
    right_list = []

    with open(input_file, "r") as file:
        for line in file:
            values = line.split(' ')

            left_list.append(int(values[0]))
            right_list.append(int(values[-1]))

    left_list.sort()
    right_list.sort()

    return left_list, right_list


def read_reports_03(input_file="data/24-aoc-03.in"):
    reports = []

    with open(input_file, "r") as file:
        for line in file:
            report = line.split(' ')
            reports.append([int(level) for level in report])

    return reports


def read_memory_muls(input_file="data/24-aoc-05.in"):
    with open(input_file, "r") as file:
        memory = "".join(file)
        
    return memory


if __name__ == "__main__":
    import doctest
    doctest.testmod()
