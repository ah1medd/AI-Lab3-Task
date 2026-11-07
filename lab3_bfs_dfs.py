from collections import deque

graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": ["G"], "F": [], "G": []}

def bfs(start, goal):
    q = deque([(start, [start])])
    seen = {start}
    order = []
    while q:
        node, path = q.popleft()
        order.append(node)
        print("processed", node, "path", path)
        if node == goal:
            return path, order
        for n in graph[node]:
            if n not in seen:
                seen.add(n)
                q.append((n, path + [n]))
        print("   queue:", [x[0] for x in q])

def dfs(start, goal):
    stack = [(start, [start])]
    seen = set()
    order = []
    while stack:
        node, path = stack.pop()
        if node in seen:
            continue
        order.append(node)
        print("processed", node, "path", path)
        if node == goal:
            return path, order
        seen.add(node)
        for n in reversed(graph[node]):
            stack.append((n, path + [n]))
        print("   stack:", [x[0] for x in stack])

print("BFS")
path, order = bfs("A", "G")
print("final path:", path)
print("visit order:", order)
print()
print("DFS")
path, order = dfs("A", "G")
print("final path:", path)
print("visit order:", order)
