import sys

lines = sys.stdin.readlines()
index = 0
parents = {}
children = {}
while len(lines[index].strip()) != 0:
    x, y = [int(i) for i in lines[index].split("|")]

    if x not in children:
        children[x] = set()
    children[x].add(y)

    if y not in parents:
        parents[y] = set()
    parents[y].add(x)

    index += 1

def is_correct(update):
    for i, page in enumerate(update):
        for j in range(i + 1, len(update)):
            if page in children[update[j]]:
                return False
    return True

def corrected_middle(update):
    indegrees = [len([child for child in parents[page] if child in update]) for page in update]

    corrected = []
    while len(corrected) < len(update):
        index = 0
        while index < len(update) and update[index] in corrected:
            index += 1

        for i, indegree in enumerate(indegrees):
            if indegree == 0:
                index = i
                break

        corrected.append(update[index])
        indegrees[index] = -1
        for child in children[update[index]]:
            if child in update:
                indegrees[update.index(child)] -= 1

    return corrected[len(corrected) // 2]

index += 1
total = 0
while len(lines[index].strip()) != 0:
    update = [int(i) for i in lines[index].split(",")]
    if not is_correct(update):
        total += corrected_middle(update)

    index += 1

print(total)

