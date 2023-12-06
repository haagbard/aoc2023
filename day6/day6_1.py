import re

def calculate_distance(time_held_button, race_time):
    boat_travel_time = race_time - time_held_button
    return boat_travel_time * time_held_button

file = 'aoc2023/day6/input.txt'

with open(file, 'r') as file:
    lines = file.read().splitlines()

digits_re = r"(\d+)"

race_time = []
distances = []

for line in lines:
    if line.startswith('Time: '):
        race_time.extend(re.findall(digits_re,line))
    elif line.startswith('Distance: '):
        distances.extend(re.findall(digits_re,line))

wins = {}

for index, time in enumerate(race_time):
    wins[index] = 0
    vr_distance = int(distances[index])
    time = int(time)
    for time_held_button in range(0, time + 1):
        if calculate_distance(time_held_button, time) > vr_distance:
            value = wins[index]
            value += 1
            wins[index] = value

sum = 1

for win in wins:
    value = wins[win]
    sum *= value

print(sum)