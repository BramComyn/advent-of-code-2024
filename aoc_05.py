#!/usr/bin/env python3

from aoc_util import read_memory_muls
import re

mul_regex = r"mul\(\d{1,3},\d{1,3}\)"

def execute_mul(mul_instruction):
    truncated_instruction = mul_instruction[4:].replace("(", "").replace(")", "")
    factor1, factor2 = truncated_instruction.split(",")
    return int(factor1) * int(factor2)


def find_muls(input_file="data/24-aoc-05.in"):
    """"
    >>> find_muls("test/24-aoc-05.test")
    161
    """
    dirty_memory = read_memory_muls(input_file)
    memory = re.finditer(mul_regex, dirty_memory)
    result = sum(execute_mul(mul_instruction.group()) for mul_instruction in memory)
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    print(f"Total value of all mul-instructions:\n\t{find_muls()}")
