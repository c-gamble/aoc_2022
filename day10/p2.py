data = []

with open('./day10/in.txt') as file:
    for line in file:
        data.append(line.split('\n')[0].split(" "))

c = 1
x = 1
ans = ""
sprite = 1

for instr in data:
    if c % 40 == 1 and c > 2: ans += "\n"
    if instr[0] == "noop": 
        if  (c-1) % 40 in range(sprite-1, sprite+2): 
            ans += "#"
        else: 
            ans += "."
        c += 1
        continue
    else: 
        x += int(instr[1])
        for _ in range(2):  
            if c % 40 == 1 and c > 2: ans += "\n"
            if  (c-1) % 40 in range(sprite-1, sprite+2): 
                ans += "#"
            else:
                ans += "."
            c += 1   
        sprite = x
print(ans)

