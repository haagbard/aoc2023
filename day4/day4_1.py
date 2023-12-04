import re

file = 'aoc2023/day4/input.txt'

with open(file, 'r') as file:
    lines = file.read().splitlines()

card_match_re = r"Card.+(\d+):"
numbers_re = r"(\d+)"

sum = 0

for line in lines:
    winners_and_numbers = re.sub(card_match_re,'',line)
    winning_numbers_raw = winners_and_numbers.split("|")[0]
    played_numbers_raw = winners_and_numbers.split("|")[1]

    winning_numbers = re.findall(numbers_re,winning_numbers_raw)
    played_numbers = re.findall(numbers_re,played_numbers_raw)

    points = 0
    for played_number in played_numbers:
        if played_number in winning_numbers:
            if points == 0:
                points = 1
            else:
                points = points * 2
    sum += points

print(sum)