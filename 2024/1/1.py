f_path = '2024/1/data.example'
f_path = '2024/1/data.1'

with open(f_path) as f:
    list_a = []
    list_b = []
    for line in  f.readlines():
        a, b = line.rstrip().split('   ')
        list_a.append(int(a))
        list_b.append(int(b))

list_a.sort(), list_b.sort()

diff = 0
for a, b in zip(list_a, list_b):
    diff += abs(a-b)

print(diff)

