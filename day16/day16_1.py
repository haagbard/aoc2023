import copy
import sys

sys.setrecursionlimit(20000)
new_limit = sys.getrecursionlimit()
print(f'recusionlimit: {new_limit}')

file = 'aoc2023/day16/input.txt'

with open(file, 'r') as file:
    lines = file.read().splitlines()

energized_lines = copy.deepcopy(lines)

moves_logged = []

def replacer(s, newstring, index, nofail=False):
    if not nofail and index not in range(len(s)):
        raise ValueError("index outside given string")
    if index < 0:  # add it to the beginning
        return newstring + s
    if index > len(s):  # add it to the end
        return s + newstring
    return s[:index] + newstring + s[index + 1:]

def mark_as_enegized(x, y):
    line = energized_lines[y]
    line = replacer(line, '#', x)
    energized_lines[y] = line

def calculate_points():
    points = 0
    for line in energized_lines:
        points += line.count('#')
    return points

def same_everywhere(input_list):
    first_element = input_list[0]
    for line in input_list:
        if line != first_element:
            return False
    return True

def move_laser(x, y, direction):
    if x == len(lines[0]) or y == len(lines) or x == -1 or y == -1:
        return # Outside
    current_tile = lines[y][x]
    standard_log = f'{direction}:{x},{y}'
    if standard_log in moves_logged:
        return
    else:
        moves_logged.append(standard_log)
    if current_tile == '.':
        mark_as_enegized(x, y)
        if direction == 'N':
            y = y - 1
        elif direction == 'W':
            x = x - 1
        elif direction == 'S':
            y = y + 1
        elif direction == 'E':
            x = x + 1
        return move_laser(x, y, direction)
    elif current_tile == '|':
        mark_as_enegized(x, y)
        if direction == 'N':
            y = y - 1
            move_laser(x, y, direction)
        elif direction == 'W':
            move_laser(x, y - 1, 'N')
            move_laser(x, y + 1, 'S')
        elif direction == 'S':
            y = y + 1
            move_laser(x, y, direction)
        elif direction == 'E':
            move_laser(x, y - 1, 'N')
            move_laser(x, y + 1, 'S')
    elif current_tile == '-':
        mark_as_enegized(x, y)
        if direction == 'N':
            move_laser(x - 1, y, 'W')
            move_laser(x + 1, y, 'E')
        elif direction == 'W':
            x = x - 1
            move_laser(x, y, direction)
        elif direction == 'S':
            move_laser(x - 1, y, 'W')
            move_laser(x + 1, y, 'E')
        elif direction == 'E':
            x = x + 1
            move_laser(x, y, direction)
    elif current_tile == '/':
        mark_as_enegized(x, y)
        if direction == 'N':
            move_laser(x + 1, y, 'E')
        elif direction == 'W':
            move_laser(x, y + 1, 'S')
        elif direction == 'S':
            move_laser(x - 1, y, 'W')
        elif direction == 'E':
            move_laser(x, y - 1, 'N')
    elif current_tile == '\\':
        mark_as_enegized(x, y)
        if direction == 'N':
            move_laser(x - 1, y, 'W')
        elif direction == 'W':
            move_laser(x, y - 1, 'N')
        elif direction == 'S':
            move_laser(x + 1, y, 'E')
        elif direction == 'E':
            move_laser(x, y + 1, 'S')

move_laser(0,0,'E')

for line in energized_lines:
    print(line)

p = calculate_points()
print(p)