#!/usr/bin/env python3

from aoc_util import read_reports_03

def is_safe(report):
    """
    >>> is_safe([7, 6, 4, 2, 1])
    True
    >>> is_safe([1, 2, 7, 8, 9])
    False
    >>> is_safe([9, 7, 6, 2, 1])
    False
    >>> is_safe([1, 3, 2, 4, 5])
    False
    >>> is_safe([8, 6, 4, 4, 1])
    False
    >>> is_safe([1, 3, 6, 7, 9])
    True
    """
    all_increasing = all(level <= next_level for level, next_level in zip(report, report[1:]))
    all_decreasing = all(level >= next_level for level, next_level in zip(report, report[1:]))
    within_bounds = all(1 <= abs(level - next_level) <= 3 for level, next_level in zip(report, report[1:]))

    return (all_increasing or all_decreasing) and within_bounds


def find_safe_reports(input_file="data/24-aoc-03.in"):
    """
    >>> find_safe_reports("test/24-aoc-03.test")
    2
    """
    reports = read_reports_03(input_file)
    safe_reports = sum(is_safe(report) for report in reports)
    return safe_reports

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    print(f"Total nr. of safe reports:\n\t{find_safe_reports()}")
