import string

with open('2022/day3.txt') as f:
    rucksacks = f.readlines()

l = string.ascii_lowercase + string.ascii_uppercase

letters = {}
for i, letter in enumerate(l):
    letters[letter] = i + 1
        
priority = 0
for r in rucksacks:
    middle = int(len(r) / 2)
    left_compartment = r[:middle]
    right_compartmnet = r[middle:]
    for c in left_compartment:
        if c in right_compartmnet:
            break
    priority += letters[c]
print(priority)