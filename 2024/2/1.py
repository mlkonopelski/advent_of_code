f_path = '2024/2/data.example'
f_path = '2024/2/data'

with open(f_path) as f:
    reports = []
    list_b = []
    for report in  f.readlines():
        reports.append(report.rstrip().split(' '))

safe = 0
for report in reports:
    safe_ = True
    diffs = [int(l2) - int(l1) for l1, l2 in zip(report[:-1], report[1:])]

    if all([diff > 0 and diff <= 3 for diff in diffs]) or all([diff < 0 and diff >= -3 for diff in diffs]):
        safe += 1

print(safe)