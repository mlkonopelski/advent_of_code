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

incorrect_updates = []

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
    if broken:
        incorrect_updates.append(update)

correct_updates = []
for inc_update in incorrect_updates:
    incorrect = True
    temp_update = inc_update.copy()
    i = 0
    corrected = False
    while i < len(temp_update):
        for j in range(i+1, len(temp_update)):
            if temp_update[i] in rules_prior and temp_update[j] in rules_prior[temp_update[i]]:
                i_v, j_v = temp_update[i], temp_update[j]
                temp_update[j], temp_update[i] = i_v, j_v
                corrected = True
                break
            corrected = False

        if corrected:
            i = 0 
        else:
            i+= 1
        
    correct_updates.append(temp_update)

print(correct_updates)


total_sum = 0
for cu in correct_updates:
    total_sum += cu[len(cu) // 2]

print(total_sum)