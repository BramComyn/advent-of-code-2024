#!/usr/bin/env python3

from aoc_util import read_reports_03
from aoc_03 import is_safe

def is_almost_safe(report):
    """
    >>> is_almost_safe([7, 6, 4, 2, 1])
    True
    >>> is_almost_safe([1, 2, 7, 8, 9])
    False
    >>> is_almost_safe([9, 7, 6, 2, 1])
    False
    >>> is_almost_safe([1, 3, 2, 4, 5])
    True
    >>> is_almost_safe([8, 6, 4, 4, 1])
    True
    >>> is_almost_safe([1, 3, 6, 7, 9])
    True
    """
    safe = False

    idx = 0
    while idx < len(report) and not safe:
        truncated_report = report[0:idx] + report[idx + 1:]
        safe = is_safe(truncated_report)
        idx += 1

    return safe


def find_safe_and_almost_safe_reports(input_file="data/24-aoc-03.in"):
    """
    >>> find_safe_and_almost_safe_reports("test/24-aoc-03.test")
    4
    """
    reports = read_reports_03(input_file)
    safe_reports = sum(is_almost_safe(report) for report in reports)
    return safe_reports


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    print(f"Total nr. of safe and almost safe reports:\n\t{find_safe_and_almost_safe_reports()}")
