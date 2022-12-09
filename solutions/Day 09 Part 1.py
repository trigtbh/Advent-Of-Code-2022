import helper
with open(helper.nrml("day9.txt")) as f:
    lines = f.read().splitlines()

incl = set()
hy, hx = 0, 0
ty, tx = hy, hx
incl.add((ty, tx))
for line in lines:
    direction, magnitude = line.split(" ")
    magnitude = int(magnitude)
    for i in range(magnitude):
        tempy, tempx = hy, hx
        if direction == "U": hy += 1
        if direction == "D": hy -= 1
        if direction == "L": hx -= 1
        if direction == "R": hx += 1
        if abs(hy - ty) > 1 or abs(hx - tx) > 1:
            ty, tx = tempy, tempx
            incl.add((ty, tx))

print(len(incl))