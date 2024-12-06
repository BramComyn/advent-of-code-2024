#!/usr/bin/env python3

from aoc_util import read_safety_manuals
from aoc_09 import sanitize_ordering_rules, sanitize_pages_to_produce

def reorder_recursive(page, stack, visited, page_list, ordering_rules):
    visited[page] = True

    for precedent in ordering_rules[page]:
        if precedent in visited and not visited[precedent]:
            reorder_recursive(precedent, stack, visited, page_list, ordering_rules)

    stack.insert(0, page)


def reorder(page_list, ordering_rules):
    visited = { page: False for page in page_list }
    stack = []

    for page in page_list:
        if not visited[page]:
            reorder_recursive(page, stack, visited, page_list, ordering_rules)
    
    return stack


def find_incorrect_middle_page_sum(input_file="data/24-aoc-09.in"):
    """
    >>> find_incorrect_middle_page_sum("test/24-aoc-09.test")
    123
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

        if not correct:
            page_list = reorder(page_list, ordering_rules)
            result += page_list[len(page_list) // 2]

    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    print(f"Total incorrect middle page sum:\n\t{find_incorrect_middle_page_sum()}")
