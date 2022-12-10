data = []

with open('./day10/in.txt') as file:
    for line in file:
        data.append(line.split('\n')[0].split(" "))

c = 1
x = 1
out = ["" for _ in range(6)]
sprite = 1

for instr in data:
    if instr[0] == "noop": #execute crt once
        if sprite == (c-1) % 40 or sprite + 1 == (c-1) % 40 or sprite - 1 == (c-1) % 40: 
            if  c <= 40: out[0] += "#"
            elif c <= 80: out[1] += "#"
            elif c <= 120: out[2] += "#"
            elif c <= 160: out[3] += "#"
            elif c <= 200: out[4] += "#"
            elif c <= 240: out[5] += "#"
        else: 
            if  c <= 40: out[0] += "."
            elif c <= 80: out[1] += "."
            elif c <= 120: out[2] += "."
            elif c <= 160: out[3] += "."
            elif c <= 200: out[4] += "."
            elif c <= 240: out[5] += "."
        c += 1
        continue
    else: #execute crt twice
        x += int(instr[1])

        for _ in range(2):  
            if sprite == (c-1) % 40 or sprite + 1 == (c-1) % 40 or sprite - 1 == (c-1) % 40: 
                if  c <= 40: out[0] += "#"
                elif c <= 80: out[1] += "#"
                elif c <= 120: out[2] += "#"
                elif c <= 160: out[3] += "#"
                elif c <= 200: out[4] += "#"
                elif c <= 240: out[5] += "#"
            else:
                if  c <= 40: out[0] += "."
                elif c <= 80: out[1] += "."
                elif c <= 120: out[2] += "."
                elif c <= 160: out[3] += "."
                elif c <= 200: out[4] += "."
                elif c <= 240: out[5] += "."
            c += 1
        
        sprite = x

for e in out: print(e)