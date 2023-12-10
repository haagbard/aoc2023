import re

file = 'aoc2023/day9/input.txt'

with open(file, 'r') as file:
    lines = file.read().splitlines()

def next_sequence(numbers):
    ret_list = []
    for index, number in enumerate(numbers):
        next_index = index + 1
        if next_index == len(numbers):
            break
        ret_list.append(numbers[next_index] - number)
    return ret_list

def all_zeros(numbers):
    for number in numbers:
        if number != 0:
            return False
    return True

sum = 0

for line in lines:
    numbers_str = re.findall(r"(-*\d+)", line)
    numbers = []
    for num_str in numbers_str:
        numbers.append(int(num_str))

    seq_no = 0
    sequences = {seq_no: numbers}
    while all_zeros(sequences[seq_no]) == False:
        nums = next_sequence(sequences[seq_no])
        seq_no += 1
        sequences[seq_no] = nums

    for i in range(len(sequences),0,-1):
        index = i - 1
        this_seq = sequences[index]

        if index == 0:
            sum += this_seq[0]
        else:
            prev_seq = sequences[index-1]
            first_no = this_seq[0]
            first_prev_no = prev_seq[0]
            new_number = first_prev_no - first_no
            prev_seq = sequences[index-1]
            prev_seq.insert(0, new_number)
            sequences[index-1] = prev_seq

print(f'{sum}')