from threading import Thread

file = 'aoc2023/day10/input.txt'

with open(file, 'r') as file:
    lines = file.read().splitlines()

max_y = len(lines) - 1
max_x = len(lines[0]) - 1

def check_valid_moves(x, y, already_stepped):
    ret = {}
    counter = 0
    
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
            ret[counter] = [x, tmp_y]
            counter += 1

    tmp_x = x
    tmp_y = y + 1
    if y + 1 != len(lines):
        # Check down
        tmp = lines[tmp_y][x: x + 1]
        if tmp in valid_down and f'{tmp_x}:{tmp_y}' not in already_stepped:
            ret[counter] = [x, tmp_y]
            counter += 1

    tmp_x = x + 1
    tmp_y = y
    if tmp_x != len(lines[0]):
        # Check right
        tmp = lines[y][tmp_x: tmp_x + 1]
        if tmp in valid_right and f'{tmp_x}:{tmp_y}' not in already_stepped:
            ret[counter] = [tmp_x, y]
            counter += 1

    tmp_x = x - 1
    tmp_y = y
    if tmp_x >= 0:
        tmp = lines[y][tmp_x: tmp_x + 1]
        if tmp in valid_left and f'{tmp_x}:{tmp_y}' not in already_stepped:
            ret[counter] = [tmp_x, y]
            counter += 1

    return ret

class ThreadStepper(Thread):
    
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args,
                                                **self._kwargs)
    def join(self, *args):
        Thread.join(self, *args)
        return self._return

def step_next(x, y, steps_taken, already_stepped):
    steps = check_valid_moves(x, y, already_stepped)
    if lines[y][x:x+1] == 'S' and steps_taken != 0: # No more steps..
        steps_taken += 1
        return steps_taken
    else:
        threads = []
        if len(steps) == 1:
            x = steps[0][0]
            y = steps[0][1]
            str_step = f'{x}:{y}'
            already_stepped.append(str_step)
            steps_taken += 1
            return step_next(x,y,steps_taken, already_stepped)
        else:
            for step in steps:
                x = steps[step][0]
                y = steps[step][1]
                str_step = f'{x}:{y}'
                already_stepped.append(str_step)
                steps_taken += 1

                thread = ThreadStepper(target=step_next, args=(x,y,steps_taken,already_stepped))
                threads.append(thread)
            
            for thread in threads:
                thread.start()
            
            for thread in threads:
                return thread.join()
            
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

threads = []

valid_moves = check_valid_moves(x,y, {})
for valid_move in valid_moves:
    already_stepped = []
    x = valid_moves[valid_move][0]
    y = valid_moves[valid_move][1]
    already_stepped.append(f'{x}:{y}')
    thread = ThreadStepper(target=step_next, args=(x,y,1,already_stepped))
    threads.append(thread)

for thread in threads:
    thread.start()

for thread in threads:
    steps_all.append(thread.join() + 1) # Account for last step

print(steps_all)
print(int(max(steps_all)/2))