import re
from itertools import combinations
from threading import Thread
import functools

file = 'aoc2023/day12/input.txt'

with open(file, 'r') as file:
    lines = file.read().splitlines()

@functools.lru_cache(maxsize=None)
def calc(record, groups):
    if not groups:
        if "#" not in record:
            return 1
        else:
            return 0

    if not record:
        return 0

    next_character = record[0]
    next_group = groups[0]

    def pound():
        this_group = record[:next_group]
        this_group = this_group.replace("?", "#")

        if this_group != next_group * "#":
            return 0

        if len(record) == next_group:
            if len(groups) == 1:
                return 1
            else:
                return 0

        if record[next_group] in "?.":
            return calc(record[next_group+1:], groups[1:])
        return 0

    def dot():
        return calc(record[1:], groups)

    if next_character == '#':
        out = pound()
    elif next_character == '.':
        out = dot()
    elif next_character == '?':
        out = dot() + pound()

    else:
        raise RuntimeError

    return out

total_arrangements = 0

threads = []

for line in lines:
    springs, all_numbers = line.split()
    numbers = list(map(int, all_numbers.split(',')))
    new_springs = ''
    new_numbers = []
    for i in range(0, 5):
        new_springs += springs + '?'
        new_numbers.extend(numbers)
    new_springs = new_springs[:-1]
    total_arrangements += calc(new_springs, tuple(new_numbers))

print(total_arrangements)