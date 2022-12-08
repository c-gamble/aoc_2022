def greatest(array, e):
    for i in array:
        if i >= e: return False
    return True

grid = []
with open('./in.txt') as file:
    for line in file:
        row = []
        line = line.split('\n')[0]
        for i in range(len(line)): row.append(int(line[i]))
        grid.append(row)

c = 2*len(grid) + 2*len(grid[0]) - 4

def scenic(r, c):
    u = []
    d = []
    l = []
    ri = []

    for i in range(0, r): u.append(grid[i][c])
    for i in range(r+1, len(grid)): d.append(grid[i][c])
    for i in range(0, c): l.append(grid[r][i])
    for i in range(c+1, len(grid[r])): ri.append(grid[r][i])

    
    t = grid[r][c]

    uc = 0
    if not greatest(u, t):
        if not len(u) > 0:
            None
        elif t <= min(u): uc += 1
        else: 
            while uc < len(u) and len(u) > 0:
                if t > u[len(u)-1-uc]: uc += 1
                else: break
            uc += 1
    else: uc = len(u)
    
    dc = 0
    if not greatest(d, t):
        if not len(d) > 0:
            None
        elif t <= min(d): dc += 1
        else:
            while dc < len(d) and len(d) > 0:
                if t > d[dc]: dc += 1
                else: break
            dc += 1
    else: dc = len(d)

    lc = 0
    if not greatest(l, t):
        if not len(l) > 0:
            None
        elif t <= min(l): lc += 1
        else:
            while lc < len(l) and len(l) > 0:
                if t > l[len(l)-1-lc]: lc += 1
                else: break
            lc += 1
    else: lc = len(l)

    rc = 0
    if not greatest(ri, t):
        if not len(ri) > 0:
            None
        elif t <= min(ri): rc += 1
        else:
            while rc < len(ri) and len(ri) > 0:
                if t > ri[rc]: rc += 1
                else: break
            rc += 1
    else: rc = len(ri)  
    
    return rc*dc*lc*uc
ans = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        ans = max(ans, scenic(i, j))

print(ans)
