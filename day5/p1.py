stacks = []
stacks.append(['P', 'F', 'M', 'Q', 'W', 'G', 'R', 'T'])
stacks.append(['H', 'F', 'R'])
stacks.append(['P', 'Z', 'R', 'V', 'G', 'H', 'S', 'D'])
stacks.append(['Q', 'H', 'P', 'B', 'F', 'W', 'G'])
stacks.append(['P', 'S', 'M', 'J', 'H'])
stacks.append(['M', 'Z', 'T', 'H', 'S', 'R', 'P', 'L'])
stacks.append(['P', 'T', 'H', 'N', 'M', 'L'])
stacks.append(['F', 'D', 'Q', 'R'])
stacks.append(['D', 'S', 'C', 'N', 'L', 'P', 'H'])


file = open('./in.txt')
moves = []
for line in file:
    if line == '\n' or line[0] == ' ' or line[0] == '[': continue
    else:
        line = line.split('\n')[0]
        n = int(line.split('move ')[1].split(' ')[0])
        origin = int(line.split('from ')[1].split(' ')[0])
        destination = int(line.split('to ')[1].split(' ')[0])
        moves.append([n, origin, destination])

for move in moves:
    [n, origin, dest] = [*move]
    for _ in range(n):
        stacks[dest-1].append(stacks[origin-1].pop())
res = ''
for stack in stacks:
    res += stack[len(stack)-1]
print(res)
