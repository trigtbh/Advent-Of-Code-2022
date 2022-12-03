import helper
with open(helper.nrml("day3.txt")) as f:
    lines = f.read().splitlines()

# lines = open("../inputs/day3.txt").read().splitlines()

lines = [lines[n:n+3] for n in range(0, len(lines), 3)]

indexes = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(sum(indexes.index(list(set(group[0]).intersection(set(group[1]).intersection(set(group[2]))))[0]) for group in lines))