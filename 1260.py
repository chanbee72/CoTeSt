import sys

input = sys.stdin.readline()
num_node, num_edge, start_node = map(int, input.split())

edges = [[] for _ in range(num_node+1)]

for _ in range(num_edge):
    edge = list(map(int, sys.stdin.readline().split()))
    edges[edge[0]].append(edge[1])
    edges[edge[1]].append(edge[0])

for edge in edges:
    edge.sort()


def bfs(start, visited):
    queue = [start]
    visited[start] = True
    
    while queue:
        s = queue.pop(0)
        print(s, end=" ")
        for node in edges[s]:
            if not visited[node]:
                visited[node] = True
                queue.append(node)


def dfs(start, visited):
    visited[start] = True
    print(start, end=" ")

    for node in edges[start]:
        if not visited[node]:
            dfs(node, visited)

visited = [False] * (num_node+1)
dfs(start_node, visited)
print()

visited = [False] * (num_node+1)
bfs(start_node, visited)