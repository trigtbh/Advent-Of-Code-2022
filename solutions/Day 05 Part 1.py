import helper
with open(helper.nrml("day5.txt")) as f:
    lines = f.read()

board, instructions = lines.split("\n\n")
cols = [[], [], [], [], [], [], [], [], []]
for line in board.split("\n")[:-1]:
    reduced = ''.join(character for index, character in enumerate(line) if (index+1)%4 != 0)
    
    n = 3
    x = [reduced[i:i+n] for i in range(0, len(reduced), n)]
    for i, y in enumerate(x):
        if y != "   ":
            cols[i].insert(0, y[1])

for line in instructions.split("\n"):
    _, count, _, start, _, end = line.split(" ")
    for i in range(int(count)):
        cols[int(end)  - 1].append(cols[int(start) - 1].pop(-1))

print("".join(c[-1] for c in cols))