file = 'aoc2023/day15/input.txt'

with open(file, 'r') as file:
    lines = file.read().splitlines()

lines = lines[0].split(',')

sum = 0

for line in lines:
    line_sum = 0
    for tmpchar in line:
        ascii_value = int(''.join(str(ord(c)) for c in tmpchar))
        ascii_value += line_sum
        value = ascii_value * 17
        remainder = value % 256
        line_sum = remainder
    sum += line_sum

print(sum)