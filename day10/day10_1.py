import sys

file = 'aoc2023/day10/input.txt'

sys.setrecursionlimit(20000)
new_limit = sys.getrecursionlimit()
print(f'recusionlimit: {new_limit}')

with open(file, 'r') as file:
    lines = file.read().splitlines()

def check_valid_moves(x, y, already_stepped):
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

    if len(ret) > 1:
        print('find out')
        current_char = lines[y][x:x+1]
        if current_char == 'S': # Start position so it's ok
            return ret 
        else:
            for ret_tmp in ret:
                next_pos = ret[ret_tmp]
                x1 = next_pos[0]
                y1 = next_pos[1]
                next_char = lines[y1][x1]
                print(f'next_char: {next_char}')
        print(f'{current_char}')

    return ret

def step_next(x, y, steps_taken, already_stepped):
    steps = check_valid_moves(x, y, already_stepped)
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
            return step_next(x, y, steps_taken, already_stepped)
        elif len(steps) > 1:
            print('How??')
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

steps_all = []

valid_moves = check_valid_moves(x,y, {}) # Start directions
for valid_move in valid_moves:
    already_stepped = []
    x = valid_moves[valid_move][0]
    y = valid_moves[valid_move][1]
    already_stepped.append(f'{x}:{y}')
    steps_all.append(step_next(x, y, 1, already_stepped))

print(steps_all)
print(int(max(steps_all)/2))