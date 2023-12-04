import re

file = 'aoc2023/day4/input.txt'

with open(file, 'r') as file:
    lines = file.read().splitlines()

card_match_re = r"Card.+(\d+):"
numbers_re = r"(\d+)"

cards = {}

for i in range(0,len(lines)):
    cards[i+1] = 1

#print(cards)

sum = 0

for card in cards:
    card_index = card - 1 # Maps card to lines
    line = lines[card_index]
    no_of_cards = cards[card]
    for i in range(0, no_of_cards):
        winners_and_numbers = re.sub(card_match_re,'',line)
        winning_numbers_raw = winners_and_numbers.split("|")[0]
        played_numbers_raw = winners_and_numbers.split("|")[1]

        winning_numbers = re.findall(numbers_re,winning_numbers_raw)
        played_numbers = re.findall(numbers_re,played_numbers_raw)

        wins = 0
        for played_number in played_numbers:
            if played_number in winning_numbers:
                wins += 1
        
        for j in range(1, wins + 1):
            card_no = j + card
            card_total_value = cards[card_no]
            card_total_value += 1
            cards[card_no] = card_total_value

for card in cards:
    sum += cards[card]

print(sum)

#print(cards)