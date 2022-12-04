import helper
with open(helper.nrml("day4.txt")) as f:
    lines = f.read().splitlines()

s = 0
for line in lines:
    l1, l2 = line.split(",")
    (min1, max1), (min2, max2) = l1.split("-"), l2.split("-")
    min1, max1, min2, max2 = list(map(int, [min1, max1, min2, max2]))
    if (min1 <= min2 and max1 >= max2) or (min2 <= min1 and max2 >= max1):
        s += 1

print(s)