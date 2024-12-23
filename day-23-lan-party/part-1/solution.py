import sys

edges = {}
for line in sys.stdin:
    if len(line.strip()) == 0:
        break

    a, b = line.strip().split("-")
    edges[a] = edges.get(a, set())
    edges[a].add(b)
    edges[b] = edges.get(b, set())
    edges[b].add(a)

found = set()
for a, adjacents in edges.items():
    for b in adjacents:
        common = (adjacents & edges[b]) - { a, b }
        for c in common:
            if a.startswith("t") or b.startswith("t") or c.startswith("t"):
                entry = tuple(sorted([a, b, c]))
                found.add(entry)

print(len(found))

