import re
import copy

file = 'aoc2023/day18/input.txt'

with open(file, 'r') as file:
    lines = file.read().splitlines()

output_data = []

def replacer(s, newstring, index, nofail=False):
    if not nofail and index not in range(len(s)):
        raise ValueError("index outside given string")
    if index < 0:  # add it to the beginning
        return newstring + s
    if index > len(s):  # add it to the end
        return s + newstring
    return s[:index] + newstring + s[index + 1:]

# Trim later
for tmp_y in range(0, 10000):
    output_data.append('.' * 10000)

def draw_line(x, y, direction, length):
    extend = 1
    if (x, y) == (0,0):
        extend = 0
    if 'R' == direction:
        for tmp_x in range(x, x + length + extend):
            line = output_data[y]
            line = replacer(line, '#', tmp_x)
            output_data[y] = line
        x = x + length
    elif 'L' == direction:
        for tmp_x in range(x - length, x + extend):
            line = output_data[y]
            line = replacer(line, '#', tmp_x)
            output_data[y] = line
        x = x - length
    elif 'U' == direction:
        for tmp_y in range(y - length, y + extend):
            crnt_line = output_data[tmp_y]
            crnt_line = replacer(crnt_line, '#', x)
            output_data[tmp_y] = crnt_line
        y = y - length
    elif 'D' == direction:
        for tmp_y in range(y, y + length + extend):
            crnt_line = output_data[tmp_y]
            crnt_line = replacer(crnt_line, '#', x)
            output_data[tmp_y] = crnt_line
        y = y + length
    return x, y

def trim_data(min_x, min_y, max_x, max_y):
    ret_data = []
    for y in range(min_y, max_y + 1):
        line = output_data[y]
        line = line[min_x:max_x + 1]
        ret_data.append(line)
    return ret_data

def ray_trace(input):
    # Replace all corners with L, 7, J and F
    for y in range(0, len(input)):
        for x in range(0, len(input[0])):
            crnt_char = input[y][x]
            if crnt_char == '#':
                if y + 1 < len(input):
                    char_below = input[y+1][x]
                    if char_below == '#':
                        if x + 1 < len(input[0]):
                            char_right = input[y][x+1]
                            if char_right == '#':
                                line = replacer(input[y], 'F', x)
                                input[y] = line
                        if x - 1 >= 0:
                            char_left = input[y][x-1]
                            if char_left == '#':
                                line = replacer(input[y], '7', x)
                                input[y] = line
                if y - 1 >= 0:
                    char_above = input[y-1][x]
                    if char_above == '#':
                        if x + 1 < len(input[0]):
                            char_right = input[y][x+1]
                            if char_right == '#':
                                line = replacer(input[y], 'L', x)
                                input[y] = line
                        if x - 1 >= 0:
                            char_left = input[y][x-1]
                            if char_left == '#':
                                line = replacer(input[y], 'J', x)
                                input[y] = line
                 
    crnt_char = ''
    for y in range(0, len(input)):
        line = input[y]
        for x in range(0, len(line)):
            crnt_char = line[x]
            if crnt_char == '.':
                count_walls = 0
                in_wall = False
                corner_char = ''
                for xx in range(x, len(line)):
                    if (line[xx] == 'F' or line[xx] == 'L' or line[xx] == '#') and in_wall == False:
                        if line[xx] == 'F' or line[xx] == 'L':
                            corner_char = line[xx]
                        if xx == len(line) - 1 and line[xx] == '#': # Edge case when line stops at #
                            count_walls += 1
                        in_wall = True
                    elif in_wall == True and (line[xx] == '.' or xx == len(line) - 1):
                        in_wall = False
                        if xx == len(line) - 1:
                            prev_char = line[xx]
                        else:
                            prev_char = line[xx-1]
                        if prev_char == 'J' and corner_char == 'L':
                            corner_char = ''
                        elif prev_char == '7' and corner_char == 'F':
                            corner_char = ''
                        else:
                            corner_char = ''
                            count_walls += 1
                if count_walls % 2 == 1:
                    # Inside
                    line = replacer(line,'#',x)
                    input[y] = line
    
    # Reset corners before return
    for y, line in enumerate(input):
        line = line.replace('L','#')
        line = line.replace('7','#')
        line = line.replace('F','#')
        line = line.replace('J','#')
        input[y] = line
    
    return input

def count_it(input):
    filled = 0
    for line in input:
        for x in range(0, len(line)):
            if line[x] == '#':
                filled += 1
    return filled

extract_re = r'(\w)\s(\d+)\s(\(#\w+\))'

data = {}

for index, line in enumerate(lines):
    data_line = re.findall(extract_re, line)[0]
    data[index] = [data_line[0], int(data_line[1]), data_line[2]]

x, y = (200,200) # start

min_x = x
min_y = y
max_x = x
max_y = y

for d in data:
    data_line = data[d]
    direction = data_line[0]
    length = data_line[1]
    color = data_line[2]
    x, y = draw_line(x, y, direction, length)
    if x < min_x:
        min_x = x
    if y < min_y:
        min_y = y
    if x > max_x:
        max_x = x
    if y > max_y:
        max_y = y

output = trim_data(min_x, min_y, max_x, max_y)

output = ray_trace(output)

sum = count_it(output)

for o in output:
    print(o)

print(sum)