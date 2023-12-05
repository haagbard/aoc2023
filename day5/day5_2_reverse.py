import re
import sys
from alive_progress import alive_bar

seeds = {}

def find_next(dst, value, data):
    final_location_data = 0
    for crnt_key in data:
        if crnt_key.endswith(f'-{dst}'):
            crnt_data = data[crnt_key]
            src = crnt_key.split('-')[0]

            new_value = None
            
            for key in crnt_data:
                data_values = crnt_data[key]
                src_val = data_values[0]
                dst_val = data_values[1]
                increment_val = data_values[2]
                if value >= dst_val and value < dst_val + increment_val:
                    tmp = value - dst_val
                    new_value = src_val + tmp
                    break

            if new_value == None:
                new_value = value

            if src == 'seed':
                final_location_data = new_value
                break
            return find_next(src, new_value, data)
    return final_location_data

file = 'aoc2023/day5/input.txt'

full_file_content = ''

with open(file, 'r') as file:
    full_file_content = file.read()
    lines = full_file_content.splitlines()

seeds_re = r"(\d+\s\d+)"
digits_re = r"(\d+)"
map_re = r"(\w+)-to-(\w+) map:"

data = {}

for line in lines:
    if line.startswith('seeds: '):
        all_seed_pairs = re.findall(seeds_re, line)
        for seed_pair in all_seed_pairs:
            nums = re.findall(digits_re, seed_pair)
            seeds[int(nums[0])] = int(nums[1])
        break

all_maps = re.findall(map_re, full_file_content)
for maps in all_maps:
    src, dst = maps
    match_re = f'{src}-to-{dst} map:\n[(\d+)\s]+'
    matches = re.findall(match_re, full_file_content)
    matches_split = matches[0].split('\n')

    tmp_data = {}

    counter = 0

    for m in matches_split:
        if re.match(r"(\d+)", m):
            all_numbers = re.findall(digits_re, m)
            src_range = int(all_numbers[1])
            dst_range = int(all_numbers[0])
            increment = int(all_numbers[2])
            tmp_data[counter] = [src_range, dst_range, increment]
            counter += 1
    data[f'{src}-{dst}'] = tmp_data

lowest_no = []

max = 145492041
with alive_bar(max) as bar:
    for location in range(0,max): # It's not higher
        seed = find_next('location', location, data)
        for tmp_seed_key in seeds:
            seed_incr = seeds[tmp_seed_key]
            if seed >= tmp_seed_key and seed < tmp_seed_key + seed_incr:
                print(f'seed: {seed}, location: {location}')
                sys.exit(1)
        bar()