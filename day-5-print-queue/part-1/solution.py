import sys

lines = sys.stdin.readlines()
index = 0
parents = {}
children = {}
while len(lines[index].strip()) != 0:
    x, y = [int(i) for i in lines[index].split("|")]

    children[x] = children.get(x, set())
    children[x].add(y)

    parents[y] = parents.get(y, set())
    parents[y].add(x)

    index += 1

def is_correct(update):
    for i, page in enumerate(update):
        for j in range(i + 1, len(update)):
            if page in children[update[j]]:
                return False
        for j in range(i):
            if page in parents[update[j]]:
                return False
    return True

index += 1
total = 0
while len(lines[index].strip()) != 0:
    update = [int(i) for i in lines[index].split(",")]
    if is_correct(update):
        total += update[len(update) // 2]

    index += 1

print(total)

