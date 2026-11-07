from collections import deque

graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": ["G"], "F": [], "G": [], "H": []}
visits = 0

def bfs(g, start, goal):
    q = deque([(start, [start])])
    seen = {start}
    while q:
        node, path = q.popleft()
        if node == goal:
            return path
        for n in g[node]:
            if n not in seen:
                seen.add(n)
                q.append((n, path + [n]))
    return None

def dls(g, node, goal, limit, path):
    global visits
    visits += 1
    if node == goal:
        return "FOUND", path
    if limit == 0:
        if g[node]:
            return "CUTOFF", None
        return "FAILURE", None
    cutoff = False
    for n in g[node]:
        if n in path:
            continue
        status, result = dls(g, n, goal, limit - 1, path + [n])
        if status == "FOUND":
            return status, result
        if status == "CUTOFF":
            cutoff = True
    if cutoff:
        return "CUTOFF", None
    return "FAILURE", None

print("start equals goal")
print("BFS:", bfs(graph, "A", "A"))
print("DLS:", dls(graph, "A", "A", 0, ["A"]))

print()
print("unreachable goal (H has no edge into it)")
print("BFS:", bfs(graph, "A", "H"))
for limit in [1, 2, 3, 4]:
    print("DLS limit", limit, dls(graph, "A", "H", limit, ["A"]))

print()
cyc = {"A": ["B"], "B": ["A", "C"], "C": []}
print("graph with a cycle A <-> B")
print("BFS:", bfs(cyc, "A", "C"))
print("DLS limit 5:", dls(cyc, "A", "C", 5, ["A"]))

print()
print("node visits: IDDFS up to limit 3 compared with one DLS at limit 3")
total = 0
for limit in range(4):
    visits = 0
    dls(graph, "A", "G", limit, ["A"])
    print("limit", limit, "visits", visits)
    total += visits
print("IDDFS total visits:", total)
visits = 0
dls(graph, "A", "G", 3, ["A"])
print("single DLS at limit 3 visits:", visits)
