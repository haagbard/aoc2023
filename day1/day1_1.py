import re

file = 'aoc2023/day1/input.txt'

with open(file, 'r') as file:
    lines = file.read().splitlines()

digits_re = r"(\d)"

digits = []

for line in lines:
    all_digits = re.findall(digits_re,line)
    digit = int(f'{all_digits[0]}{all_digits.pop()}')
    digits.append(digit)

sum = 0

for digit in digits:
    sum += digit

print(f'Final sum: {sum}')