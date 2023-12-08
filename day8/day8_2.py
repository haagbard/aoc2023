import re
from math import lcm

file = 'aoc2023/day8/input.txt'

with open(file, 'r') as file:
    lines = file.read().splitlines()

directions = lines[0] # LLRLRLR etc
instructions = {}

def find_next(target, steps):
    index = steps % len(directions)
    direction = directions[index]
    if direction == 'L':
        i = 0
    else:
        i = 1
    new_direction = instructions[target][i]
    return new_direction
    
def all_ends_with_z(instructions_to_check):
    for instr in instructions_to_check:
        if instr.endswith('Z') == False:
            return False
    return True
    
def find_next_for_all(starting_points, steps):
    new_starting_point = []
    if all_ends_with_z(starting_points):
        return steps

    for starting_point in starting_points:
        next_step = find_next(starting_point, steps)
        new_starting_point.append(next_step)
    
    steps += 1
    return new_starting_point, steps


map_instructions_re = r"(\w+)\s=\s\((\w+),\s(\w+)\)"

for line in lines:
    if re.match(map_instructions_re, line):
        data = re.findall(map_instructions_re, line)[0]
        target = data[0]
        left = data[1]
        right = data[2]
        instructions[target] = [left, right]

found = False

starting_points = []
for intruction in instructions:
    if intruction.endswith('A'):
        starting_points.append(intruction)

steps = []

for starting_point in starting_points:
    found_z = False
    steps_crnt = 0
    next_step = starting_point
    while found_z == False:
        next_step = find_next(next_step, steps_crnt)
        steps_crnt += 1
        if next_step.endswith('Z'):
            steps.append(steps_crnt)
            found_z = True

#print(steps)
print(f'steps: {lcm(*steps)}') # Least common multiple..