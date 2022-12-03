
def return_common(s1, s2, s3):
    for char in s1:
        if char in s2 and char in s3: return char
sacks = []
with open('./in.txt') as file:
    group = []
    for line in file:
        line = line.split('\n')[0]
        group.append(line)
        if len(group) < 3: continue
        else:
            sacks.append(group)
            group = []

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
    item = return_common(sack[0], sack[1], sack[2])
    if item in s: total += lowercase[item]
    elif item in S: total += uppercase[item]
    

print(total)
