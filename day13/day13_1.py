file = 'aoc2023/day13/input.txt'

def scan_vertical(pattern):
    match_indexes = []
    for index in range(1, len(pattern)):
        prev_line = pattern[index - 1]
        line = pattern[index]
        if prev_line == line:
            match_indexes.append(index)

    # See if they can match all the way to either end
    for index in match_indexes:
        end_found = False
        all_match = True
        counter = 1
        while end_found == False:
            if index - counter == 0:
                end_found = True
            elif index + counter == len(pattern):
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

def scan_horizontal(pattern):
    match_indexes = []
    for index in range(1, len(pattern[0])):
        prev_line = ''
        line = ''
        for tmp_line in pattern:
            prev_line += tmp_line[index - 1]
            line += tmp_line[index]
        if prev_line == line:
            match_indexes.append(index)
    
    # See if they can match all the way to either end
    for index in match_indexes:
        end_found = False
        all_match = True
        counter = 1
        while end_found == False:
            if index - counter == 0:
                end_found = True
            elif index + counter == len(pattern[0]):
                end_found = True
            else:
                prev_x = index - counter - 1
                next_x = index + counter
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
    vert_score = scan_vertical(patterns[c])
    hor_score = scan_horizontal(patterns[c])
    if vert_score != -1:
        sum += vert_score * 100
    elif hor_score != -1:
        sum += hor_score

print(sum)