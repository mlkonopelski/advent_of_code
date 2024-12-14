from collections import defaultdict

rules_after = defaultdict(list)
rules_prior = defaultdict(list)
updates = []

with open('2024/5/data') as f:

    text = f.readlines()
    for line in text:
        if line == '\n':
            continue
        if '|' in line:
            k, v = [int(r) for r in line.rstrip().split('|')]
            rules_after[k].append(v)
            rules_prior[v].append(k)
        else:
            updates.append([int(r) for r in line.rstrip().split(',')])

correct_updates = []

for update in updates:
    i = 0 
    broken = False
    while i < len(update):
        # check priors
        for j in range(0, i):
            if update[i] in rules_after and update[j] in rules_after[update[i]]:
                broken = True
                break
        if broken:
            break
        # check afters:
        for j in range(i+1, len(update)):
            if update[i] in rules_prior and update[j] in rules_prior[update[i]]:
                # contradict prior rule
                broken = True
                break
        if broken:
            break

        i+=1
        
    # no rules broken
    if not broken:
        correct_updates.append(update)

total_sum = 0
for cu in correct_updates:
    total_sum += cu[len(cu) // 2]

print(total_sum)


## Quicker solution
with open('2024/5/data') as f:
    data = f.read().strip()

rules_raw, updates_raw = data.split('\n\n')

rules = defaultdict(set)
for rule in rules_raw.split('\n'):
    x, y = rule.split('|')
    x, y = int(x), int(y)
    rules[y].add(x)

ans = 0
for update in updates_raw.split('\n'):
    update = [int(x) for x in update.split(',')]
    ok = True
    for i, x in enumerate(update):
        for j, y in enumerate(update):
            if i < j and y in rules[x]:
                ok = False
    if ok:
        ans += update[len(update) // 2]

print(ans)