import re

with open('2024/3/data') as f:
    input = f.readlines()[0].rstrip()

pattern = r"mul\((\d+),(\d+)\)"
total_sum = 0

for x,y in re.findall(pattern, input):
    total_sum += int(x)*int(y)

print(total_sum)