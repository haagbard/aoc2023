import re

def calculate_distance(time_held_button, race_time):
    boat_travel_time = race_time - time_held_button
    return boat_travel_time * time_held_button

file = 'aoc2023/day6/input.txt'

with open(file, 'r') as file:
    lines = file.read().splitlines()

digits_re = r"(\d+)"

race_time = ''
distance = ''

for line in lines:
    if line.startswith('Time: '):
        tmp_racetime = re.findall(digits_re,line)
        race_time = int(race_time.join(tmp_racetime))
    elif line.startswith('Distance: '):
        tmp_distance = re.findall(digits_re,line)
        distance = int(distance.join(tmp_distance))

wins = 0

for time_held_button in range(0, race_time + 1):
    if calculate_distance(time_held_button, race_time) > distance:
        wins += 1

print(wins)