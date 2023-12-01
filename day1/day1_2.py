with open('aoc2023/day1/input.txt', 'r') as file:
    lines = file.read().splitlines()
#with open('aoc2023/day1/training_data2.txt', 'r') as file:
#    lines = file.read().splitlines()

valid_digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

digits = []

for line in lines:
    first_digit = -1
    last_digit = -1
    for i in range(0, len(line)):
        if first_digit != -1:
            break
        x = line[i]
        if x.isdigit():
            first_digit = x
        else:
            for valid_digit in valid_digits:
                maybe_digit = line[i:i+len(valid_digit)]
                if maybe_digit == valid_digit:
                    first_digit = valid_digits.index(valid_digit) + 1
    for i in range(len(line)-1,-1,-1):
        if last_digit != -1:
            break
        x = line[i]
        if x.isdigit():
            last_digit = x
        else:
            for valid_digit in valid_digits:
                maybe_digit = line[i:i+len(valid_digit)]
                if maybe_digit == valid_digit:
                    last_digit = valid_digits.index(valid_digit) + 1
    digit = int(f'{first_digit}{last_digit}')
    digits.append(digit)

sum = 0

for digit in digits:
    sum += digit

print(f'Final sum: {sum}')