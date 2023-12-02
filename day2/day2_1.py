import re

with open('aoc2023/day2/input.txt', 'r') as file:
    lines = file.read().splitlines()
#with open('aoc2023/day2/training_data.txt', 'r') as file:
#    lines = file.read().splitlines()

game_match = r"Game.(\d+):"
color_match = r"(\d+) (\w+)"

max = {'red':12,'green':13,'blue':14}

allowed_games = []

for line in lines:
    to_much = False

    game_res = re.search(game_match, line)
    game = int(game_res.group(1))

    line = re.sub(game_match,'',line)

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
                to_much = True

    if to_much == False:
        allowed_games.append(game)

sum = 0

for allowed_game in allowed_games:
    sum += allowed_game

print(sum)