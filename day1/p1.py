import math

data = []
with open('./in.txt') as file:
    temp_data = []
    for line in file:
        if line != "\n":
            line = line.split('\n')[0]
            temp_data.append(int(line))
        else:
            data.append(temp_data)
            temp_data = []
    data.append(temp_data)

m = -math.inf
for arr in data:
    if sum(arr) > m: m = sum(arr)
print(m)
