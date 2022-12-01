import helper
with open(helper.nrml("day1.txt")) as f:
    lines = f.read()

ind = lines.split("\n\n")

print(sum(sorted(sum(int(y) for y in x.split("\n")) for x in ind)[::-1][:3]))