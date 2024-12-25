import sys

lines = [line.strip() for line in sys.stdin if len(line.strip()) != 0]

def parse_lock(lines):
    lock = []
    for i in range(5):
        h = 0
        while h < 5 and lines[h + 1][i] == "#":
            h += 1
        lock.append(h)
    return tuple(lock)

def parse_key(lines):
    key = []
    for i in range(5):
        h = 0
        while h < 5 and lines[5 - h][i] == "#":
            h += 1
        key.append(h)
    return tuple(key)

def fit(lock, key):
    return all((i + j) <= 5 for i, j in zip(lock, key))

locks = []
keys = []
for i in range(0, len(lines), 7):
    schematic = lines[i:i + 7]
    if schematic[0] == "#####":
        locks.append(parse_lock(schematic))
    else:
        keys.append(parse_key(schematic))

total = 0
for lock in locks:
    for key in keys:
        if fit(lock, key):
            total += 1
print(total)

