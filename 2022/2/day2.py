# Opponent: A - Rock B - paper C - scisors
# Me: X - Rock, Y - Paper, and Z - Scissors

# 1 for Rock, 2 for Paper, and 3 for Scissors
# 0 if you lost, 3 if the round was a draw, and 6 if you won
with open('2022/day2.txt') as f:
    competition = f.readlines()

def rps(h1, h2):
    if (h1 == 'A' and h2 == 'X') or (h1 == 'B' and h2 == 'Y') or (h1 == 'C' and h2 == 'Z'):
        return 6
    elif (h1 == 'A' and h2 =='Y') or (h1 == 'C' and h2 == 'X'):
        return 3
    else:
        return 0

hand_score = {
    'X':1,
    'Y':2,
    'Z':3
}

total_score = 0

for c in competition:
    c = c.rstrip().split(' ')
    result = rps(c[0], c[1])
    hand = hand_score[c[1]]
    print(c[0], c[1], result, hand)
    total_score += (result + hand)

print(total_score)