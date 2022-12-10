import helper
with open(helper.nrml("day10.txt")) as f:
    lines = f.read().splitlines()

register = 1
counter = 0
s = []
for item in lines:
    x = item.split(" ")
    if x[0] == "noop":
        
        if register - 1 <= counter % 40 <= register + 1:
            print("#", end="")
        else:
            print(".", end="")
        
        counter += 1
        if counter in map(lambda x: x, [40, 80, 120, 160, 200, 240]):
            print("")
    elif x[0] == "addx":
            
        if  register - 1 <= counter % 40 <= register + 1:
            print("#", end="")
        else:
            print(".", end="")
        counter += 1
        if counter in map(lambda x: x, [40, 80, 120, 160, 200, 240]):
            print("")
        if  register - 1 <= counter % 40 <= register + 1:
            print("#", end="")
        else:
            print(".", end="")
        register += int(x[1])
        
        counter += 1
        if counter in map(lambda x: x, [40, 80, 120, 160, 200, 240]):
            print("")