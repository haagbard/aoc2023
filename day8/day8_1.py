import re
import sys

file = 'aoc2023/day8/input.txt'

sys.setrecursionlimit(20000)
new_limit = sys.getrecursionlimit()
print(f'recusionlimit: {new_limit}')

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
    steps += 1
    if new_direction == 'ZZZ':
        return steps
    else:
        return find_next(new_direction, steps)

map_instructions_re = r"(\w+)\s=\s\((\w+),\s(\w+)\)"

for line in lines:
    if re.match(map_instructions_re, line):
        data = re.findall(map_instructions_re, line)[0]
        target = data[0]
        left = data[1]
        right = data[2]
        instructions[target] = [left, right]

found = False

steps = find_next('AAA', 0)

print(steps)