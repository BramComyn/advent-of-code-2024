#!/usr/bin/env python3

from aoc_util import read_calibration_equations

def is_possible_concat_combination_rec(result, intermediate, remaining_terms):
    # base cases
    if result < intermediate or (intermediate < result and len(remaining_terms) == 0):
        return False
    elif intermediate == result and len(remaining_terms) == 0:
        return True

    # recursion with the sum
    if is_possible_concat_combination_rec(result, intermediate + remaining_terms[0], remaining_terms[1:]):
        return True
    
    # recursion with the product
    if is_possible_concat_combination_rec(result, intermediate * remaining_terms[0], remaining_terms[1:]):
        return True
    
    # recursion with the concatenation
    if is_possible_concat_combination_rec(result, int(str(intermediate) + str(remaining_terms[0])), remaining_terms[1:]):
        return True
    
    return False


def is_possible_concat_combination(result, terms):
    if is_possible_concat_combination_rec(result, 0, terms):
        return result
    return 0


def find_possible_concat_equations_sum(input_file="data/24-aoc-13.in"):
    """
    >>> find_possible_concat_equations_sum("test/24-aoc-13.test")
    11387
    """
    equations = read_calibration_equations(input_file)
    return sum(is_possible_concat_combination(result, terms) for result, terms in equations)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    print(f"Total possibly concatenated calibrations sum:\n\t{find_possible_concat_equations_sum()}")
