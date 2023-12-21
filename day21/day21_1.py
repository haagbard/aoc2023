import copy

file = 'aoc2023/day21/input.txt'

with open(file, 'r') as file:
    lines = file.read().splitlines()

max_steps = 64

logged_steps = set()

def replacer(s, newstring, index, nofail=False):
    if not nofail and index not in range(len(s)):
        raise ValueError("index outside given string")
    if index < 0:  # add it to the beginning
        return newstring + s
    if index > len(s):  # add it to the end
        return s + newstring
    return s[:index] + newstring + s[index + 1:]

def check_boundries_and_char(x, y, direction):
    if direction == 'N':
        if y - 1 >= 0:
            if lines[y-1][x] == '.':
                return True
        return False
    if direction == 'W':
        if x - 1 >= 0:
            if lines[y][x-1] == '.':
                return True
        return False
    if direction == 'S':
        if y + 1 < len(lines):
            if lines[y+1][x] == '.':
                return True
        return False
    if direction == 'E':
        if x + 1 < len(lines[0]):
            if lines[y][x+1] == '.':
                return True
        return False

next_steps = []

def find_next():

    while len(next_steps) > 0:
        next_step = next_steps.pop()
        splitted = next_step.split(' ')
        x = int(splitted[0])
        y = int(splitted[1])
        steps = int(splitted[2])
        steps += 1
        if check_boundries_and_char(x, y, 'N'):
            new_x = x
            new_y = y - 1
            if steps <= max_steps:
                if steps == max_steps:
                    logged_steps.add((new_x, new_y))
                next_steps.append(f'{new_x} {new_y} {steps}')
        if check_boundries_and_char(x, y, 'S'):
            new_x = x
            new_y = y + 1
            if steps <= max_steps:
                if steps == max_steps:
                    logged_steps.add((new_x, new_y))
                next_steps.append(f'{new_x} {new_y} {steps}')
        if check_boundries_and_char(x, y, 'W'):
            new_x = x - 1
            new_y = y
            if steps <= max_steps:
                if steps == max_steps:
                    logged_steps.add((new_x, new_y))
                next_steps.append(f'{new_x} {new_y} {steps}')
        if check_boundries_and_char(x, y, 'E'):
            new_x = x + 1
            new_y = y
            if steps <= max_steps:
                if steps == max_steps:
                    logged_steps.add((new_x, new_y))
                next_steps.append(f'{new_x} {new_y} {steps}')

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == 'S':
            start_pos = (x, y)

# Replace 'S' with '.'
lines[start_pos[1]] = replacer(lines[start_pos[1]], '.', start_pos[0])

next_steps.append(f'{start_pos[0]} {start_pos[1]} 0')

find_next()

print(len(logged_steps))