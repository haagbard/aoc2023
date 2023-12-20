import re
import copy

file = 'aoc2023/day20/input.txt'

with open(file, 'r') as file:
    lines = file.read().splitlines()

# name: (target, signal_type)
broadcaster = {}
# name: {target, state}
flip_flops = {}
# name: {target, previous_signal}
conjunctions = {}
conjunction_input_states = {}

def check_signal(conjunction_name):
    signal = 0
    all_states = conjunction_input_states[conjunction_name]
    for data in all_states:
        state = all_states[data]
        if state == 0:
            signal = 1
    return signal

for line in lines:
    if line.startswith('broadcaster -> '):
        line = line[len('broadcaster -> '):]
        destinations = line.split(', ')
        for i, d in enumerate(destinations):
            broadcaster['bc' + str(i)] = (d, 0) 
    elif line.startswith('%'):
        flip_flops_re = r'%(\w+) -> (.*)'
        res = re.findall(flip_flops_re, line)[0]
        name = res[0]
        targets = res[1]
        targets = targets.split(', ')
        targets_dict = {}
        for t in targets:
            targets_dict[t] = 0
        flip_flops[name] = targets_dict
    elif line.startswith('&'):
        conjunction_re = r'&(\w+) -> (.*)'
        res = re.findall(conjunction_re, line)[0]
        name = res[0]
        targets = res[1]
        targets = targets.split(', ')
        targets_dict = {}
        for t in targets:
            targets_dict[t] = 0
        conjunctions[name] = targets_dict

for conjunction in conjunctions:
    conjunction_input_states[conjunction] = {}

for flip_flop in flip_flops:
    data = flip_flops[flip_flop]
    for target in data:
        if target in conjunctions:
            conjunction_data = conjunction_input_states[target]
            conjunction_data[flip_flop] = 0
            conjunction_input_states[target] = conjunction_data
nodes = []

low_signals = 0
high_signals = 0

# Begin loop
for i in range(0, 1000):

    # button press, counts as low
    low_signals += 1

    for b in broadcaster:
        nodes.append(b)

    while len(nodes) > 0:
        node = nodes.pop(0)
        if ' ' in node:
            splitted = node.split()
            signal_sent = int(splitted[1])
            node = splitted[0]
            sender = splitted[2]
        if node.startswith('bc'):
            # Broadcaster
            data = broadcaster[node]
            target = data[0]
            signal = data[1]
            if signal == 0:
                low_signals += 1
            else:
                high_signals += 1
            nodes.append(f'{target} {signal} {node}')
        elif node in flip_flops:
            data_dict = flip_flops[node]
            new_data_dict = copy.deepcopy(data_dict)
            for target in data_dict:
                signal = data_dict[target]
                if signal_sent == 0:
                    if signal == 0: 
                        new_signal = 1
                        high_signals += 1
                    else:
                        new_signal = 0
                        low_signals += 1
                    new_data_dict[target] = new_signal
                    nodes.insert(0, f'{target} {new_signal} {node}')
            flip_flops[node] = new_data_dict
        elif node in conjunctions:
            data_dict = conjunctions[node]
            new_data_dict = copy.deepcopy(data_dict)

            conjunction_input_state = conjunction_input_states[node]
            conjunction_input_state[sender] = signal_sent
            conjunction_input_states[node] = conjunction_input_state

            signal_to_send = check_signal(node)

            for target in data_dict:
                if signal_to_send == 0:
                    low_signals += 1
                else:
                    high_signals += 1
                nodes.insert(0, f'{target} {signal_to_send} {node}')

sum = high_signals * low_signals

print(sum)