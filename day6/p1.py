string = ""
with open('./in.txt') as file:
    for line in file:
        line = line.split('\n')[0]
        string += line

def occur(s, e):
    r = 0
    for c in s:
        if e == c: r += 1
    return r
def check_repeating(s):
    for c in s:
        if occur(s, c) > 1: return True
    return False
#window size 4
ans = ''
for i in range(len(string)):
    curr_window = string[i:i+4]
    if check_repeating(curr_window): continue
    else:
        print(i+4)
        break
