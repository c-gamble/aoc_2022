file = open('./in.txt')
rows = []
moves = []
for line in file:
    if line == '\n':
        continue
    elif line[0] == ' ' or line[0] == '[':
        if "1" in line: continue
        line = line.split('\n')[0]

        row = []
        ptr = 0
        while ptr < len(line):
            if line[ptr] == '[':
                row.append(line[ptr+1])
                ptr += 1
                continue
            elif line[ptr] == ' ' and line[ptr+1] == ' ':
                row.append('')
                ptr += 4
                continue
            else: ptr += 1
        rows.append(row)
    else:
        line = line.split('\n')[0]
        n = int(line.split('move ')[1].split(' ')[0])
        origin = int(line.split('from ')[1].split(' ')[0])
        destination = int(line.split('to ')[1].split(' ')[0])
        moves.append([n, origin, destination])

stacks = []
col = 0
while col < len(rows[-1]):
    stack = []
    for row in rows:
        if row[col] != '': stack.append(row[col])
    stacks.append(list(reversed(stack)))
    col += 1

for move in moves:
    [n, origin_idx, dest_idx] = [*move]
    for _ in range(n):
        origin, dest = stacks[origin_idx-1], stacks[dest_idx-1]
        crate = origin.pop(-1)
        dest.append(crate)
res = ''
for stack in stacks:
    res += stack[-1]
print(res)
