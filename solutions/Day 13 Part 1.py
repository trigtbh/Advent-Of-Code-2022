import helper
with open(helper.nrml("day13.txt")) as f:
    pairs = f.read().split("\n\n")

pairs = [tuple(eval(x) for x in p.split("\n")) for p in pairs]

s = []

def recurse(left, right):
    for i in range(min(len(left), len(right))):
        l = left[i]
        r = right[i]
        if isinstance(l, list) and not isinstance(r, list):
            r = [r]
            x = recurse(l, r)
            if x is not None:
                return x
        elif not isinstance(l, list) and isinstance(r, list):
            l = [l]
            x = recurse(l, r)
            if x is not None:
                return x
        elif isinstance(l, list) and isinstance(r, list):
            x = recurse(l, r)
            if x is not None:
                return x
        else:
            if l < r:
                return True
            elif l > r:
                return False

    if len(left) < len(right):
        return True
    elif len(left) > len(right):
        return False

for i, tup in enumerate(pairs):
    if recurse(tup[0], tup[1]):
        s.append(i + 1)

print(sum(s))
