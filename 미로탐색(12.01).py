#2178 미로탐색

# bfs? dfs? 우선 배열을 다 받고 1,1부터 시작해서
#인접한 칸(x:1,0,-1,0, y:0,-1,0,1) 중 1인거 큐에 넣기

import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

dx = [1,0,-1,0]
dy = [0,-1,0,1]

def bfs(x, y):
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                q.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1

    return graph[n-1][m-1]

print(bfs(0,0))