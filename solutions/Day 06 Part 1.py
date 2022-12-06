import helper
with open(helper.nrml("day6.txt")) as f:
    line = f.read()

for i in range(len(line) - 4):
    sub = line[i:i+4]
    if len(sub) == len(set(sub)):
        print(i+4)
        break