rounds = []

with open('./in.txt') as file:
    
    for line in file:
        line = line.split('\n')[0]
        mvs = line.split(' ')
        rounds.append(mvs)


values = {'X': 1, 'Y': 2, 'Z': 3}
draw = {'A': 'X', 'B':'Y', 'C':'Z'}
win = {'A': 'Y', 'B':'Z', 'C': 'X'}

total = 0
for round in rounds:
    total += values[round[1]]
    if round[1] == draw[round[0]]: total += 3
    elif round[1] == win[round[0]]: total += 6

print(total)
