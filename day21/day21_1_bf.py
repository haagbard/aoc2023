import time

file = 'aoc2023/day21/input.txt'

with open(file, 'r') as file:
    lines = file.read().splitlines()

max_steps = 10

steps_to_take = ((-1,0), (1,0), (0,-1), (0,1))

max_x = len(lines[0])
max_y = len(lines)

logged_steps = set()

def replacer(s, newstring, index, nofail=False):
    if not nofail and index not in range(len(s)):
        raise ValueError("index outside given string")
    if index < 0:  # add it to the beginning
        return newstring + s
    if index > len(s):  # add it to the end
        return s + newstring
    return s[:index] + newstring + s[index + 1:]

def check_boundries_and_char(x, y):
    if x >= 0 and x < max_x:
        if y >= 0 and y < max_y:
            if lines[y][x] != '#':
                return True
    return False

next_steps = []

def find_next():

    while len(next_steps) > 0:
        next_step = next_steps.pop()
        x = next_step[0]
        y = next_step[1]
        steps = next_step[2]
        steps += 1

        for step in steps_to_take:
            new_x = x + step[0]
            new_y = y + step[1]
            if check_boundries_and_char(new_x, new_y):
                if steps == max_steps:
                    logged_steps.add((new_x, new_y))
                else:
                    next_step_t = (new_x, new_y, steps)
                    next_steps.append(next_step_t)

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == 'S':
            start_pos = (x, y)

start_time = time.time()

# Replace 'S' with '.'
lines[start_pos[1]] = replacer(lines[start_pos[1]], '.', start_pos[0])

next_steps.append((start_pos[0], start_pos[1], 0))

find_next()

print(len(logged_steps))

print("--- %s seconds ---" % (time.time() - start_time))
