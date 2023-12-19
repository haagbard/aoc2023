import re

file = 'aoc2023/day19/input.txt'

with open(file, 'r') as file:
    lines = file.read().splitlines()

workflows = {}
ratings = []

def find_workflow(workflow_name, x, m, a, s):
    if workflow_name == 'A':
        return True
    elif workflow_name == 'R':
        return False
    
    workflow_re = r'(\w)(<|>)(\d+):(\w+)'
    final_instruktion_re = r',(A|R|\w{2,3})'

    data = {'x':x, 'm':m, 'a':a, 's':s}

    workflow = workflows[workflow_name]
    instructions = re.findall(workflow_re,workflow)

    for instruction in instructions:
        letter = instruction[0]
        compare = instruction[1]
        number = int(instruction[2])
        instruction = instruction[3]
        letter_number = data[letter]
        if compare == '<':
            if letter_number < number:
                return find_workflow(instruction, x, m, a, s)
        elif compare == '>':
            if letter_number > number:
                return find_workflow(instruction, x, m, a, s)
    
    final_instruction = re.findall(final_instruktion_re, workflow)[0]
    return find_workflow(final_instruction, x, m, a, s)


workflow_re = r'(\w+){(.*)}'
blank_line_index = 0

for index, line in enumerate(lines):
    if line == '':
        blank_line_index = index
        break
    worksflows_data = re.findall(workflow_re, line)[0]
    workflows[worksflows_data[0]] = worksflows_data[1]

for index in range(blank_line_index + 1, len(lines)):
    ratings.append(lines[index])

ratings_re = r'{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}'

sum = 0

for rating in ratings:
    ratings_data = re.findall(ratings_re, rating)[0]
    x = int(ratings_data[0])
    m = int(ratings_data[1])
    a = int(ratings_data[2])
    s = int(ratings_data[3])
    passed = find_workflow('in', x, m, a, s)
    if passed:
        sum += x + m + a + s

print(sum)

#print(worksflows)
#print(ratings)