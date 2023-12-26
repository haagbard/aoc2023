import time

file = 'aoc2023/day21/input.txt'

with open(file, 'r') as file:
    lines = file.read().splitlines()

max_steps = 10

logged_steps = set()

next_steps = []

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == 'S':
            start_pos = (x, y)

start_time = time.time()

next_steps.append((start_pos[0], start_pos[1], 0))

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == '.':
            steps_x = abs(x - start_pos[0])
            steps_y = abs(y - start_pos[1])
            total_steps = steps_x + steps_y
            if total_steps <= max_steps and total_steps % 2 == 0: # if less or eq to max_steps and even amount of steps.
                logged_steps.add((x, y))

print(len(logged_steps))

print("--- %s seconds ---" % (time.time() - start_time))
