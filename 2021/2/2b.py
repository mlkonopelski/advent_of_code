with open('2a_data.txt') as f:
    horizontal = 0
    depth = 0
    aim = 0
    for line in f:
        direction = line.split()[0]
        value = int(line.split()[1])
        print(f'|{direction}|, {value}')
        if direction == 'forward':
            horizontal += value
            depth = depth + (aim * value)
            print(horizontal, depth)
        elif direction == 'up':
            aim -= value
            print(aim)
        elif direction == 'down':
            aim += value
            print(aim)

    print(f'horizontal= {horizontal}')
    print(f'depth={depth}')
    print(f'multiplication={horizontal*depth}')