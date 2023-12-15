import re
from alive_progress import alive_bar

file = 'aoc2023/day14/input.txt'

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

def move_north():
    for y in range(1, len(lines)):
        line = lines[y]
        for x in range(0,len(line)):
            if line[x] == 'O':
                moved = False
                stoned_moved_to = -1
                for y_var in range(y-1, -1, -1):
                    x_above = lines[y_var][x]
                    if x_above == '.':
                        moved = True
                        stoned_moved_to = y_var
                    else: 
                        break
                if moved:
                    for y_var in range(y, stoned_moved_to-1, -1):
                        line_y = lines[y_var]
                        line_y = replacer(line_y,'.',x)
                        lines[y_var] = line_y
                    line_y = lines[stoned_moved_to]
                    line_y = replacer(line_y, 'O', x)
                    lines[stoned_moved_to] = line_y

def move_west():
    for y in range(0, len(lines)):
        line = lines[y]
        for x in range(1, len(line)):
            if line[x] == 'O':
                moved = False
                stoned_moved_to = -1
                for x_var in range(x-1, -1, -1):
                    x_left = line[x_var]
                    if x_left == '.':
                        moved = True
                        stoned_moved_to = x_var
                    else: 
                        break
                if moved:
                    for x_var in range(x, stoned_moved_to - 1, -1):
                        line = replacer(line,'.',x_var)
                        lines[y] = line
                    line = replacer(line, 'O', stoned_moved_to)
                    lines[y] = line

def move_south():
    for y in range(len(lines)-1, -1, -1):
        line = lines[y]
        for x in range(0,len(line)):
            if line[x] == 'O':
                moved = False
                stoned_moved_to = -1
                for y_var in range(y+1, len(lines)):
                    x_below = lines[y_var][x]
                    if x_below == '.':
                        moved = True
                        stoned_moved_to = y_var
                    else: 
                        break
                if moved:
                    for y_var in range(y, stoned_moved_to+1):
                        line_y = lines[y_var]
                        line_y = replacer(line_y,'.',x)
                        lines[y_var] = line_y
                    line_y = lines[stoned_moved_to]
                    line_y = replacer(line_y,'O',x)
                    lines[stoned_moved_to] = line_y


def move_east():
    for y in range(0, len(lines)):
        line = lines[y]
        for x in range(len(line)-1, -1, -1):
            if line[x] == 'O':
                moved = False
                stoned_moved_to = -1
                for x_var in range(x+1, len(line)):
                    x_right = line[x_var]
                    if x_right == '.':
                        moved = True
                        stoned_moved_to = x_var
                    else: 
                        break
                if moved:
                    for x_var in range(x, stoned_moved_to):
                        line = replacer(line,'.',x_var)
                        lines[y] = line
                    line = replacer(line, 'O', stoned_moved_to)
                    lines[y] = line

def calculate_load():
    stone_re = r"(O)"
    load_max = len(lines)
    ret_sum = 0
    for i in range(0, load_max):
        line = lines[i]
        amount_of_stones = len(re.findall(stone_re,line))
        ret_sum += amount_of_stones * (load_max - i)

    return ret_sum

iterations = 10000

sums = {}

# The pattern stabilizes after ~50 turns.
# The pattern should start to repeat itself after 22 turns

sums = []

offset = 100

for i in range(0, iterations):
    move_north()
    move_west()
    move_south()
    move_east()

    sum = calculate_load()
    if i >= offset: # Stable pattern
        if len(sums) > 1 and sum == sums[0]: # repeat detected
            break
        else:
            sums.append(sum)

position_to_get = 1000000000 - 1 # Offset by one..

list_post = (position_to_get - offset) % len(sums)

print(sums[list_post])