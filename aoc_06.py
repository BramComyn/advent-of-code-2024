#!/usr/bin/env python3

from aoc_util import read_memory_muls
from aoc_05 import execute_mul
import re

mul_regex = r"do\(\)|mul\(\d{1,3},\d{1,3}\)|don't\(\)"
do_instruction = "do()"
dont_instruction = "don't()"

def execute_program(memory):
    enabled = True
    result = 0

    for instruction in memory:
        if instruction == do_instruction:
            enabled = True
        elif instruction == dont_instruction:
            enabled = False
        elif enabled:
            result += execute_mul(instruction)

    return result

def find_conditional_muls(input_file="data/24-aoc-05.in"):
    """
    >>> find_conditional_muls("test/24-aoc-06.test")
    48
    """
    dirty_memory = read_memory_muls(input_file)
    memory = re.finditer(mul_regex, dirty_memory)
    result = execute_program([instruction.group() for instruction in memory])
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    print(f"Total value of all conditional mul-instructions:\n\t{find_conditional_muls()}")
