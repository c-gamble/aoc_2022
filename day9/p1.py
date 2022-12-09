moves = []
with open("./day9/in.txt") as file:
    for line in file:
        line = line.split("\n")[0].split(" ")
        moves.append([line[0], int(line[1])])

def move(head, tail):
    x = abs(head[0] - tail[0])
    y = abs(head[1] - tail[1])

    if x <= 1 and y <=1: pass
    elif x >=2 and y >= 2: tail = (head[0] - 1 if head[0] > tail[0] else head[0]+1, head[1] - 1 if head[1] > tail[1] else head[1]+1)
    elif x >=2: tail = (head[0] - 1 if head[0] > tail[0] else head[0]+1, head[1])
    elif y >= 2: tail = (head[0], head[1] - 1 if head[1] > tail[1] else head[1]+1)

    return tail

h, t = (0, 0), (0, 0)
adj_x = {"L": 0, "U": -1, "R": 0, "D": 1}
adj_y = {"L": -1, "U": 0, "R": 1, "D": 0}
visited = set()
for mv in moves:
    direction = mv[0]
    mag = mv[1]
    for _ in range(mag):
        h = (h[0] + adj_x[direction], h[1] + adj_y[direction])
        t = move(h, t)
        visited.add(t)
print(len(visited))