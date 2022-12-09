import helper
with open(helper.nrml("day9.txt")) as f:
    lines = f.read().splitlines()


incl = set()
hy, hx = 0, 0

pos = [(0, 0)] * 10
incl.add(pos[-1])
for line in lines:
    direction, magnitude = line.split(" ")
    magnitude = int(magnitude)
    for i in range(magnitude):
        copy = [x for x in pos]
        if direction == "U": hy += 1
        if direction == "D": hy -= 1
        if direction == "L": hx -= 1
        if direction == "R": hx += 1
        pos[0] = (hy, hx)
        for p in range(1, len(pos)):
            if abs(pos[p][0] - pos[p - 1][0]) > 1 or abs(pos[p][1] - pos[p - 1][1]) > 1:
                pos[p] = (pos[p][0] + (1 if pos[p - 1][0] - pos[p][0] > 0 else (0 if pos[p-1][0] - pos[p][0] == 0 else -1)), pos[p][1] + (1 if pos[p - 1][1] - pos[p][1] > 0 else (0 if pos[p-1][1] - pos[p][1] == 0 else -1)))

            #elif abs(pos[p][0] - pos[p - 1][0]) > 1 or abs(pos[p][1] - pos[p - 1][1]) > 1:
            #    pos[p] = copy[p - 1]
        incl.add(pos[-1])

print(len(incl))