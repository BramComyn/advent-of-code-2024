#!/bin/bash

export PATH="$PATH:$(pwd)"

find -iname "aoc_*.py" -exec ./{} \;
