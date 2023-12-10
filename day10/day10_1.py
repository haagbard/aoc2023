file = 'aoc2023/day10/input.txt'

already_stepped = []

with open(file, 'r') as file:
    lines = file.read().splitlines()

max_y = len(lines) - 1
max_x = len(lines[0]) - 1

def check_valid_moves(x, y):
    ret = {}
    counter = 0
    
    valid_up = ['|', '7', 'F']
    valid_down = ['|', 'J', 'L']
    valid_right = ['-','J','7']
    valid_left = ['-', 'F', 'L']

    if y - 1 >= 0:
        # Check up
        tmp = lines[y - 1][x: x + 1]
        if tmp in valid_up:
            ret[counter] = [x, y - 1]
            counter += 1

    if y + 1 != len(lines):
        # Check down
        tmp = lines[y + 1][x: x + 1]
        if tmp in valid_down:
            ret[counter] = [x, y + 1]
            counter += 1

    if x + 1 != len(lines[0]):
        # Check right
        tmp = lines[y][x + 1: x + 2]
        if tmp in valid_right:
            ret[counter] = [x + 1, y]
            counter += 1

    if x - 1 >= 0:
        tmp = lines[y][x - 1: x]
        if tmp in valid_left:
            ret[counter] = [x - 1, y]
            counter += 1

    return ret

def step_next(x, y, steps_taken):
    steps = check_valid_moves(x, y)
    if lines[y][x:x+1] == 'S' and steps_taken != 0: # No more steps..
        steps_taken += 1
        return steps_taken
    else:
        for step in steps:
            x = steps[step][0]
            y = steps[step][1]
            str_step = f'{x}:{y}'
            if str_step in already_stepped: # No back stepping
                pass
            else:
                already_stepped.append(str_step)
                steps_taken += 1
                return step_next(x,y,steps_taken)
            
    return steps_taken

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

steps_all = []

valid_moves = check_valid_moves(x,y)
for valid_move in valid_moves:
    already_stepped = []
    x = valid_moves[valid_move][0]
    y = valid_moves[valid_move][1]
    already_stepped.append(f'{x}:{y}')
    steps = step_next(x, y, 1)
    # Account for last step:
    steps += 1
    steps_all.append(steps)

print(steps_all)
print(int(max(steps_all)/2))