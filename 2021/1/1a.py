count = 0
previous = 1e100

with open('1a_data.txt') as f:
    for line in f:
        if int(line) > previous:
            count+=1
        previous = int(line)

print(count)