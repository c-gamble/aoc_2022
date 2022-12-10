data = []
with open('./day10/in.txt') as file:
    for line in file:
        data.append(line.split('\n')[0].split(" "))
c = 1
x = 1
ans = []
for instr in data:
    if (c+20) % 40 == 0: 
        print(c, x, c*x, "noop")
        ans.append(c*x)
   
    if instr[0] == "noop": c += 1
    else:
        c += 2
        if (c+19) % 40 == 0: ans.append((c-1)*x)
        x += int(instr[1])
print(sum(ans))