import helper
with open(helper.nrml("day4.txt")) as f:
    lines = f.read().splitlines()

s = 0
for line in lines:
    l1, l2 = line.split(",")
    (min1, max1), (min2, max2) = l1.split("-"), l2.split("-")
    min1, max1, min2, max2 = (map(int, (min1, max1, min2, max2)))
    if (min1 <= min2 <= max1) or (min2 <= min1 <= max2):
        s += 1

print(s)