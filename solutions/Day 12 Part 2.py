import helper
with open(helper.nrml("day12.txt")) as f:
    c = f.read()
    grid = c.splitlines()
    flattened = c.replace("\n", "")

def valid_pos(y, x):
    x = [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]
    v = [t for t in x if 0 <= t[0] < len(grid) and 0 <= t[1] < len(grid[0])]
    return v


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop(-1)

    def is_empty(self):
        return len(self.stack) == 0

def one_below(previous, target):
    pt = grid[previous[0]][previous[1]]
    tt = grid[target[0]][target[1]]
    
    
    if grid[previous[0]][previous[1]] == "S":
        return ord(tt) - ord("a") <= 1
    if grid[target[0]][target[1]] == "E":
        return ord("z") - ord(pt) <= 1

    return ord(tt) - ord(pt) <= 1

def find_indices(list_to_check, item_to_find):
    indices = []
    for idx, value in enumerate(list_to_check):
        if value == item_to_find:
            indices.append(idx)
    return indices

temp = flattened.index("S")

validpaths = []
ei = flattened.index("E")
end = (ei // len(grid[0]), ei % len(grid[0]))

for si in find_indices(flattened, "a") + [temp]:
    #print(si)
    start = (si // len(grid[0]), si % len(grid[0]))


    paths = Queue()
    startpath = Stack()
    startpath.push(start)
    paths.enqueue(startpath)

    visited_rooms = set()
    visited_rooms.add(start)

    canon_path = None
    while True:
        if paths.is_empty():
            break
        path = paths.dequeue()
        points = path.stack
        copy = points.copy()
        last = points[-1]

        if grid[last[0]][last[1]] == "E":
            validpaths.append(points[1:])
            break
        valid = valid_pos(*last)
        for point in valid:
            if one_below(last, point) and point not in visited_rooms:
                s = Stack()
                s.stack = points.copy() # stack abuse
                s.push(point)
                paths.enqueue(s)
                visited_rooms.add(point)



print(len(min(validpaths, key=len)))