#2606번 바이러스

import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
M = int(input())

count = 0

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N + 1)

def bfs():
    global count
    q = deque([1])
    while q:
        v = q.popleft()
        visited[v] = True
        for i in graph[v]:
            if not visited[i]:
                q.append(i)

bfs()

count = 0
for i in range(N + 1):
    if visited[i]:
        count += 1

print(count - 1)