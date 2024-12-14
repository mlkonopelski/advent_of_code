rules_after = {}
rules_prior = {}
updates = []

with open('2024/5/data') as f:

    text = f.readlines()
    for line in text:
        if line == '\n':
            continue
        if '|' in line:
            k, v = [int(r) for r in line.rstrip().split('|')]
            if rules_after.get(k):
                rules_after[k].append(v)
            else:
                rules_after[k] = [v]

            if rules_prior.get(v):
                rules_prior[v].append(k)
            else:
                rules_prior[v] = [k]
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