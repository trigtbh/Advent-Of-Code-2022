import helper
with open(helper.nrml("day10.txt")) as f:
    lines = f.read().splitlines()

register = 1
counter = 0
s = []
for item in lines:
    x = item.split(" ")
    if x[0] == "noop":
        
        counter += 1
        if counter in [20, 60, 100, 140, 180, 220]:
            s.append(register * counter)
    elif x[0] == "addx":
        for i in range(2):
            
            counter += 1
            if counter in [20, 60, 100, 140, 180, 220]:
                s.append(register * counter)
        register += int(x[1])

print(register)
print(sum(s))