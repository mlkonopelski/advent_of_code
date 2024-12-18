import numpy as np
from collections import defaultdict

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


def search_loop(map, start, debug=False):

    i, j = start
    path = defaultdict(list)

    while (i<max_rows-1 and i > 0) and (j<max_columns-1 and j > 0):

        # which way we go?
        looking = map[i, j].item()
        p =  str((i,j))
        if path.get(p) and looking in path.get(p):
            return True 
        else:
            path[p].append(looking)

        step = decide_way(looking, (i, j))

        # print(f'pos: {i, j} looking: {looking} step: {step}')
        if map[step].item() == '#' or map[step].item() == 'O':
            looking = turn_side[looking]
            map[i, j] = looking
        else:
            i, j = step
            map[i, j] = looking
    
    return False

positions = 0

for m in range(max_rows):
    for n in range(max_columns):
        if map[m, n] == '.':
            print(f'processing: ({m,n})')
            temp_map = map.copy()
            temp_map[m, n] = 'O'
            positions += search_loop(temp_map, start=(i,j))
    
print(positions)