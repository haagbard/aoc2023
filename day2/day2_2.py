import re

with open('aoc2023/day2/input.txt', 'r') as file:
    lines = file.read().splitlines()
#with open('aoc2023/day2/training_data.txt', 'r') as file:
#    lines = file.read().splitlines()

game_match = r"Game.(\d+):"
color_match = r"(\d+) (\w+)"

powers = []

for line in lines:
    game_res = re.search(game_match, line)
    game = int(game_res.group(1))

    line = re.sub(game_match,'',line)

    max = {'red':0,'green':0,'blue':0}

    hands = line.split(';')
    for hand in hands:
        hand = hand.strip()
        colors = hand.split(',')
        for color in colors:
            color = color.strip()
            color_res = re.search(color_match,color)
            amount = int(color_res.group(1))
            crnt_color = color_res.group(2)
            if max[crnt_color] < amount:
                max[crnt_color] = amount

    tmp_power = 1
    for color in max:
        tmp_power *= max[color]

    powers.append(tmp_power)

sum = 0

for power in powers:
    sum += power

print(sum)