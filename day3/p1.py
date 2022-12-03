sacks = []
with open('./in.txt') as file:
    for line in file:
        line = line.split('\n')[0]
        sacks.append(line)

s = 'abcdefghijklmnopqrstuvwxyz'
S = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase = {}
uppercase = {}
for i, e in enumerate(s):
    lowercase[e] = i+1
for i, e in enumerate(S):
        uppercase[e] = 26+i+1

total = 0
for sack in sacks:
    
    first, second = sack[:len(sack)//2], sack[len(sack)//2:]
    item = ''.join(set(first).intersection(second))

    if item in s: total += lowercase[item]
    elif item in S: total += uppercase[item]


print(total)
