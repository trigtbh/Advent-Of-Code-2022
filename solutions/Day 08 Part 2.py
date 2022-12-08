import helper
with open(helper.nrml("day8.txt")) as f:
    lines = f.read().splitlines()


m = 0
for y in range(1, len(lines) - 1):
    for x in range(1, len(lines[0]) - 1):
        val = int(lines[y][x])
        something = []

        c = 0
        ty = y - 1
        while ty >= 0:
            c += 1
            if int(lines[ty][x]) < val:    
                ty -= 1
            else: break
        
        something.append(c)
        c = 0
        ty = y + 1
        while ty < len(lines):
            c += 1
            if int(lines[ty][x]) < val:    
                ty += 1
            else: break
        something.append(c)

        c = 0
        ty = x - 1
        while ty >= 0:
            c += 1
            if int(lines[y][ty]) < val:    
                ty -= 1
            else: break
        something.append(c)
        c = 0
        ty = x + 1
        while ty < len(lines):
            c += 1
            if int(lines[y][ty]) < val:    
                ty += 1
            else: break
        something.append(c)

        test = something[0] * something[1] * something[2] * something[3]
        if test > m:
            m = test


print(m)