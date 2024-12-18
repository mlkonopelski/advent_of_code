import numpy as np


with open('2024/6/data') as f:
    content = f.read().rstrip()

map = [list(line) for line in content.split('\n')]
map = np.array(map)
print(map)

# boundries
max_rows, max_columns = map.shape

# start 
start = np.where((map=='^') | (map == '>') | (map=='<') | (map == 'v'))
i, j = start[0].item(), start[1].item()

def decide_way(value, position):
    if value == '>':
        return (position[0], position[1] + 1)
    elif value == '<':
        return (position[0], position[1] - 1)
    elif value == 'v':
        return (position[0] + 1, position[1])
    elif value == '^':
        return (position[0] - 1, position[1])

turn_side = {
    '^': '>',
    '>': 'v',
    'v': '<',
    '<': '^'
}

def save_route(map, f_name= '2024/6/data.route'):

    with open(f_name, 'w') as f:
        map_list = map.tolist()
        map_str = '\n'.join([''.join(line) for line in map_list])
        f.write(map_str)


while (i<max_rows-1 and i > 0) and (j<max_columns-1 and j > 0):

    # which way we go?
    looking = map[i, j].item()
    step = decide_way(looking, (i, j))

    # print(f'pos: {i, j} looking: {looking} step: {step}')

    if map[step].item() == '#':
        map[i, j] = turn_side[looking]
    else:
        map[i, j] = 'X'
        i, j = step
        map[i, j] = looking

    # save_route(map)

    

# mark last position
map[i, j] = 'X'

# count X
print(np.count_nonzero(map=='X'))