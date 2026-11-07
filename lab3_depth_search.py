graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": ["G"], "F": [], "G": []}

def dls(node, goal, limit, path):
    if node == goal:
        return "FOUND", path
    if limit == 0:
        if graph[node]:
            return "CUTOFF", None
        return "FAILURE", None
    cutoff = False
    for n in graph[node]:
        if n in path:
            continue
        status, result = dls(n, goal, limit - 1, path + [n])
        if status == "FOUND":
            return status, result
        if status == "CUTOFF":
            cutoff = True
    if cutoff:
        return "CUTOFF", None
    return "FAILURE", None

def iddfs(start, goal, max_depth):
    tried = []
    for limit in range(max_depth + 1):
        tried.append(limit)
        status, result = dls(start, goal, limit, [start])
        if status == "FOUND":
            return status, result, tried
    return status, None, tried

print("DLS")
for limit in [1, 2, 3, 4]:
    status, path = dls("A", "G", limit, ["A"])
    print("limit", limit, status, path)

print()
print("IDDFS")
for m in [1, 2, 3, 4]:
    status, path, tried = iddfs("A", "G", m)
    print("max depth", m, status, path, "limits tried:", tried)
