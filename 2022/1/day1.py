# who has te most calories?
calories = []
with open('2022/day1.txt') as f:
    calories = ''.join(f.readlines()).split('\n\n')

print(max([sum([int(c) for c in cal.split('\n')]) for cal in calories]))
