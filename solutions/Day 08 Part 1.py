import helper
with open(helper.nrml("day8.txt")) as f:
    lines = f.read().splitlines()
    
vis = set()
for y in range(len(lines)):
    vis.add((y, 0))
    vis.add((y, len(lines[0]) - 1))

for x in range(len(lines)):
    vis.add((0, x))
    vis.add((len(lines) - 1, x))

for y in range(1, len(lines) - 1):
    for x in range(1, len(lines[0]) - 1):
        val = int(lines[y][x])
        if val > max(map(int, [c for c in lines[y][:x]])) or val > max(map(int, [c for c in lines[y][x+1:]])) or val > max(map(int, [lines[ty][x] for ty in range(y)])) or val > max(map(int, [lines[ty][x] for ty in range(y+1, len(lines))])):
            vis.add((y, x))

print(len(vis))