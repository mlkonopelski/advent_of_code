import re

with open('2024/3/data') as f:
    input_string = f.readlines()[0].rstrip()

pattern_remove = r"don't.*?do\(\)"
pattern_find = r"mul\((\d+),(\d+)\)"

cleaned_string = re.sub(pattern_remove, "", input_string)

sum = 0 
for x, y in re.findall(pattern_find, cleaned_string):
    sum += int(x) * int(y)

print(sum)