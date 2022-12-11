import math 

monkeys  = []
with open("./day11/in.txt") as file:
    curr_monkey = {}
    for line in file:
        if line == "\n": 
            monkeys.append(curr_monkey)
            curr_monkey = {}
            continue
        else:
            if "Monkey" in line: continue
            elif "Starting" in line:
                curr_monkey['start'] =[int(x) for x in line.split("Starting items: ")[1].split(", ")]
            elif "old * old" in line:
                curr_monkey['op'] = "square"
                curr_monkey['inc'] = 1
            elif "Operation" in line: 
                curr_monkey['op'] = line.split("old ")[1].split(" ")[0]
                curr_monkey['inc'] = int(line.split("old ")[1].split(" ")[1])
            elif "Test" in line: 
                curr_monkey['test'] = int(line.split("divisible by ")[1])
            elif "true" in line: 
                curr_monkey['true'] = int(line.split("throw to monkey ")[1])
            elif "false" in line:
                curr_monkey['false'] = int(line.split("throw to monkey ")[1])
    monkeys.append(curr_monkey)
    
divisors = []
for monkey in monkeys: 
    divisors.append(monkey['test'])
    monkey['inspected'] = 0


lcm = math.lcm(*divisors)

for _ in range(10000):
    for i, monkey in enumerate(monkeys):
        for item in monkey['start']:
            monkey['inspected'] += 1
            if monkey['op'] == "*": item *= monkey['inc']
            elif monkey['op'] == "+": item += monkey['inc']
            elif monkey['op'] == "square": item *= item
            item = item%lcm
            if item % monkey['test'] == 0: 
                monkeys[monkey['true']]['start'].append(item)
            elif item % monkey['test'] != 0: 
                monkeys[monkey['false']]['start'].append(item)
        monkey['start'] = []

inspections = []
for monkey in monkeys: inspections.append(monkey['inspected'])
print(sorted(inspections, reverse = True)[:2][0]*sorted(inspections, reverse = True)[:2][1])