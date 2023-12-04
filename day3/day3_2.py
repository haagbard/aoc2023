import re

file = 'aoc2023/day3/input.txt'

with open(file, 'r') as file:
    lines = file.read().splitlines()

def extract_number(line, start_index, end_index):
    new_start_index, new_end_index = expand_indexes(start_index, end_index, line, 3, 3)
    digit_pattern = r"(\d+)"

    sub_str = line[new_start_index:new_end_index]

    tmp_start_index, tmp_end_index = expand_indexes(start_index, end_index, line, 1, 1)

    trim_left = False
    trim_right = False

    pattern_match_middle = re.match(r"[\d|\.]\.\d+\.[\d|\.]", sub_str)
    if pattern_match_middle: # When stuff looks like '9.212..' shit breaks below.
        sub_str = sub_str[1:len(sub_str) - 2]
        return re.findall(digit_pattern, sub_str)
    elif len(re.findall(digit_pattern, sub_str)) == 1: # Just one number, no need to process
        pattern_match_middle = re.match(r"[\d|\.]+\d+[\d|\.]+", sub_str)
        if pattern_match_middle:
            pattern_match_middle = re.match(r"[\d|\.]{2}\.\.\.[\d|\.]{2}", sub_str)
            pattern_match_middle_alt = re.match(r"\.{1,2}\d{1,3}\.{1,2}", sub_str)
            if pattern_match_middle == False: # Edge cases when string looks like '.....61'
                return re.findall(digit_pattern, sub_str)
            elif pattern_match_middle_alt:
                return re.findall(digit_pattern, sub_str)

    if line[tmp_start_index:end_index -1] == ".":
        # Remove left
        trim_left = True
    if line[end_index:tmp_end_index] == ".":
        # Remove right
        trim_right = True

    remove_left = start_index - new_start_index
    remove_right = new_end_index - end_index + 1

    if trim_right:
        sub_str = sub_str[0:remove_right]
    if trim_left:
        sub_str = sub_str[remove_left:]
    
    return re.findall(digit_pattern, sub_str)

    
def expand_indexes(start_index, end_index, line, start_steps, end_steps):
    new_start_index = start_index
    for i in range(0,start_steps):
        if new_start_index != 0: # Make sure we dont reach below 0
            new_start_index -= 1
    new_end_index = end_index
    for i in range(0,end_steps):
        if new_end_index != len(line): # Make sure we dont reach above line length
            new_end_index += 1
    
    return new_start_index, new_end_index

part_numbers = []
tmp_sum = 0

for index, line in enumerate(lines):
    if index != 0:
        prev_index_line = lines[index - 1]
    else:
        prev_index_line = 'N/A'
    if index != len(lines) - 1:
        next_index_line = lines[index + 1]
    else:
        next_index_line = 'N/A'
    
    stars_re = r"(\*)"
    all_stars = re.findall(stars_re, line)

    last_index = 0

    for crnt_star in all_stars:     
        start_index = line.index(crnt_star, last_index)
        end_index = start_index + 1

        last_index = end_index

        gear_numbers = []

        # Line above
        if prev_index_line != 'N/A':
            numbers = extract_number(prev_index_line, start_index, end_index)
            gear_numbers.extend(numbers)
        # Line below
        if next_index_line != 'N/A':
            numbers = extract_number(next_index_line, start_index, end_index)
            gear_numbers.extend(numbers)
        # Current line
        numbers = extract_number(line, start_index, end_index)
        gear_numbers.extend(numbers)

        if len(gear_numbers) == 2:
            product = int(gear_numbers[0]) * int(gear_numbers[1])
            part_numbers.append(product)

sum = 0

for part_number in part_numbers:
    sum += int(part_number)

print(sum)