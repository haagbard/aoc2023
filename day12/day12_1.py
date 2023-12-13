import re
from itertools import combinations

file = 'aoc2023/day12/input.txt'

def is_valid_arrangement(springs: str, expected_group_sizes: list[int]) -> bool:
    actual_groups = re.findall(r'#+', springs)
    actual_group_sizes = list(map(len, actual_groups))
    return actual_group_sizes == expected_group_sizes

with open(file, 'r') as file:
    lines = file.read().splitlines()

def find_all_solutions(springs, numbers):
    total_springs = sum(numbers)
    unassigned_springs = total_springs - springs.count('#')
    unassigned_positions = []
    for x, char in enumerate(springs):
        if char == "?":
            unassigned_positions.append(x)

    arrangements_counter = 0
    for combination in combinations(unassigned_positions, unassigned_springs):
        new_springs = list(springs)
        for pos in combination:
            new_springs[pos] = '#'
        if is_valid_arrangement(''.join(new_springs), numbers):
            arrangements_counter += 1

    return arrangements_counter

total_arrangements = 0

for line in lines:
    springs, all_numbers = line.split()
    numbers = list(map(int, all_numbers.split(',')))
    total_arrangements += find_all_solutions(springs, numbers)

print(total_arrangements)