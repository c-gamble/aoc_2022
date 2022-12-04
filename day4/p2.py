
def check_common(arr1, arr2):
    for e in arr1:
        if e in arr2: return True
    return False
c = 0
with open('./in.txt') as file: 
    for line in file:
        line = line.split('\n')[0]
        r1, r2 = line.split(',')[0], line.split(',')[1]
        elf1, elf2 = r1.split('-'), r2.split('-')

        arr1 = [x for x in range(int(elf1[0]), int(elf1[1])+1)]
        arr2 = [x for x in range(int(elf2[0]), int(elf2[1])+1)]
        if check_common(arr1, arr2): c += 1
print(c)
