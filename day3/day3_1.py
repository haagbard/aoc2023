import re

file = 'aoc2023/day3/input.txt'

with open(file, 'r') as file:
    lines = file.read().splitlines()

part_numbers = []

for index, line in enumerate(lines):
    if index != 0:
        prev_index_line = lines[index - 1]
    else:
        prev_index_line = 'N/A'
    if index != len(lines) - 1:
        next_index_line = lines[index + 1]
    else:
        next_index_line = 'N/A'
    
    numbers_re = r"(\d+)"
    all_numbers = re.findall(numbers_re, line)

    last_index = 0

    for crnt_number in all_numbers:
        #all_non_words_re = r"([^a-zA-Z0-9\.\n])"
        no_and_dots_re = r"([^0-9\.\n])"
        
        start_index = line.index(crnt_number, last_index)
        end_index = start_index + len(crnt_number)

        last_index = end_index

        start_offset_index = start_index - 1
        end_offset_index = end_index + 1
        if start_offset_index < 0:
            start_offset_index = 0
        if end_offset_index >= len(line):
            end_offset_index = end_offset_index - 1

        part = False

        # Line above
        if prev_index_line != 'N/A':
            sub_str = prev_index_line[start_offset_index:end_offset_index]
            if len(re.findall(no_and_dots_re, sub_str)) != 0:
                part = True
        # Line below
        if next_index_line != 'N/A':
            sub_str = next_index_line[start_offset_index:end_offset_index]
            if len(re.findall(no_and_dots_re, sub_str)) != 0:
                part = True
        # Current line
        sub_str = line[start_offset_index:end_offset_index]
        if len(re.findall(no_and_dots_re, sub_str)) != 0:
            part = True

        if all_numbers[0] == '699':
            print('break..')

        #if crnt_number in ['795','940','539','491']:
        #    print('break..')

        if index == 139:
            print('break..')

        if part:
            part_numbers.append(crnt_number)
        #else:
        #    print('debug')

sum = 0

for part_number in part_numbers:
    sum += int(part_number)

print(sum)