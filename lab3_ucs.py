import heapq
from collections import deque

# weights chosen
graph = {
    "A": [("B", 1), ("C", 5)],
    "B": [("D", 4), ("E", 1)],
    "C": [("F", 2), ("G", 7)],
    "D": [],
    "E": [("G", 1)],
    "F": [],
    "G": []}

def ucs(start, goal):
    pq = [(0, start, [start])]
    done = set()
    order = []
    while pq:
        cost, node, path = heapq.heappop(pq)
        if node in done:
            continue
        done.add(node)
        order.append(node)
        if node == goal:
            return cost, path, order
        for n, w in graph[node]:
            heapq.heappush(pq, (cost + w, n, path + [n]))

def bfs(start, goal):
    q = deque([(start, [start])])
    seen = {start}
    while q:
        node, path = q.popleft()
        if node == goal:
            return path
        for n, w in graph[node]:
            if n not in seen:
                seen.add(n)
                q.append((n, path + [n]))

def path_cost(path):
    total = 0
    for i in range(len(path) - 1):
        for n, w in graph[path[i]]:
            if n == path[i + 1]:
                total += w
    return total

cost, path, order = ucs("A", "G")
print("UCS path:", path)
print("UCS cost:", cost)
print("UCS processing order:", order)
print("cost added up again:", path_cost(path))

bpath = bfs("A", "G")
print("BFS path:", bpath, "hops:", len(bpath) - 1, "cost:", path_cost(bpath))
