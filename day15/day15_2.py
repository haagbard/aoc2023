file = 'aoc2023/day15/input.txt'

with open(file, 'r') as file:
    lines = file.read().splitlines()

lines = lines[0].split(',')

boxes = {}

def hash(input):
    line_sum = 0
    for tmpchar in input:
        ascii_value = int(''.join(str(ord(c)) for c in tmpchar))
        ascii_value += line_sum
        value = ascii_value * 17
        remainder = value % 256
        line_sum = remainder
    return line_sum

def insert_or_replace(box_index, key, value):
    if box_index in boxes:
        box_content = boxes[box_index]
    else:
        box_content = []
    replaced = False
    for x in range(0,len(box_content)):
        crnt_lens = box_content[x]
        if key in crnt_lens:
            del box_content[x]
            box_content.insert(x, f'{key} {value}')
            replaced = True
    if replaced == False:
        box_content.append(f'{key} {value}')
    boxes[box_index] = box_content  

def remove_value(box_index, key):
    if box_index in boxes:
        box_content = boxes[box_index]
    else:
        return 0
    to_remove = []
    for x in range(0,len(box_content)):
        crnt_lens = box_content[x]
        if key in crnt_lens:
            to_remove.insert(0,x)
    for x in to_remove:
        del box_content[x]
    boxes[box_index] = box_content

for line in lines:
    if '=' in line:
        key,value = line.split('=')
        box_index = hash(key)
        insert_or_replace(box_index, key, value)
    else:
        key = line.replace('-','')
        box_index = hash(key)
        remove_value(box_index, key)

sum = 0

for key in boxes:
    box_content = boxes[key]
    for x in range(0, len(box_content)):
        lens_key,lens_value = box_content[x].split()
        value = (key + 1) * (x + 1) * int(lens_value)
        sum += value

print(sum)