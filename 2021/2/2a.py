with open('2a_data.txt') as f:
    horizontal = 0
    depth = 0
    for line in f:
        direction = line.split()[0]
        value = int(line.split()[1])
        print(f'|{direction}|, {value}')
        if direction == 'forward':
            horizontal += value
        elif direction == 'up':
            depth -= value
        elif direction == 'down':
            depth += value

    print(f'horizontal= {horizontal}')
    print(f'depth={depth}')
    print(f'multiplication={horizontal*depth}')