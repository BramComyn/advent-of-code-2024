#!/usr/bin/env python3

from collections import defaultdict
from aoc_util import read_safety_manuals

def sanitize_ordering_rules(ordering_rules):
    ordering = defaultdict(set)

    for rule in ordering_rules:
        str_precedent, str_page = rule.split("|")
        precedent, page = int(str_precedent), int(str_page)
        ordering[page].add(precedent)

    return ordering


def sanitize_pages_to_produce(str_pages_to_produce):
    pages_to_produce = [ [ int(page) for page in page_list.split(",") ] for page_list in str_pages_to_produce ]
    return pages_to_produce


def find_correct_middle_page_sum(input_file="data/24-aoc-09.in"):
    """
    >>> find_correct_middle_page_sum("test/24-aoc-09.test")
    143
    """
    str_ordering_rules, str_pages_to_produce = read_safety_manuals(input_file)
    ordering_rules = sanitize_ordering_rules(str_ordering_rules)
    pages_to_produce = sanitize_pages_to_produce(str_pages_to_produce)

    result = 0
    for page_list in pages_to_produce:
        idx = 0
        correct = True

        while idx < len(page_list) and correct:
            page = page_list[idx]

            next_idx = idx + 1
            while next_idx < len(page_list) and correct:
                next_page = page_list[next_idx]
                correct = page not in ordering_rules or next_page not in ordering_rules[page]
                next_idx += 1

            idx += 1

        if correct:
            result += page_list[len(page_list) // 2]

    return result    


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    print(f"Total correct middle page sum:\n\t{find_correct_middle_page_sum()}")
