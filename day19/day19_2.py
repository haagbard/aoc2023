import re
import copy

file = 'aoc2023/day19/input.txt'

with open(file, 'r') as file:
    lines = file.read().splitlines()

workflows = {}
workflows_binary_order = {}
ratings = []

def get_next(instruction_name, intervalls):
    nodes = []
    workflow_re = r'(\w)(<|>)(\d+):(\w+),(A|R|\w{2,3}\d*)'

    workflow = workflows_binary_order[instruction_name]
    instruction = re.findall(workflow_re,workflow)[0]
    
    letter = instruction[0]
    compare = instruction[1]
    number = int(instruction[2])
    new_instruction = instruction[3]
    other_instruction = instruction[4]

    if compare == '<':
        interval = intervalls[letter]
        fmin = interval[0]
        fmax = number - 1
        nmin = number
        nmax = interval[1]
        if number in range(interval[0],interval[1]):
            intervalls[letter] = (fmin, fmax)
            next_intervall = copy.deepcopy(intervalls)
            next_intervall[letter] = (nmin, nmax)
            nodes = [(new_instruction, intervalls), (other_instruction, next_intervall)]
        else:
            nodes = [(other_instruction, intervalls)]
    else:
        interval = intervalls[letter]
        nmin = interval[0]
        nmax = number
        fmin = number + 1
        fmax = interval[1]
        if number in range(interval[0],interval[1]):
            intervalls[letter] = (fmin, fmax)
            next_intervall = copy.deepcopy(intervalls)
            next_intervall[letter] = (nmin, nmax)
            nodes = [(new_instruction, intervalls), (other_instruction, next_intervall)]
        else:
            nodes = [(other_instruction, intervalls)]
    
    return copy.deepcopy(nodes)

def binary_order():
    workflow_re = r'(\w)(<|>)(\d+):(\w+)'
    final_instruktion_re = r',(A|R|\w{2,3})'
    start_workflow = 'in'
    workflow_names = [start_workflow]
    workflow_names_fixed = []
    # Do a new grouping order, making it easier to follow
    while len(workflow_names) > 0:
        workflow_name = workflow_names.pop()
        workflow = workflows[workflow_name]
        instructions = re.findall(workflow_re,workflow)

        for index, instruction in enumerate(instructions):
            index = index + 1
            letter = instruction[0]
            compare = instruction[1]
            number = int(instruction[2])
            new_instruction = instruction[3]
            final_instruction = re.findall(final_instruktion_re, workflow)[0]
            if new_instruction not in workflow_names_fixed:
                if new_instruction != 'A' and new_instruction != 'R':
                    workflow_names.append(new_instruction)
            if final_instruction not in workflow_names_fixed:
                if final_instruction != 'A' and final_instruction != 'R':
                    workflow_names.append(final_instruction)

            workflow_names_fixed.append(new_instruction)
            workflow_names_fixed.append(final_instruction)

            if workflow_name != 'in':
                workflow_name_tmp = workflow_name + str(index)
            else:
                workflow_name_tmp = workflow_name
            if new_instruction != 'A' and new_instruction != 'R':
                for i in range(1, index + 1):
                    if new_instruction + str(i) not in workflows_binary_order:
                        new_instruction = new_instruction + str(i)
                        break
            if len(instructions) == index:
                if final_instruction != 'A' and final_instruction != 'R':
                    for i in range(1, index + 1):
                        if final_instruction + str(i) not in workflows_binary_order:
                            final_instruction = final_instruction + str(i)
                            break
            else:
                for i in range(1, index + 2):
                    if workflow_name + str(i) not in workflows_binary_order and workflow_name_tmp != workflow_name + str(i):
                        fi_name = workflow_name + str(i)
                        break
                    
                final_instruction = fi_name
                
            workflows_binary_order[workflow_name_tmp] = f'{letter}{compare}{number}:{new_instruction},{final_instruction}'
            


workflow_re = r'(\w+){(.*)}'

for index, line in enumerate(lines):
    if line == '':
        break
    worksflows_data = re.findall(workflow_re, line)[0]
    workflows[worksflows_data[0]] = worksflows_data[1]

max_v = 4000
min_v = 1

start_intervalls = {'x':(min_v, max_v), 'm':(min_v, max_v), 'a':(min_v, max_v), 's':(min_v, max_v)}

nodes = [('in', start_intervalls)]

moves_logged = []

binary_order()

while len(nodes) > 0:
    instruction, intervalls = nodes.pop(0)
    new_nodes = get_next(instruction, intervalls)
    new_nodes.reverse()
    for new_node in new_nodes:
        if new_node[0] == 'A' or new_node[0] == 'R':
            if new_node[0] == 'A':
                moves_logged.append(new_node[1])
        else:
            nodes.insert(0, (new_node[0], new_node[1]))

sum = 0

for move in moves_logged:
    x = move['x'][1] - move['x'][0] + 1
    m = move['m'][1] - move['m'][0] + 1
    a = move['a'][1] - move['a'][0] + 1
    s = move['s'][1] - move['s'][0] + 1
    sum += x * m * a * s

print(sum)