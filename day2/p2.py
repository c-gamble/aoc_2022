rounds = []

with open('./in.txt') as file:
    for line in file:
        line = line.split('\n')[0]
        mvs = line.split(' ')
        rounds.append(mvs)
l = {'A': 'Z', 'B': 'X', 'C': 'Y'}
d = {'A':'X', 'B':'Y', 'C':'Z'}
w = {'A': 'Y', 'B':'Z', 'C':'X'}
s = {'X': 1, 'Y': 2, 'Z': 3}


total = 0
for round in rounds:
    if round[1] == 'X': #lose
        total += s[l[round[0]]]
    elif round[1] == 'Y': #draw
        total += s[d[round[0]]] + 3
    elif round[1] == 'Z': #win
        total += s[w[round[0]]] + 6
print(total)
