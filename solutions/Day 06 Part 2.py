import helper
with open(helper.nrml("day6.txt")) as f:
    line = f.read()

for i in range(len(line) - 14):
    sub = line[i:i+14]
    if len(sub) == len(set(sub)):
        print(i+14)
        break