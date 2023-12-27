import time
import copy
from alive_progress import alive_bar
import math

file = 'aoc2023/day21/input.txt'

with open(file, 'r') as file:
    lines = file.read().splitlines()

def replacer(s, newstring, index, nofail=False):
    if not nofail and index not in range(len(s)):
        raise ValueError("index outside given string")
    if index < 0:  # add it to the beginning
        return newstring + s
    if index > len(s):  # add it to the end
        return s + newstring
    return s[:index] + newstring + s[index + 1:]

def check_surroundings(x, y):
    if y - 1 >= 0:
        char_above = lines[y-1][x]
    else:
        char_above = '#'
    if y + 1 < len(lines):
        char_below = lines[y+1][x]
    else:
        char_below = '#'
    if x + 1 < len(lines[0]):
        char_right = lines[y][x+1]
    else:
        char_right = '#'
    if x - 1 >= 0:
        char_left = lines[y][x-1]
    else:
        char_left = '#'
    if char_above == '#' and char_below == '#' and char_left == '#' and char_right == '#':
        return False
    return True

max_steps = 26501365
#max_steps = 500

logged_steps = set()

next_steps = []

# Find start
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == 'S':
            start_pos = (x, y)

# Make a copy
lines_origin = copy.deepcopy(lines)

# Replace 'S' with '.'
lines_origin[start_pos[1]] = replacer(lines_origin[start_pos[1]], '.', start_pos[0])

x_extend = math.ceil((max_steps + start_pos[0]) / len(lines[0]))
y_extend = math.ceil((max_steps + start_pos[1]) / len(lines))

with alive_bar(len(lines)) as bar:
# Expand X
    for y_pos in range(0, len(lines)):
        original_position = y_pos % len(lines_origin)
        prepend_str = lines_origin[original_position] * x_extend
        lines[y_pos] = f'{prepend_str}{lines[y_pos]}{prepend_str}'
        bar()
print('Expanded X')

with alive_bar(y_extend) as bar:
    # Expand Y
    for i in range(0, y_extend):
        lines[:0] = lines_origin
        lines.extend(lines_origin)
        bar()
print('Expanded Y')

start_time = time.time()

# Find start again
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == 'S':
            start_pos = (x, y)

next_steps.append((start_pos[0], start_pos[1], 0))

# Replace 'S' with '.'
lines[start_pos[1]] = replacer(lines[start_pos[1]], '.', start_pos[0])

odd_or_even = max_steps % 2

max_field = len(lines) * len(lines[0])

with alive_bar(max_field) as bar:

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == '.':
                steps_x = abs(x - start_pos[0])
                steps_y = abs(y - start_pos[1])
                if check_surroundings(x, y):
                    total_steps = steps_x + steps_y
                    if total_steps <= max_steps and total_steps % 2 == odd_or_even: # if less or eq to max_steps and even amount of steps.
                        logged_steps.add((x, y))
            bar()

for y in range(0, len(lines)):
    for x in range(0, len(lines[0])):
        if (x, y) in logged_steps:
            line = lines[y]
            line = replacer(line,'O',x)
            lines[y] = line

#for line in lines:
#    print(line)

print(len(logged_steps))

print("--- %s seconds ---" % (time.time() - start_time))