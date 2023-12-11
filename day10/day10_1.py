import sys

file = 'aoc2023/day10/input.txt'

already_stepped = []

sys.setrecursionlimit(20000)
new_limit = sys.getrecursionlimit()
print(f'recusionlimit: {new_limit}')

with open(file, 'r') as file:
    lines = file.read().splitlines()

def check_valid_moves(x, y):
    ret = {}
    counter = 0
    
    current_char = lines[y][x:x+1]
    
    valid_up = ['|', '7', 'F']
    valid_down = ['|', 'J', 'L']
    valid_right = ['-','J','7']
    valid_left = ['-', 'F', 'L']

    tmp_x = x
    tmp_y = y - 1
    if tmp_y >= 0:
        # Check up
        tmp = lines[tmp_y][x: x + 1]
        if tmp in valid_up and f'{tmp_x}:{tmp_y}' not in already_stepped:
            if current_char in valid_down or current_char == 'S':
                ret[counter] = [tmp_x, tmp_y]
                counter += 1

    tmp_x = x
    tmp_y = y + 1
    if y + 1 != len(lines):
        # Check down
        tmp = lines[tmp_y][x: x + 1]
        if tmp in valid_down and f'{tmp_x}:{tmp_y}' not in already_stepped:
            if current_char in valid_up or current_char == 'S':
                ret[counter] = [tmp_x, tmp_y]
                counter += 1

    tmp_x = x + 1
    tmp_y = y
    if tmp_x != len(lines[0]):
        # Check right
        tmp = lines[y][tmp_x: tmp_x + 1]
        if tmp in valid_right and f'{tmp_x}:{tmp_y}' not in already_stepped:
            if current_char in valid_left or current_char == 'S':
                ret[counter] = [tmp_x, tmp_y]
                counter += 1

    tmp_x = x - 1
    tmp_y = y
    if tmp_x >= 0:
        tmp = lines[y][tmp_x: tmp_x + 1]
        if tmp in valid_left and f'{tmp_x}:{tmp_y}' not in already_stepped:
            if current_char in valid_right or current_char == 'S':
                ret[counter] = [tmp_x, tmp_y]
                counter += 1

    return ret

def step_next(x, y, steps_taken):
    steps = check_valid_moves(x, y)
    if lines[y][x:x+1] == 'S' and steps_taken != 0: # No more steps..
        steps_taken += 1
        return steps_taken
    else:
        if len(steps) == 1:
            x = steps[0][0]
            y = steps[0][1]
            str_step = f'{x}:{y}'
            already_stepped.append(str_step)
            steps_taken += 1
            return step_next(x, y, steps_taken)
        else:
            pass
            
    return steps_taken + 1

start_x = -1
start_y = -1

for index, line in enumerate(lines):
    if 'S' in line:
        start_y = index
        start_x = line.index('S')

valid_moves = {}

print(f'Starting at {start_x}, {start_y}')

x = start_x
y = start_y

valid_moves = check_valid_moves(x, y) # Start directions
x = valid_moves[0][0]
y = valid_moves[0][1]
already_stepped.append(f'{x}:{y}')
steps = step_next(x, y, 1)

print(int(steps/2))