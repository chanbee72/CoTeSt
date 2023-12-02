import sys

N = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split())
M = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)


visited = [False for _ in range(N+1)]

def bfs(a, b):
    queue = [a]

    while queue:
        #print(visited)
        #print(queue)
        x = queue.pop(0)

        if x == b:
            return visited[x]

        for element in graph[x]:
            if not visited[element]:
                queue.append(element)
                visited[element] = visited[x] + 1

    return -1

result = bfs(a, b)
print(result)