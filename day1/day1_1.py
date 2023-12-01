with open('aoc2023/day1/input.txt', 'r') as file:
    lines = file.read().splitlines()
#with open('aoc2023/day1/training_data.txt', 'r') as file:
#    lines = file.read().splitlines()

digits = []

for line in lines:
    first_digit = -1
    last_digit = -1
    for x in line:
        if x.isdigit():
            first_digit = x
            break
    for x in reversed(line):
        if x.isdigit():
            last_digit = x
            break
    digit = int(f'{first_digit}{last_digit}')
    digits.append(digit)

sum = 0

for digit in digits:
    sum += digit

print(f'Final sum: {sum}')