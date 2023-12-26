x,y = (5,5)

steps = ((-1,0), (1,0), (0,-1), (0,1))

for step in steps:
    new_x = x + step[0]
    new_y = y + step[1]
    print(f'{new_x}, {new_y}')


