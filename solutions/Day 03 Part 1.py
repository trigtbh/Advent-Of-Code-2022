import helper
with open(helper.nrml("day3.txt")) as f:
    lines = f.readlines()

indexes = "-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(sum(indexes.index(list(set(line[:len(line)//2]).intersection(set(line[len(line)//2:])))[0]) for line in lines))
