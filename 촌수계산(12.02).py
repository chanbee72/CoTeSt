#2644번 촌수계산

#graph => 사람들간의 관계
# N = 9 (사람들의 수)
# a, b = 구하려는 사람1, 2(이들의 관계)
# M = 7 (부모<->자식 관계 수)
# graph = [], [], ,,, []
# x는 부모, y는 자식
# 1 : [2, 3] , 2 : [7, 8], 3 : [1], 4 : [5, 6]
# 부모 자식 관계 양쪽 다 넣고, 찾기 시작
# bfs로 찾기 시작해서 하나 올라갈때마다 visited 수정, 찾으면 스탑

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
a, b = map(int, input().split())
M = int(input())

graph = [[] for _ in range(N + 1)]
for i in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (N + 1)

suc = 0

def bfs(v):
    global suc
    q = deque([v])
    visited[v] = 0
    while q:
        v = q.popleft()
        if v == b:
            suc = 1
        for i in graph[v]:
            if visited[i] == False:
                q.append(i)
                visited[i] = visited[v] + 1

bfs(a)
if suc == 1:
    print(visited[b])
else:
    print(-1)

print(visited)