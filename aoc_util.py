#!/usr/bin/env python3

def __read_and_strip(input_file):
    with open(input_file, "r") as file:
        lines = [ line.strip() for line in file ]
    return lines


def borders_safe(position, width, height):
    p_height, p_width = position
    return 0 <= p_width < width and 0 <= p_height < height


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


def read_wordsearch(input_file="data/24-aoc-07.in"):
    return __read_and_strip(input_file)


def read_safety_manuals(input_file="data/24-aoc-09.in"):
    ordering_rules = []
    pages_to_produce = []

    switched = False

    with open(input_file, "r") as file:
        for line in file:

            if line.strip() == "":
                switched = True
                continue

            if not switched:
                ordering_rules.append(line)
            else:
                pages_to_produce.append(line)

    return ordering_rules, pages_to_produce


def read_guard_path(input_file="data/24-aoc-11.in"):
    return __read_and_strip(input_file)


def read_calibration_equations(input_file="data/24-aoc-13.in"):
    with open(input_file, "r") as file:
        equations = []

        for line in file:
            result, terms = line.strip().split(':')
            terms = terms.strip().split(' ')

            equations.append((int(result), [ int(term) for term in terms ]))

    return equations


def read_antenna_map(input_file="data/24-aoc-15.in"):
    return __read_and_strip(input_file)


def read_dense_disk_map(input_file="data/24-aoc-17.in"):
    with open(input_file, "r") as file:
        return ''.join(line.strip() for line in file)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
