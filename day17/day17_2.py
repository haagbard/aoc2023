import heapq

file = 'aoc2023/day17/input.txt'

G = {i + j*1j: int(c) for i,r in enumerate(open(file))
                      for j,c in enumerate(r.strip())}

with open(file, 'r') as file:
    lines = file.read().splitlines()

def in_range(position, grid):
    return position[0] in range(len(grid[0])) and position[1] in range(len(grid))

def dijkstra(min_steps, max_steps, grid):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    # weight, x, y, not_allowed_direction
    paths = [(0,0,0,-1)] # Start value
    visited_paths = []

    weights = {}

    while paths:
        weight, x, y, no_direction = heapq.heappop(paths)

        if x == len(grid[0]) - 1 and y == len(grid) - 1:
            return weight
        if (x, y, no_direction) in visited_paths:
            continue
        visited_paths.append((x,y,no_direction))

        for direction in range(4):
            weight_increase = 0

            if direction == no_direction or (direction + 2) % 4 == no_direction:
                continue
            for distance in range(1, max_steps + 1):
                new_x = x + directions[direction][0] * distance
                new_y = y + directions[direction][1] * distance
                if in_range((new_y, new_x), grid):
                    weight_increase += grid[new_y][new_x]
                    if distance < min_steps:
                        continue
                    new_weight = weight + weight_increase
                    if weights.get((new_x, new_y, direction), 1e100) <= new_weight:
                        continue
                    weights[(new_x, new_y, direction)] = new_weight
                    heapq.heappush(paths, (new_weight, new_x, new_y, direction))

def f(min, max, end=[*G][-1], x=0):
    todo = [(0,0,0,1), (0,0,0,1j)]
    seen = set()

    while todo:
        val, _, pos, dir = heapq.heappop(todo)

        if (pos==end): return val
        if (pos, dir) in seen: continue
        seen.add((pos,dir))

        for d in 1j/dir, -1j/dir:
            for i in range(min, max+1):
                if pos+d*i in G:
                    v = sum(G[pos+d*j] for j in range(1,i+1))
                    heapq.heappush(todo, (val+v, (x:=x+1), pos+d*i, d))

grid = []

for line in lines:
    tmp_list = list(line)
    tmp_list_i = []
    for x in tmp_list:
        tmp_list_i.append(int(x))
    grid.append(tmp_list_i)

min_steps = 4
max_steps = 10

sum = dijkstra(min_steps,max_steps,grid)

print(sum)