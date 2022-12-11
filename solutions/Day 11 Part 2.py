import helper
with open(helper.nrml("day11.txt")) as f:
    m = f.read().split("\n\n")

#m = open("day11.txt").read().split("\n\n")

class Monkey:
    def __init__(self, str):
        lines = str.split("\n")
        self.num = lines[0][7:-1]
        self.items = [hex(int(x))[2:] for x in lines[1][18:].split(", ")]
        self.op = lines[2][19:]
        self.test = int(lines[3][21:])
        self.throw_true = int(lines[4][29:])
        self.throw_false = int(lines[5][30:])


mcounts = {}
monkeys = []

divs = []

for monkey in m:
    tempm = Monkey(monkey)
    monkeys.append(tempm)
    mcounts[tempm.num] = 0
    divs.append(tempm.test)

s = 1
for item in divs:
    s *= item

for _ in range(10000):
    for monkey in monkeys:
        while len(monkey.items) > 0:
            mcounts[monkey.num] += 1
            item = monkey.items.pop()
            newval = eval(monkey.op.replace("old", "0x" + str(item))) % s
            if newval % monkey.test == 0:
                monkeys[monkey.throw_true].items.append(hex(newval)[2:])
            else:
                monkeys[monkey.throw_false].items.append(hex(newval)[2:])

maximum = sorted(list(mcounts.values()), reverse=True)
print(maximum[0] * maximum[1])