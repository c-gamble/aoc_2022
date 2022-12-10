data = []

with open('./day10/in.txt') as file:
    for line in file:
        data.append(line.split('\n')[0].split(" "))

c = 0
x = 1
ans = []
for instr in data:
    print(c, x)
    if c == 19 or c == 59 or c== 99 or c == 139 or c == 179 or c == 219:
        ans.append((c+1)*x)
    if instr[0] == "noop": 
        c += 1
        continue
    else:
        c += 2
        if c - 1 == 219 or c - 1 == 19 or c - 1 == 59 or c - 1 == 99 or c - 1 == 139 or c - 1 == 179:
            ans.append(c*x)
        x += int(instr[1])
print(sum(ans))