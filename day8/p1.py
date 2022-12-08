def greatest(array, e):
    for i in array:
        if i >= e: return False
    return True

def check_row(r, c, board):
    left = []
    right = []
    target = board[r][c]
    for l in range(0, c): left.append(board[r][l])
    for ri in range(c+1, len(board[r])): right.append(board[r][ri]) 
    if greatest(left, target) or greatest(right, target): return True
    return False
    
def col(r, c, board):
    up = []
    down = []
    target = board[r][c]

    for u in range(0, r): up.append(board[u][c])
    for d in range(r+1, len(board)): down.append(board[d][c])

    if greatest(up, target) or greatest(down, target): return True
    return False
grid = []
with open('./in.txt') as file:
    for line in file:
        row = []
        line = line.split('\n')[0]
        for i in range(len(line)): row.append(int(line[i]))
        grid.append(row)

c = 2*len(grid) + 2*len(grid[0]) - 4
#trim grid
for i in range(len(grid)):
    if i == 0 or i == len(grid) - 1: continue
    for j in range(len(grid[i])):
        if j == 0 or j == len(grid[i])-1: continue
        if check_row(i, j, grid) or col(i, j, grid): c += 1
print(c)
