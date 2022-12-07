import helper
with open(helper.nrml("day7.txt")) as f:
    lines = f.read().splitlines()

directories = {"/": 0}
path = "/"
i = 1
scanned = set()
while i < len(lines):
    line = lines[i]
    if line.startswith("$ "):
        line = line[2:]
        if line.startswith("cd "):
            new = line[3:]
            if new == "..":
                if path != "/":
                    path = "/".join(path.split("/")[:-1])
            else:
                if path != "/":
                    path = path + "/" + new
                else:
                    path = "/" + new
            if path not in directories:
                directories[path] = 0
            i += 1
        elif line.startswith("ls"):
            index = i+1
            i += 1
            while not lines[index].startswith("$ "):
                num, _ = lines[index].split(" ")
                if num != "dir" and path not in scanned:

                    for item in directories:
                        if path.startswith(item):
                            directories[item] += int(num)

                index += 1
                i += 1
                if index >= len(lines): break
            scanned.add(path)

x = {k: v for k, v in directories.items() if v <= 100000}
print(sum(list(x.values())))
