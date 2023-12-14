import copy

file = 'aoc2023/day13/input.txt'

def scan_vertical(pattern, row_to_skip, original_vert_score):
    match_indexes = []
    for index in range(1, len(pattern)):
        prev_line = pattern[index - 1]
        line = pattern[index]
        if prev_line == line and index != original_vert_score:
            match_indexes.append(index)

    # See if they can match all the way to either end
    for index in match_indexes:
        end_found = False
        all_match = True
        counter = 0
        while end_found == False:
            if index - counter == 0:
                end_found = True
            elif index + counter == len(pattern):
                end_found = True
            elif index - counter - 1 == row_to_skip:
                end_found = True
            elif index + counter == row_to_skip:
                end_found = True
            else:
                prev_line = pattern[index - counter - 1]
                next_line = pattern[index + counter]
                if prev_line != next_line:
                    all_match = False
                    break
            counter += 1
        if all_match:
            return index
            
    return -1

def scan_horizontal(pattern, col_to_skip, original_hor_score):
    match_indexes = []
    for index in range(1, len(pattern[0])):
        prev_line = ''
        line = ''
        for tmp_line in pattern:
            prev_line += tmp_line[index - 1]
            line += tmp_line[index]
        if prev_line == line and index != original_hor_score:
            match_indexes.append(index)
    
    # See if they can match all the way to either end
    for index in match_indexes:
        end_found = False
        all_match = True
        counter = 0
        while end_found == False:
            if index - counter == 0:
                end_found = True
            elif index + counter == len(pattern[0]):
                end_found = True
            else:
                prev_x = index - counter - 1
                next_x = index + counter
                if prev_x != col_to_skip and next_x != col_to_skip:
                    prev_line = ''
                    next_line = ''
                    for tmp_line in pattern:
                        prev_line += tmp_line[prev_x]
                        next_line += tmp_line[next_x]
                    if prev_line != next_line:
                        all_match = False
                        break
            counter += 1
        if all_match:
            return index
        
    return -1

def replacer(s, newstring, index, nofail=False):
    # raise an error if index is outside of the string
    if not nofail and index not in range(len(s)):
        raise ValueError("index outside given string")

    # if not erroring, but the index is still not in the correct range..
    if index < 0:  # add it to the beginning
        return newstring + s
    if index > len(s):  # add it to the end
        return s + newstring

    # insert the new string between "slices" of the original
    return s[:index] + newstring + s[index + 1:]

def replace_one_mirror(x, y, pattern):
    line = pattern[y]
    char = line[x]
    if char == '#':
        char = '.'
    elif char == '.':
        char = '#'
    line = replacer(line,char,x)
    pattern[y] = line
    return pattern

def find_non_mirrored_lines(pattern):
    row_to_ignore = -1
    col_to_ignore = -1
    if pattern[0] == pattern[len(pattern) - 2]:
        row_to_ignore = len(pattern) - 1
    elif pattern[len(pattern) - 1] == pattern[1]:
        row_to_ignore = 0

    pos_0_str = ''
    pos_1_str = ''
    pos_last_str = ''
    pos_second_to_last_str = ''
    for p_temp in pattern:
        pos_0_str += p_temp[0]
        pos_1_str += p_temp[1]
        pos_last_str += p_temp[len(p_temp) - 1]
        pos_second_to_last_str += p_temp[len(p_temp) - 2]

    if pos_0_str == pos_second_to_last_str:
        col_to_ignore = len(pattern[0]) - 1
    elif pos_last_str == pos_1_str:
        col_to_ignore = 0

    return row_to_ignore, col_to_ignore

patterns = {}

with open(file, 'r') as file:
    lines = file.read().splitlines()

counter = 0
tmp_lines = []
for line in lines:
    if line == '' :
        patterns[counter] = tmp_lines
        tmp_lines = []
        counter += 1
    else:
        tmp_lines.append(line)

patterns[counter] = tmp_lines

sum = 0

for c in patterns:
    found = False
    pattern = patterns[c]

    row_to_ignore, col_to_ignore = find_non_mirrored_lines(pattern)

    original_vert_score = scan_vertical(pattern, -1, -1)
    original_hor_score = scan_horizontal(pattern, -1, -1)

    for y in range(0, len(pattern)):
        for x in range(0, len(pattern[0])):
            if found == False:
                p = replace_one_mirror(x, y, copy.deepcopy(patterns[c]))
                vert_score = -1
                hor_score = -1
                vert_score = scan_vertical(p, col_to_ignore, original_vert_score)
                hor_score = scan_horizontal(p, row_to_ignore, original_hor_score)
                if vert_score > 0:
                    print(f'{c}: V found at {x},{y}')
                    sum += vert_score * 100
                    found = True
                elif hor_score > 0:
                    print(f'{c}: H found at {x},{y}')
                    sum += hor_score
                    found = True

print(sum)