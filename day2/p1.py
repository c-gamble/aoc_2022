rounds = []

with open('./in.txt') as file:
    
    for line in file:
        line = line.split('\n')[0]
        mvs = line.split(' ')
        rounds.append(mvs)

total = 0

for round in rounds:
    if round[1] == 'X': total += 1
    elif round[1] == 'Y': total += 2
    elif round[1] == 'Z': total += 3
    if (round[0] == 'A' and round[1] == 'X') or (round[0] == 'B' and round[1] == 'Y') or (round[0] == 'C' and round[1] == 'Z'): total += 3
    elif round[0] == 'A' and round[1] == 'Y': total += 6
    elif round[0] == 'A' and round[1] == 'Z': total += 0
    elif round[0] == 'B' and round[1] == 'X': total += 0
    elif round[0] == 'B' and round[1] == 'Z': total += 6
    elif round[0] == 'C' and round[1] == 'X': total += 6
    elif round[0] == 'C' and round[1] == 'Y': total += 0

print(total)
