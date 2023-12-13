file = 'aoc2023/day11/input.txt'

expansion = 1000000

x_expansions = []
y_expansions = []

with open(file, 'r') as file:
    lines = file.read().splitlines()

def only_empty_space(input):
    for i in input:
        if i != '.':
            return False
    return True

def expand_star_map():
    expanded_starmap = []
    # expand y
    for y, line in enumerate(lines):
        if only_empty_space(line):
            y_expansions.append(y)
    # expand x
    expanded_starmap_tmp_var = []
    expanded_starmap_tmp_var.extend(expanded_starmap)
    extended_amount = 0
    for x in range(0,len(lines[0])):
        tmp_str = ''
        for line in lines:
            tmp_char = line[x:x+1]
            tmp_str += tmp_char
        if only_empty_space(tmp_str):
            x_expansions.append(x)

def measure_distance(star_position, star_position_next):
    pos1 = star_position.split(':')
    pos2 = star_position_next.split(':')
    x1 = int(pos1[0])
    y1 = int(pos1[1])
    x2 = int(pos2[0])
    y2 = int(pos2[1])

    x_change = abs(x1 - x2)
    for x_exp in x_expansions:
        if (x1 > x_exp and x2 < x_exp) or (x1 < x_exp and x2 > x_exp):
            x_change += expansion - 1

    y_change = abs(y1 - y2)
    for y_exp in y_expansions:
        if (y1 > y_exp and y2 < y_exp) or (y1 < y_exp and y2 > y_exp):
            y_change += expansion - 1

    return x_change + y_change

expand_star_map()
expanded_starmap = lines

star_positions = []

for y, starmap in enumerate(expanded_starmap):
    for x, char in enumerate(starmap):
        if char == '#':
            star_positions.append(f'{x}:{y}')

checked_stars = []
sum = 0

for star_position in star_positions:
    for star_position_next in star_positions:
        check_one = f'{star_position}:{star_position_next}'
        check_two = f'{star_position_next}:{star_position}'
        if check_one in checked_stars or check_two in checked_stars:
            pass
        elif check_one == check_two:
            pass
        else:
            # measure...
            sum += measure_distance(star_position, star_position_next)
            checked_stars.append(f'{star_position}:{star_position_next}')

print(sum)