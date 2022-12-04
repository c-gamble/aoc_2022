def check_common(arr1, arr2):
    for e in arr1:
        if e not in arr2: return False
    return True

c = 0
with open('./in.txt') as file:
    for line in file:
        line = line.split('\n')[0]
        r1, r2 = line.split(',')[0], line.split(',')[1]
        elf1, elf2 = r1.split('-'), r2.split('-')

        if int(elf1[0]) >= int(elf2[0]) and int(elf1[1]) <= int(elf2[1]) or int(elf1[0]) <= int(elf2[0]) and int(elf1[1]) >= int(elf2[1]): c+=1
print(c)
