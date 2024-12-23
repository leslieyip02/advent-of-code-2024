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

visited = set()
def expand(current_nodes, next_node):
    common = edges[next_node]
    for node in current_nodes:
        common = common & edges[node]
    duplicates = set(current_nodes)
    duplicates.add(next_node)
    common = common - duplicates

    current_nodes = sorted([*current_nodes, next_node])
    longest = ",".join(current_nodes)
    if longest in visited:
        return longest

    visited.add(longest)
    if len(common) == 0:
        return longest

    for node in common:
        entry = expand(current_nodes, node)
        if len(entry) > len(longest):
            longest = entry

    return longest

longest = ""
for a in edges.keys():
    entry = expand([], a)
    if len(entry) > len(longest):
        longest = entry

print(longest)

