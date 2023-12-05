import re
from threading import Thread

def find_next(src, value, data):
    final_location_data = 0
    for crnt_key in data:
        if crnt_key.startswith(f'{src}-'):
            crnt_data = data[crnt_key]
            dst = crnt_key.split('-')[1]

            new_value = None
            
            for key in crnt_data:
                data_values = crnt_data[key]
                src_val = data_values[0]
                dst_val = data_values[1]
                increment_val = data_values[2]
                if value >= src_val and value < src_val + increment_val: # Faster
                #if value in range(src_val, src_val + increment_val): # Slower
                    tmp = value - src_val
                    new_value = dst_val + tmp

            if new_value == None:
                new_value = value

            if dst == 'location':
                final_location_data = new_value
                break
            return find_next(dst, new_value, data)
    return final_location_data

class CustomThread(Thread):
    def __init__(self, seed, value, data):
        Thread.__init__(self)
        self.seed = seed
        self.value = value
        self.data = data
        self.lowest_no = None

    def run(self):
        print(f'Starting {self.name}...')
        lowest_no_tmp = None
        for seed_val in range(self.seed, self.seed + self.value):
            location = find_next('seed', seed_val, self.data)
            if lowest_no_tmp == None:
                lowest_no_tmp = location
            if location < lowest_no_tmp:
                lowest_no_tmp = location
        self.lowest_no = lowest_no_tmp

file = 'aoc2023/day5/input.txt'

full_file_content = ''

with open(file, 'r') as file:
    full_file_content = file.read()
    lines = full_file_content.splitlines()

seeds_re = r"(\d+\s\d+)"
digits_re = r"(\d+)"
map_re = r"(\w+)-to-(\w+) map:"

seeds = {}
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
threads = []

for seed in seeds:
    seed_value = seeds[seed]
    threads.append(CustomThread(seed, seed_value, data))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
    lowest_no.append(thread.lowest_no)

print(lowest_no)
print(min(lowest_no))