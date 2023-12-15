import copy
import re

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
    moved_since_last = True # Reached maximum
    
    while moved_since_last:
        previous_lines = copy.deepcopy(lines)
        for y in range(1, len(lines)):
            line = lines[y]
            for x in range(0,len(line)):
                if line[x] == 'O':
                    x_above = lines[y-1][x]
                    if x_above == '.':
                        line = replacer(line,'.',x)
                        line_above = replacer(lines[y-1],'O',x)
                        lines[y] = line
                        lines[y - 1] = line_above
        if previous_lines == lines:
            # No more moves
            moved_since_last = False

def calculate_load():
    stone_re = r"(O)"
    load_max = len(lines)
    ret_sum = 0
    for i in range(0, load_max):
        line = lines[i]
        amount_of_stones = len(re.findall(stone_re,line))
        ret_sum += amount_of_stones * (load_max - i)

    return ret_sum

move_north()

sum = calculate_load()

print(sum)