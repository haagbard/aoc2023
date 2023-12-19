import re

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

def count_it(input):
    filled = 0
    for line in input:
        for x in range(0, len(line)):
            if line[x] == '#':
                filled += 1
    return filled

def get_coordinates(x, y, direction, length):
    if direction == 'R':
        x = x + length
    elif direction == 'L':
        x = x - length
    elif direction == 'U':
        y = y - length
    elif direction == 'D':
        y = y + length
    return x, y

def run_shoelace(input):
    number_of_vertices = len(input)
    all_sums = []
    sum1 = 0
    sum2 = 0

    for i in range(0, number_of_vertices - 1):
        sum1 = sum1 + input[i][0] * input[i+1][1]
        sum2 = sum2 + input[i][1] * input[i+1][0]
        all_sums.append(sum1)
        all_sums.append(sum2)

    #Add xn.y1
    sum1 = sum1 + input[number_of_vertices-1][0]*input[0][1]   
    #Add x1.yn
    sum2 = sum2 + input[0][0]*input[number_of_vertices-1][1]   
    
    all_sums.append(sum1)
    all_sums.append(sum2)
    
    area = abs(sum1 - sum2) / 2
    return area

extract_re = r'\w\s\d+\s\(#(\w+)\)'

data = []

for index, line in enumerate(lines):
    data_line = re.findall(extract_re, line)
    data.append(data_line[0])

x, y = (0, 0)

directions = {0:'R', 1:'D', 2:'L', 3:'U'}

b = 0

output = []

for d in data:
    length = int(d[0:5], 16)
    direction = directions[int(d[5:6])]
    
    x, y = get_coordinates(x, y, direction, length)
    output.append((x, y))
    b += length

area = int(run_shoelace(output))

# Picks theorem
I = area + 1 - b / 2
sum = int(I) + b

print(sum)