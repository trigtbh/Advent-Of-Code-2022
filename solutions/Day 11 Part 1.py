import helper
with open(helper.nrml("day11.txt")) as f:
    m = f.read().split("\n\n")

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
for monkey in m:
    tempm = Monkey(monkey)
    monkeys.append(tempm)
    mcounts[tempm.num] = 0

for _ in range(20):
    for monkey in monkeys:
        while len(monkey.items) > 0:
            mcounts[monkey.num] += 1
            item = monkey.items.pop()
            newval = eval(monkey.op.replace("old", "0x" + str(item))) // 3
            if newval % monkey.test== 0:
                monkeys[monkey.throw_true].items.append(hex(newval)[2:])
            else:
                monkeys[monkey.throw_false].items.append(hex(newval)[2:])
        #for m in monkeys:
        #    print(m.items)
        #input()
    if _ % 1 == 0:
        print(_)

for m in monkeys:
    print(m.items)
maximum = sorted(list(mcounts.values()), reverse=True)
print(mcounts)
print(maximum[0] * maximum[1])