import time
import math

start_time = time.time()

file = 'aoc2023/day21/input.txt'

with open(file, 'r') as file:
    lines = file.read().splitlines()

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
#max_steps = 10

# Find start
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == 'S':
            start_pos = (x, y)

steps_for_odd = 0
steps_for_even = 0

# Find all the amount of marked "." for odd and even squares
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == '.' or char == 'S':
            steps_x = abs(x - start_pos[0])
            steps_y = abs(y - start_pos[1])
            total_steps = steps_x + steps_y
            if total_steps % 2 == 0 and check_surroundings(x, y): # Even steps
                steps_for_even += 1
            if total_steps % 2 == 1 and check_surroundings(x, y): # Odd steps
                steps_for_odd += 1


steps_for_odd_corners = 0
steps_for_even_corners = 0

# And for corners, we count everything where steps > x
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == '.' or char == 'S':
            steps_x = abs(x - start_pos[0])
            steps_y = abs(y - start_pos[1])
            total_steps = steps_x + steps_y
            if total_steps % 2 == 0 and total_steps > start_pos[0] and check_surroundings(x, y): # Even steps
                steps_for_even_corners += 1
            if total_steps % 2 == 1 and total_steps > start_pos[0] and check_surroundings(x, y): # Odd steps
                steps_for_odd_corners += 1

# Squares from start to edge = (max_steps - start_position_x) / length_of_square
# In this instance, square is 131x131, so amount of squares from start to edge = (26501365 - 65) / 131
amount_squares = int((max_steps - start_pos[0]) / len(lines))

amount_odd_squares = int(math.pow(amount_squares + 1, 2))
amount_even_squares = int(math.pow(amount_squares, 2))

print(f'Steps per odd square: {steps_for_odd}, steps for even: {steps_for_even}')
print(f'Steps per odd square corners: {steps_for_odd_corners}, steps for even corners: {steps_for_even_corners}')

print(f'Amount odd: {amount_odd_squares}, amount even: {amount_even_squares}')

sum = (amount_odd_squares * steps_for_odd) + (amount_even_squares * steps_for_even) - ((amount_squares+1) * steps_for_odd_corners) + (amount_squares * steps_for_even_corners)

print(f'Sum: {sum}')

print("--- %s seconds ---" % (time.time() - start_time))