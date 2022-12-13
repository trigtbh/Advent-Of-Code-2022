import helper
with open(helper.nrml("day13.txt")) as f:
    pairs = f.read().replace("\n\n", "\n").split("\n")

pairs = pairs + ["[[2]]", "[[6]]"]
temp = []
good = []
mapped = {}
for p in pairs:
    test = p.replace("[]", "[0]")
    test = test.replace("[", "").replace("]", "")
    
    mapped[p] = eval("[" + test + "]")
    good.append(p)
z = sorted(good, key=lambda x: mapped[x])

i1 = z.index("[[2]]") + 1
i2 = z.index("[[6]]") + 1

print(i1 * i2)