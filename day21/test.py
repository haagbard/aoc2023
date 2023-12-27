import copy

steps = 50

lines = ['...............','---------------','-------S-------','---------------','--------------|',
         '|--------------','---------------','---------------','---------------',',,,,,,,,,,,,,,,']

def replacer(s, newstring, index, nofail=False):
    if not nofail and index not in range(len(s)):
        raise ValueError("index outside given string")
    if index < 0:  # add it to the beginning
        return newstring + s
    if index > len(s):  # add it to the end
        return s + newstring
    return s[:index] + newstring + s[index + 1:]

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == 'S':
            start_pos = (x, y)

for line in lines:
    print(line)

lines_origin = copy.deepcopy(lines)

print('------')

# Replace 'S' with '.'
lines_origin[start_pos[1]] = replacer(lines_origin[start_pos[1]], '.', start_pos[0])

# Expand Y
while len(lines) - steps < 0:
    for y_pos in range(0, len(lines_origin)):
        new_line_append = lines_origin[y_pos]
        lines.insert(y_pos, new_line_append)
        lines.append(new_line_append)

# Expand X
while len(lines[0]) - steps < 0:
    for y_pos in range(0, len(lines)):
        line = lines[y_pos]
        original_position = y_pos % (len(lines_origin))
        new_line_append = lines_origin[original_position]
        lines[y_pos] = f'{new_line_append}{line}{new_line_append}'

# Should be expanded now

for line in lines:
    print(line)
